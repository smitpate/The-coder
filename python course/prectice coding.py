subscribe = 1000
likes = 200
comment = 55

if subscribe>150 and likes>150 and comment>50:
    print('amazing video')
# change
b = [1,2,321,5,5,2,52,1452,1,15]
print(b)
b= list(set(b))
print(b)
most = max(set(b), key=b.count)
print(most)
odd_squares = []
for i in range(10):
    if i % 2 == 1:
        odd_squares.append(i**2)

print(odd_squares)
# change
def sum(*a):
    result  = 0
    for i in a :
        result = result+ i
        return result

res = sum(2,3)
print(res)
# to reverse the name
name = 'smit'[::-1]
print(name)
