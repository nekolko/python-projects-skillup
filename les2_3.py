from random import randint

list_1=[]
list_2=[]
num = int(input('Enter range of characters :'))
for i in range(num):       
    list_1.append(randint(1,100))
    list_2.append(randint(1,100 ))

print ('First list : ', list_1)
print ('Second list : ', list_2)


list_3=list_1+list_2
print ('List with elemens from 1 & 2 :')
print (list_3)



list_3=[]
for i in list_1:
    if i not in list_3:
        list_3.append(i)
for i in list_2:
    if i not in list_3:
        list_3.append(i)
print ('List with elements from 1 & 2 without repeats :')
print (list_3)


list_3=[]
for i in list_1:
    if i in list_2:
        list_3.append(i)
print ('List with common elements :')
print (list_3)


list_3=list(set(list_1))+list(set(list_2))
print ('List with unique elements :')
print (list_3)


list_3=[min(list_1), min(list_2), max(list_1), max(list_2)]
print ('List with min/max :')
print (list_3)
