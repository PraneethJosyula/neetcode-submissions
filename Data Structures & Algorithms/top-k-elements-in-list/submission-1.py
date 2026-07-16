class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        heap=[]
        for n in nums:
            count[n]=1+count.get(n,0)
        for n in count.keys():
            heapq.heappush(heap,(count[n],n))

            if len(heap)>k:
                heapq.heappop(heap)

        result=[]

        while k>0:
            k-=1
            result.append(heapq.heappop(heap)[1])
        return result