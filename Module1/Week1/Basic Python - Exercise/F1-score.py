def evaluate_classification_model(tp, fp, fn):
     if not isinstance(tp, int):
          print('tp must be int')
          return
     
     if not isinstance(fp, int):
          print('fp must be int')
          return
     
     if not isinstance(fn, int):
          print('fn must be int')
          return

     if tp <= 0 or fn <= 0 or fp <= 0:
          print('tp and fp and fn must be greater than zero')
          return

     precision = tp / (tp + fp)
     recall = tp / (tp + fn)  
     f1_score = 2 * (precision * recall) / (precision + recall)

     print(f'precision is {precision}')
     print(f'recall is {recall}')
     print(f'f1_score is {f1_score}')


evaluate_classification_model(2, 3, 4)
evaluate_classification_model('a', 3, 4)
evaluate_classification_model(2, 'a', 4)
evaluate_classification_model(2, 3, 'a')
evaluate_classification_model(2, 3, 0)
evaluate_classification_model(-2.1, 3, 0)

