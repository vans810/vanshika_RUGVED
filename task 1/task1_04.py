def selection_sort(arr):
    arr=list(arr)
    string2=""
    for i in range(len(arr)):
        smallest=i
        for j in range(i+1, len(arr)):
            if arr[j]<arr[smallest]:
                arr[j],arr[smallest]=arr[smallest],arr[j]
                smallest=j
        string2+=arr[i]
    return string2
print(selection_sort(input("Enter a string: ")))

