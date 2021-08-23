number_list=[]
for i in range(3):
    print(("please write one number"))
    item=int(input())
    number_list.append(item)

number_list.sort()
print(number_list[-1])
