class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        ## insertion sort > guarda o valor em uma variavel e fica comparaando, vai dando swap
        ## da swap ate o final do sorted part

        if len(names) == 1:
            return names
        for i in range(1, len(names)): ## de 1 a 3
            j = i ## 1
            while (j != 0): ## 1
                aux = heights[j] ## 165
                if aux > heights[j - 1]:
                    heights[j - 1], heights[j] = heights[j], heights[j - 1]
                    names[j - 1], names[j] = names[j], names[j - 1] ### [155,150,185]
                j = j - 1
        return names

## complexidade de espaço: O(1)
## complexidade de tempo: O(n)2

## https://leetcode.com/problems/sort-the-people/