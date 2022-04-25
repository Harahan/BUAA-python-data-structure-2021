arr1 = list(input().split())
arr2 = list(input().split())
for i in range(len(arr2)):
    if arr2[i] == "O":
        print(arr1[i], end="")
    elif arr2[i] == "B-LOC":
        print("<LOC>" + arr1[i], end="")
        if i + 1 == len(arr2) or arr2[i + 1] != "I-LOC":
            print("</LOC>", end="")
    elif arr2[i] == "I-LOC":
        print(arr1[i], end="")
        if i + 1 == len(arr2) or arr2[i + 1] != "I-LOC":
            print("</LOC>", end="")
