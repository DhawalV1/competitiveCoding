class Solution(object):
    def isHappy(self, n):

        sq_sum = 0
        b = []
		#as long as list of squares doesnt have 1 run the loop
        while(sq_sum!=1):
            a = [int(i) for i in str(n)]
			#find the square of digits
            for i in a:
                sq_sum+=i*i
			#if square is present, loop exist, break from loop	
            if sq_sum in b:
                break
            b.append(sq_sum)
            n = sq_sum
            sq_sum=0
		# if no cycle exist, the while loop has exited because of 1 in list at last position
        if b[-1]==1:
            return True
			
        return False