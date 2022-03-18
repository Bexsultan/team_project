#3
j = 4729461084
a = 237
p = 0
while j > 0:
    d = j % 10
    p = p + d
    j = j // 10
print(p)
