class solution:
    def __init__(self):
        self.memo = {}


    def fib(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]

        if n <= 1:
            return n
        self.memo[n] = self.fib(n -1) + self.fib(n-2)
        return self.memo[n]


sol = solution()
print(sol.fib(10))