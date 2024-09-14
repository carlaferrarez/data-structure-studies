class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        ## contar os segundos por cada vez na fila, dependendo do k
        if (len(tickets) == 1):
            return tickets[0]
        person = tickets[k] ## person = 5
        position = 0
        time_count = 0
        while (person != 0): 
            if (position == k): ## sim, 0 == 0, nao
                person = person - 1 ## 4, 3
                k = len(tickets) ## 4
                position = 0 

            if (tickets[0] > 0):
                tickets[0] = tickets[0] - 1  ## 4, 0, 0, 0, 3
                time_count = time_count + 1 ## 1 , 2, 3, 4, 5

            tickets.append(tickets[0])
            tickets.pop(0)
            position = position + 1 

        return time_count

## complexidade de espaço = O(1)
## complexidade de tempo = O(n)

## https://leetcode.com/problems/time-needed-to-buy-tickets/








        