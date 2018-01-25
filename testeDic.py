dic = [
    {1:2, 2:4},
    {3:1},
    {3:5}
]

# for i in dic[0].values():
dic[0][3] = 'k'
print(dic)

# x = [ {} for i in range(3) ]
# print(x)

x = [i for i in range(3)]
print('>', x)

print(float("inf") > float("inf")+1)