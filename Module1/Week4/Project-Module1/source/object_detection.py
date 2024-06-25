import cv2
import numpy as np
from PIL import Image
import streamlit as st

MODEL = "./Module1/Week4/Project-Module1/source/model/MobileNetSSD_deploy.caffemodel"
PROTOTXT = "./Module1/Week4/Project-Module1/source/model/MobileNetSSD_deploy.prototxt.txt"


def process_image(image):
    blob = cv2.dnn.blobFromImage(
        cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5
    )
    net = cv2.dnn.readNetFromCaffe(PROTOTXT, MODEL)
    net.setInput(blob)
    detections = net.forward()
    return detections


def annotate_image(image, detections, confidence_threshold=0.5):
    # loop over the detections
    (h, w) = image.shape[:2]
    for i in np.arange(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        if confidence > confidence_threshold:
            # extract the index of the class label from the `detections`,
            # then compute the (x, y)-coordinates of the bounding box for
            # the object
            idx = int(detections[0, 0, i, 1])
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (start_x, start_y, end_x, end_y) = box.astype("int")

            # draw bouding box
            cv2.rectangle(image, (start_x, start_y),
                          (end_x, end_y), (0, 255, 0), 3)

            label = f'{idx}: {confidence:.2f}'
            top_label = start_y - 15 if start_x - 15 > 15 else start_y + 15
            cv2.putText(image, label, (start_x, top_label),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.85, (0, 255, 0), 3)

    return image


def main():
    st.title('Object Detection for Images')
    file = st.file_uploader('Upload Image', type=['jpg', 'png', 'jpeg'])
    if file is not None:
        st.image(file, caption="Uploaded Image")

        image = Image.open(file)
        image = np.array(image)
        detections = process_image(image)
        processed_image = annotate_image(image, detections)
        st.image(processed_image, caption="Processed Image")


if __name__ == "__main__":
    main()
