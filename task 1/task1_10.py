string=input("Enter a number:")
string=list(string)
sum=0
for i in range(len(string)-2, -1,-2 ):
    d=(int)(string[i])*2
    if(d>9):
        d=d-9
    sum=sum+d
for j in range(len(string)-1,-1,-2):
    sum=sum+(int)(string[j])
if(sum%10==0):
    print("Credit card number valid")
else:
    print("Credit card number not valid")
