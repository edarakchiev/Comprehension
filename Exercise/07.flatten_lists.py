data = input().split("|")[::-1]
number = [i.split() for i in data]
flatten = [num for row in number for num in row]
print(" ".join(flatten))

