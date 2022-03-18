#1
numbers = [2,4,7,1,8.4,-3.3,7.1,-2,4,-1,7,-43,8,-3,6,9]
if len(numbers) % 2 == 0:
    print('Even',numbers)    
if len(numbers) % 2 != 0:
    print('Odd',numbers)

#2
numbers = [0,2,4,7,1,8,0,-3,7,0,-2,4,0,0,-1,7,-43,0,8,-3,6,9]
nums = []
for i in numbers:
    if i < 0:
        nums.append(-1)
    elif i > 0:
        nums.append(1)
    else:
        nums.append(0)    
    print(nums)

#3
my_list = [2,4,6,8,10,1,3,5,7,9,11,13,17]
even_i = []
for i in range(0, len(my_list)):
    if i % 2:
        even_i.append(my_list[i])
    print(even_i)

#4
numbers = [1,0,-2,4,3,6,6,3,5,8,4,2]
numbers.sort()
print(numbers[-1])





