string= input("Enter a sequence: ")
n=(int)(input("Enter the size of parts: "))
string=list(string)
N=len(string)
count=0
parts=[]
while(N-n>0):
    temp=""
    for index in range(count, count+n):
        temp=temp+string[index]
    parts.append(temp)
    count=count+n
    N=N-n
if(N-n<0):
    print("division in equal parts not possible")
else:
    print(parts)
