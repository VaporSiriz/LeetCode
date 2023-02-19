class Solution:
    def mySqrt(self, x: int) -> int:
        """
        
        1,4,9,16,25,...., x<2^31-1
        65536(2^16)
        100
        
        """
        sqrts = []
        for i in range(0, 65536+1):
            sqrts.append(i*i)
        
        for index, sqrt in enumerate(sqrts):
            #print(f"{index}, {x}>?{sqrt}")
            if x<sqrt:
                #print(sqrts[index-1])
                return index-1
        