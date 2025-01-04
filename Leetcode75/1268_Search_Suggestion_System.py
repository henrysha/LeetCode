"""
1268. Search Suggestions System
Medium

You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of searchWord is typed.

Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"].
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"].
After typing mou, mous and mouse the system suggests ["mouse","mousepad"].
Example 2:

Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
Explanation: The only word "havana" will be always suggested while typing the search word.
 

Constraints:

- 1 <= products.length <= 1000
- 1 <= products[i].length <= 3000
- 1 <= sum(products[i].length) <= 2 * 104
- All the strings of products are unique.
- products[i] consists of lowercase English letters.
- 1 <= searchWord.length <= 1000
- searchWord consists of lowercase English letters.
"""

class TrieNode:
    def __init__(self, value: str, isLeaf: bool = False):
        self.value = value
        self.children = {}
        self.isLeaf = isLeaf
    
class Trie:
    def __init__(self):
        self.head = TrieNode(None)

    def insert(self, word: str):
        curr = self.head

        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                curr.children[c] = TrieNode(c)
                curr = curr.children[c]
        curr.isLeaf = True
        

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # construct trie
        trie = Trie()
        for product in products:
            trie.insert(product)

        result = [[] for _ in range(len(searchWord))] 

        head = trie.head

        prefix = ''

        # perform search
        for i in range(len(searchWord)):
            # return if node does not exist
            if searchWord[i] not in head.children:
                return result

            # get the current trie node
            head = head.children[searchWord[i]]
            prefix += head.value

            stack = [(head, prefix)]

            # get the tree lexicographically minimums products
            while len(result[i]) < 3 and stack:
                curr, prefix_str = stack.pop()
                if curr.isLeaf:
                    result[i].append(prefix_str)
                if len(curr.children) > 0:
                    for c in range(ord('z'), ord('a') - 1, -1):
                        char = chr(c)
                        if char in curr.children:
                            stack.append((curr.children[char], prefix_str + char))
        
        return result

