a = [[1,2,3],[4,5,6]]

print(a)

print(list(zip(*a)))

print(list(zip( [[1,2,3],[4,5,6]] )))

print(list(zip([1,2,3], [4,5,6])))

# avg = [sum(x)/len(x) for x in zip(*a)]