# 49. Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

class Solution(object):
    def groupAnagrams(self, strs):
        # Initialize a defaultdict with a list as the default factory.
        # defaultdict allows us to avoid key errors when accessing keys that don't exist.
        # The default factory here is list, so if a key is not present, it will create an empty list for that key.
        res = defaultdict(list)

        # Iterate through each string in the input list 'strs'.
        for s in strs:
            # Initialize a list 'count' with 26 zeros, representing the count of each letter from 'a' to 'z'.
            count = [0] * 26

            # Count the occurrences of each character in the current string 's'.
            for c in s:
                # Increment the count for the current character 'c' in the 'count' list.
                # 'ord(c) - ord("a")' gives the index of the character in the range [0, 25].
                count[ord(c) - ord("a")] += 1

            # Convert the 'count' list to a tuple and use it as a key to group anagrams.
            # Anagrams will have the same counts for each character, resulting in the same tuple.
            # Append the current string 's' to the list associated with the tuple key in the 'res' defaultdict.
            res[tuple(count)].append(s)

        # Return the values (lists of anagrams) from the defaultdict as a result.
        return res.values()
