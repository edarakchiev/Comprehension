start = int(input())
stop = int(input())
number = [num for num in range(start, stop + 1)]
divisible = [num for num in range(2, 11)]
result = [el for el in number if any([el % x == 0 for x in divisible])]
print(result)