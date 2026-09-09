num=input("Enter a number to check hill number: ")
num=list(num)
count=0
for index in range(len(num)-1):
    if num[index+1]< num[index]:
        count=index
        break
count2=0
for index in range(count, len(num)-1):
    if(num[index+1]> num[index]):
        count2+=1
if count2>0:
    print("not hill")
else:
    print("hill")


