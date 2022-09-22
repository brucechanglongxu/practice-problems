# A trie/prefix tree is a tree data structure used to efficiently store and retrieve keys in
# a dataset of strings. There are various applications of this data structure, such as autocomplete
# and spellchecker. Implement the Trie class:

# 1. Trie() initializes the trie object
# 2. void insert(String word) inserts the string word into the trie
# 3. booolean search(String word) returns true if the string word is in the trie and false otherwise
# 4. boolean startsWith(String prefix) returns true if there is a previously inserted string word that has the 
# prefix prefix and false otherwise

class Node:
  def __init__(self):
    self.children = [None]*26
    self.pcnt = 0
    self.cnt = 0

class Trie(object):
  def __init__(self):
    self.__trie = Node()
    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.__trie
        curr.pcnt += 1
        for c in word:
            if curr.children[ord(c)-ord('a')] is None:
                curr.children[ord(c)-ord('a')] = Node()
            curr = curr.children[ord(c)-ord('a')]
            curr.pcnt += 1
        curr.cnt += 1

    def countWordsEqualTo(self, word):
        """
        :type word: str
        :rtype: int
        """
        curr = self.__trie
        for c in word:
            if curr.children[ord(c)-ord('a')] is None:
                return 0
            curr = curr.children[ord(c)-ord('a')]
        return curr.cnt

    def countWordsStartingWith(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        curr = self.__trie
        for c in prefix:
            if curr.children[ord(c)-ord('a')] is None:
                return 0
            curr = curr.children[ord(c)-ord('a')]
        return curr.pcnt

    def erase(self, word):
        """
        :type word: str
        :rtype: None
        """
        cnt = self.countWordsEqualTo(word)
        if not cnt:
            return
        curr = self.__trie
        curr.pcnt -= 1
        for c in word:
            if curr.children[ord(c)-ord('a')].pcnt == 1:
                curr.children[ord(c)-ord('a')] = None  # delete all unused nodes
                return
            curr = curr.children[ord(c)-ord('a')]
            curr.pcnt -= 1
        curr.cnt -= 1  
