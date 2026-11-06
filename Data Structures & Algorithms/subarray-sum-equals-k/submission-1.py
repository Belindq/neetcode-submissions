class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        out=0
        prefix=defaultdict(int)
        prefixsums=defaultdict(int)
        prefix[0]=nums[0]
        prefixsums[0]=1
        for n in range(1,len(nums)):
            prefix[n]= prefix[n-1]+nums[n]
        
        print('prefix', prefix)
    
        # two pointers, left and for loop for right sliding window
        # record prefix sums in hash map 
        # find k-current presum and find # of times it appaers in hash
        #current presum-past presum = k
        #k+past presum = current presum needed
        #current presum - k = past presume needed
        for x in range(len(nums)):
            if prefix[x]-k in prefixsums:
                out+=prefixsums[prefix[x]-k]
            prefixsums[prefix[x]] +=1   
       
        return out

                


