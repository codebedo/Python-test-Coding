class solution:
    def __init__(self):
        self.memo = {}


    def fib(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]

        if n <= 1:
            return n
        # burada dict olark saklıyor  #fibonacci tanimi yapıldı
        self.memo[n] = self.fib(n -1) + self.fib(n-2)
        return self.memo[n]


sol = solution()
print(sol.fib(10))



class mysolution:
    def __init__(self):
        self.memo = {}


    def fibo(self, n : int)-> int:
        if n in self.memo:
            return self.memo[n]
        if n <= 1:
            return n

        self.memo[n] = self.fibo(n -1) + self.fibo(n-2)
        return self.memo[n]


class secondSolution:
    def __init__(self):
        self.memo = {} # amaç geçici dict oluşturmak


    def fioo(self, n: int) -> int:
        if n in self.memo:
            return  self.memo[n]
        if n <= 1:
            return n

        self.memo[n] = self.fioo(n-1) + self.fioo(n-2)
        return self.memo[n]