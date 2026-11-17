class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # naive approach would be to search through each possible pair in heights
        # take shorter height of the two, compare with the next inner height, if it is > than its current height, move in. 
        #compare new max area with new minum height * width (make sure to minus 1 everytime we move in)

       # edge case: what if both heights are equal
        left =0
        right = len(heights)-1
        maxArea=0
        minHeight=min(heights[right],heights[left])
        area = minHeight * (right -left)
        maxArea = max(area, maxArea)
        while left<right:
            if heights[left]<=heights[right]:
                minHeight = heights[left]
                area = minHeight * (right -left)
                left +=1
                
            else: 
                minHeight = heights[right]
                area = minHeight * (right -left)
                right-=1
                
            
            maxArea = max(area, maxArea)
        return maxArea


            #left = 0, right is 7, minheight is 1


