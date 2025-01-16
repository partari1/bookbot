def main():
    file_contents = ""
    file_name = "books/frankenstein.txt"
    with open(file_name) as f:
        file_contents = f.read()

    char_dict = count_characters(file_contents)
    char_list = sort(char_dict)
    print(f"--- Begin report of {file_name} ---")
    print(f"{count_words(file_contents)} words found in document")
    print("")
    for char in char_list:
        print(f"The '{char['character']}' character was found {char['count']} times")
    print("--- End report ---")


def count_words(contents):
    return len(contents.split())

def count_characters(contents):
    counter = {}
    for c in contents.lower():
        if not c.isalpha():
            continue
        if c in counter:
            counter[c] += 1
        else:
            counter[c] = 1
    return counter

def sort_on(dict):
    return dict["count"]

def sort(characters):
    char_list  =[]
    for char in characters:
        char_list.append({"character": char, "count": characters[char]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list


main()