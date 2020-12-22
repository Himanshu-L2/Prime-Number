n = int(input('Please enter your number.'))
flag = 0
for i in range (2,n):
    if ((n % i) == 0):
        flag = 1

if(flag==1):
    print("Non-Prime")
else:
    print("Prime")