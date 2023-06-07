# 1532 -> 2*2*2*2 + 3*3*3*3 + 5*5*5*5 + 1*1*1*1  = 

# Armstrong Number 1 to 10000




for num in range(1,10001):  # 25
    length = len(str(num))   # 2
    safe = num
    sum = 0
    while num > 0:
        rem = num % 10      # rem = 2
        sum += (rem ** length)   # sum = 20 + 180
        num = num // 10   # num = 0
    
    if sum == safe:   # 723 == 1532
        print(sum,end=' ')


# 6 -> 1,2,3 -> 1+2+3 = 6



# function_name =  lambda argument : task
print()
sum = lambda num1,num2 : num1 + num2

print(sum(10,20))  # 30
print()

square = lambda num1 : num1 ** 2

print(square(30))   # 900

# ---------------------------
def power1(n):
    return lambda a:a*n

fun4 = power1(4)

print(fun4(20))  # 80

print (fun4(20))