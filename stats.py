def count_words(file_path):
        with open(file_path, 'r') as file:
            text = file.read()
            count_words = len(text.split())
        return count_words

def count_characters(file_path):
    with open(file_path, 'r') as file:
        letters = {}
        text = file.read()
        for char in text:
            if char.isalpha():
                char = char.lower()
                if char in letters:
                    letters[char] += 1
                else:
                    letters[char] = 1
    return letters
        
def sort_characters(char_dict):
    char_dict.sort(key=lambda item: item["num"], reverse=True)
    return char_dict