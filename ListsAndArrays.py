"""x = [9, 10,12, 12]
print(x)

y = 0
while y <= 10:
    x.append(y)
    print(x)
    y += 1


    print(x)"""

mine_Array = [12,5,7,8,8,1,2,8]
checked_array = mine_Array[6]

for i in mine_Array:
    if i < checked_array:
        checked_array =i

print('Lowest Value', checked_array)

