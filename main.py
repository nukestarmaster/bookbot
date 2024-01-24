def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = len(file_contents.split())

        lower_caps_file_contents = file_contents.lower()
        letter_count = {}
        for c in lower_caps_file_contents:
            if c.isalpha():
                if c in letter_count:
                    letter_count[c] += 1
                else:
                    letter_count[c] = 1
        letter_list = []
        for d in letter_count:
            letter_list.append((d, letter_count[d]))
        letter_list.sort(reverse = True, key= tuple_get)

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document")
        print("")
        for t in letter_list:
            print(f"The {t[0]} character was found {t[1]} times")
        print("--- End report ---")

def tuple_get(tuple):
    return tuple[1]

main()