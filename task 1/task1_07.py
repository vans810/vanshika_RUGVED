n=input("Enter n: ")
n=(int)(n)
a=0;
b=1;
print(a)
print(b)
n=n-2
while(n!=0):
    sum=a+b
    print(sum)
    a=b
    b=sum
    n=n-1
