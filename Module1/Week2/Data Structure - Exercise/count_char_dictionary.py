def count_char_in_dict(string):
    key_values = {}
    for word in string.split():
        for char in word:
            if char.isalpha():
                if char in key_values:
                    key_values[char] += 1
                else:
                    key_values[char] = 1

    sorted_items = sorted(key_values.items(), key=lambda item: item[1])
    return dict(sorted_items)


if __name__ == "__main__":
    string = input('')

    count_chars = count_char_in_dict(string)
    print(count_chars)
