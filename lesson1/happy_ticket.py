def hpticket(arr):
    test = []
    c = arr[0]
    c.split()
    for i in range(0, len(c)):
        test.append(c[i])
    if int(test[0]) + int(test[1]) == int(test[2]) + int(test[3]):
        return 'Yes'
    return 'No'


arr = ['0001']
print(hpticket(arr))
