number_list=[]
for i in range(5):
    print(("please write one number"))
    item=int(input())
    number_list.append(item)

number=0
for x in number_list:
    if x > 0:
        number=number + x
print(number)
