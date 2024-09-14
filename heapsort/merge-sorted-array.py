class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        while (n != 0):
            if (nums1[i] == 0):
                nums1[i] = nums2[j]
                j = j + 1
                n = n - 1
            else:
                nums1[i] = nums1[i]
                m = m - 1
            i = i + 1
        self.order(nums1)

    def order(self,nums1):
        size = len(nums1)
        self.buildHeap(size,nums1)

        for i in range(size-1, 0, -1):
            nums1[i], nums1[0] = nums1[0],nums1[i]
            self.maxHeap(0, i, nums1)

        ##.    1
        ##.  2.   3 
        ##0.  0  0
        
        ## buildheap
        ## max heap
        
    def buildHeap(self,size,nums):
        for i in range(size//2-1, -1, -1):
            self.maxHeap(i, size, nums)
    def maxHeap(self,i,size,nums):
        largest = i
        right = 2*i + 1
        left = 2*i + 2

        if (right < size and nums[largest] < nums[right]):
            largest = right
        if (left < size and nums[largest] < nums[left]):
            largest = left
        if (i != largest):
            nums[i], nums[largest] = nums[largest], nums[i]
            self.maxHeap(largest, size, nums)

    ## complexidade de tempo: O(n)
    ## complexidade de espaço: O(1)