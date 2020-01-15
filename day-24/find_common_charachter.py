import copy
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        duplicates = {}
        for char in A[0]:
            if char in duplicates:
                duplicates[char] += 1
            else:
                duplicates[char] = 1
        for i in range(1,len(A)):
            current_dup = {}
            for j in range(len(A[i])):
                if A[i][j] in duplicates:
                    if A[i][j] in current_dup:
                        current_dup[A[i][j]] += 1
                    else:
                        current_dup[A[i][j]] = 1
            for char in copy.deepcopy(duplicates):
                if not char in current_dup:
                    del duplicates[char]
                else:
                    if duplicates[char] > current_dup[char]:
                        duplicates[char] = current_dup[char]

        
        return [char for char in duplicates for count in range(duplicates[char])]
                
        