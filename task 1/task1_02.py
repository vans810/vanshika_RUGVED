string=input("Enter a string: ")
string=list(string)
string.sort()
for index in string:
    count=0
    count2=0
    for j in range(0,string.index(index)):
        if string[j]==index:
            count+=1
    if count>0:
        continue
    for j in string:
        if j==index:
            count2+=1
    print("count of " + index + " is " + str(count2) )
