str1 = "NayaN"

var = len(str1)//2
print(var)   # 3

flag = 0   # Green
for i in range(0,var):
    if str1[i] == str1[len(str1) - i - 1]:
        flag = 1   # Red
    else:
        flag =0
        break


if flag == 1:   # 
    print("Palindrome") 


# ---------------------------
str2 = str1[::-1]
if str1 == str2:
    print("Plaindrome")