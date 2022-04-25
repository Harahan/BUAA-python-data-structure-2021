array1 = list(input().split())
array2 = list(input().split())
for i in range(len(array1)):
    if array2[i] == 'O':
        print(array1[i], end='')
    elif array2[i] == 'I-LOC' and i + 1 < len(array1) and array2[i + 1] == 'I-LOC':
        print(array1[i], end='')
    elif array2[i] == 'B-LOC' and i > 0 and array2[i - 1] == 'B-LOC':
        print('</LOC>' + '<LOC>' + array1[i], end='')
        if array2[i + 1] == 'O':
            print('</LOC>', end='')
    elif array2[i] == 'B-LOC':
        print('<LOC>' + array1[i], end='')
    elif array2[i] == 'I-LOC':
        print(array1[i] + '</LOC>', end='')
if array2.pop() == 'B-LOC':
    print('</LOC>', end='')
