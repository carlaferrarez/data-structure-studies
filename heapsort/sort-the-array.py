class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ## [5,2,3,1] <    [5,2,3,10, 11]      [5,2,3,10, 11,8,5].    nums = [5,1,1,2,0,0]
        ##   5                  5                  5                             5
        ## 2   3             2    3            0       3                      1     1 
       ## 1                10  11         10     11   8    5               2   0   0  
 ##                                     3    1  2   1

 ## nums = [5,1,1,2,0,0]
        size = len(nums) ## 6
        self.buildHeap(size, nums) 
        ## remove o topo da arvore, adiciona na ultima posicao e tras a atual ultima posicao pro topo
        for i in range(size - 1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.maxHeap(nums, i,0)
        return nums

       ## fazer o max heap para eleger o maior numero.  len(nums)/2 - 1
    def maxHeap(self,nums, size, i):   ## i = 2, i = 1
        largest = i ## 1
        right = 2*(i) + 1 ## posiçao da direita
        left = 2*(i) + 2  ## posiçao da esquerda

        if (right < size and nums[largest] < nums[right]): ## comparo largest com size pra garantir que nao vai sair do array
            largest = right
        if (left < size and nums[largest] < nums[left]):
            largest = left
        if (i != largest): ## a posiçao que eu comecei nao é a maior ## 1 != 4
            nums[i], nums[largest] = nums[largest], nums[i]
            self.maxHeap(nums, size, largest) ##  preciso calcular o maxHeap de novo, porque se o largest tiver filhos, preciso ordenalos

    def buildHeap(self, size, nums):   ## 6, nums  ## o build heap so pega metade
        for i in range(size//2-1,-1, -1): ## 2, 1, 0. ## começo de tras pra frente, pra garantir que os filhos sao sempre menores
            self.maxHeap(nums, size, i)   

## complexidade de tempo: O(n log(n))
## complexidade de espaço: O(1)


        

        