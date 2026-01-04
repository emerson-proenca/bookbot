import sys

from stats import count_char, count_words, sort_dict


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    content: str = get_book_text(path)
    num_words: int = count_words(content)
    count: dict[str, int] = count_char(content)
    hashmap: list[dict[str, int]] = sort_dict(count)

    pretty_print(path, num_words, hashmap)


def get_book_text(path: str) -> str:
    with open(path) as f:
        content = f.read()
        return content


def pretty_print(path: str, num_words: int, hashmap: list[dict]):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in range(len(hashmap)):
        if hashmap[i]["char"].isalpha():
            print(f"{hashmap[i]['char']}: {hashmap[i]['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
