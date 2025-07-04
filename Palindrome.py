class Solution:
     def polindrome(self, num):
        self.num = num

        reversed = int(str(self.num) [::-1])
        print(reversed)
        if num == reversed:
            print(f"{self.num}palindrome")
        else:
            print("is not polindrome")
"""
        i = num

        reversed = 0

        while i > 0:
            remainder = i % 10
            reversed = remainder + (reversed * 10)
            i = i // 10
        if num == reversed:
            print(f"{self.num} is a palindrome number ")

        else:
            print("sorry mate this is not")"""

k1 = Solution()
k1.polindrome(353)