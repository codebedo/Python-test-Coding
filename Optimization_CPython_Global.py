import time

global_var = 10


def func1():
    ans = 0
    for i in range(1000000):
        ans += global_var * i
    return  ans


def fun2():
    ans = 0
    local_var = global_var

    for i in range(1000000):
        ans += local_var *i

    return  ans


start = time.time()
func1()
print("Global erişim süresi: ", time.time() - start)

start = time.time()

fun2()
print("Local kopya süresi: ", time.time() - start)
