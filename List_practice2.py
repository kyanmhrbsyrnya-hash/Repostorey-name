fruits_list=['banana','cheery','coconat','apple','blue berry']
print(fruits_list[1:4])



#####
fruits_list=['banana','cheery','coconat','apple','blue berry']
fruits_list[0]='orange'
print(fruits_list)



####
fruits_list=['banana','cheery','coconat','apple','blue berry']
print(fruits_list[1:4])
fruits_list[0]='orange'




####
numbers_list=range(1,21,1)
number_nuws=[ ]
for number in numbers_list:
    if(number%3==0):
        print(number)
        number_nuws.append(number)
        print(number_nuws)
