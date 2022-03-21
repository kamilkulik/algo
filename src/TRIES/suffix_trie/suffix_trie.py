class SuffixTrie:
    def __init__(self, string: str):
        self.root = {}
        self.end_symbol = "*"
        self.populate_suffix_trie_from(string)

    def populate_suffix_trie_from(self, string: str) -> None:
        for i in range(len(string)):
            self.insert_substring_startin_at(string, i)

    def insert_substring_startin_at(self, string: str, i: int) -> None:
        node = self.root
        for j in range(i, len(string)):
            letter = string[j]
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node[self.end_symbol] = True

    def contains(self, string: str) -> bool:
        node = self.root
        for j in range(len(string)):
            letter = string[j]
            if letter not in node:
                return False
            node = node[letter]
        return self.end_symbol in node