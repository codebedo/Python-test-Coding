class Solution(object):
    def isPalindrome(self,x):
        self.x = x
        original = self.x
        reversed = 0

        while(x > 0):
            reversed = reversed * 10 + (x%10)
            x//= 10

        if reversed == original:
            print(f"{self.x} is a palindrome")
        else:
            print(f"{self.x} reserved {reversed} thi end this is not palindrome")






k1 = Solution()

k1.isPalindrome(123)



