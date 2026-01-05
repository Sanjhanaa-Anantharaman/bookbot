from stats import count_words, count_characters, sort_characters
import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1) 
def main():
    file_path= sys.argv[1]
    
    word_count = count_words(file_path)
    print(f"Found {word_count} total words")
    
    charac_count = count_characters(file_path)
    print(charac_count)
    
    lst = []
    for key, value in charac_count.items():
        lst.append({"char": key, "num": value})
    
    sorted_charac = sort_characters(lst)
    for i in sorted_charac:
        print(f"{i['char']}: {i['num']}")

if __name__ == "__main__":
    main()