def count_words(content: str) -> int:
    return len(content.split())


def count_char(content: str) -> dict[str, int]:
    new_content: str = content.lower()
    hashmap: dict[str, int] = {}
    for char in new_content:
        if char in hashmap:
            hashmap[char] += 1
        else:
            hashmap[char] = 1
    return hashmap


def sort_dict(hashmap: dict) -> list[dict[str, int]]:
    new_dict: list[dict] = []
    for k, v in hashmap.items():
        tmp: dict[str, int] = {}
        tmp["char"] = k
        tmp["num"] = v
        new_dict.append(tmp)
    return sorted(new_dict, reverse=True, key=sort_on)


def sort_on(items):
    return items["num"]
