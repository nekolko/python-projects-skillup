from random import randint

maxnum = int(input('Enter max number in tuple : '))
Range = int(input('Enter range of numbers : '))

tuple_1 = tuple(randint(1, maxnum) for i in range(Range))
tuple_2 = tuple(randint(1, maxnum) for i in range(Range))
tuple_3 = tuple(randint(1, maxnum) for i in range(Range))
print('Tuple 1 : ', tuple_1 , '\n','Tuple 2 : ', tuple_2 , '\n' ,'Tuple 3 : ' , tuple_3 )


res1 = set(tuple_1) & set(tuple_2) & set(tuple_3)
print('Common elements in three tuples :')
if len(res1) == 0:
    print('There are no common elements.', '\n')
else:
    print(*res1, sep=', ' )


unique1tup = tuple(i for i in tuple_1 if tuple_1.count(i) == 1)
unique2tup = tuple(i for i in tuple_2 if tuple_2.count(i) == 1)
unique3tup = tuple(i for i in tuple_3 if tuple_3.count(i) == 1)
print('Unique elements in each of the tuples :')
if len(unique1tup) > 0:
    print('Tuple 1 :', unique1tup)
else:
    print('No unique elemnts')
if len(unique2tup) > 0:
    print('Tuple 2 :', unique2tup)
else:
    print('No unique elemnts')
if len(unique3tup) > 0:
    print('Tuple 3 :', unique3tup, '\n')
else:
    print('No unique elemnts', '\n')


print('Match in exact place and meaning :', '\n')
minlen = min(len(tuple_1), len(tuple_2), len(tuple_3))
counter = 0
for i in range(minlen):
    if tuple_1[i] == tuple_2[i] == tuple_3[i]:
        counter += 1
        print(tuple_1[i])
if counter == 0:
    print('Match not found((')