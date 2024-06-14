def count_words_in_dict(file_path):
    with open(file_path, 'r') as file_name:
        word_count = {}
        for sentence in file_name:
            sentence = sentence.rstrip('\n')
            for word in sentence.split():
                word = word.lower()
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

        return word_count


if __name__ == "__main__":
    file_path = 'D:/AIO-Exercise/Module1/Week2/Data Structure - Exercise/P1_data.txt'

    count_words = count_words_in_dict(file_path)
    print(count_words)
