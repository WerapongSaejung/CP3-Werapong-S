number = int(input())
star = ""
for i in range(number):
    star = (" "*(number-i-1)+("*"*(2*i+1)))
    print(star)