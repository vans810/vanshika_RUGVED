string1=input("enter a string: ")
string2=input("enter another string: ")
string1= list(string1)
string2= list(string2)

count3=0
for index in string1:
    count1=0
    count2=0
    for index1 in string1:
        if(index==index1):
          count1+=1
    for index2 in string2:
        if(index==index2):
          count2+=1
    if(count1!=count2):
        count3+=1
if count3>0:
    print("not anagram")
else:
    print("anagram")