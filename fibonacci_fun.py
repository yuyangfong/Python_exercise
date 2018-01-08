def fibonacci_fun(f1, f2, fib_len):
    fibo = [f1, f2]
    while len(fibo) < fib_len:
        f1, f2 = f2 , f1 + f2
        fibo.append(f2)
    return fibo

f1 = int(input("第一個數字:"))
f2 = int(input("第二個數字:"))
fibo_len = int(input("數列函數:"))
print(fibonacci_fun(f1, f2, fibo_len))
