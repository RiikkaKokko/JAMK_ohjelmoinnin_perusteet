pisteet_list=[]

for i in range(5):
    pisteet = int(input("Give points: "))
    print(pisteet)
    pisteet_list.append(pisteet)

print(pisteet_list)
max_pisteet=max(pisteet_list)
min_pisteet=min(pisteet_list)
summa_pisteet=sum(pisteet_list)

tulos=summa_pisteet-max_pisteet-min_pisteet
print("Total points are " + str(tulos))