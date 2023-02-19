class Solution:
    def mySqrt(self, x: int) -> int:
        """
        
        1,4,9,16,25,...., x<2^31-1
        65536(2^16)
        100
        
        """
        sqrts = [i*i for i in range(0, 65536+1)]
        start = 0
        end = len(sqrts)
        # 큰 것들 중에 가장 작은 수 찾기
        # 작은 숫자를 찾았다 > 오른쪽으로 쭉?, 큰 숫자를 찾았다 > 왼쪽으로 쭉? 겨우 절반 줄임
        # 끝까지 가자.
        while start<=end:
            mid = start + int((end-start)/2)
            #print(f"{mid} - {sqrts[mid]} !=? x")
            if sqrts[mid] == x:
                return mid
            if sqrts[mid] < x:
                start = mid+1
            else:
                end = mid-1
        #print(f"start: {start}, end:{end}")
        return end
            
        