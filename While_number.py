count=(10)
while(count>1):
    print(count)
    count=count-1
print('done')



####رسیدن به عدد حدس زده شده
num=int(input('لطفا یک عدد واردکنید:'))
numa=(1)
while(numa!=num):
    print(numa)
    numa=numa+1
print('you found it')



####توان اعداد۲ به صورت حرفه ای
num=2
while(num<100):
    print(num)
    num=num*2


####
friends=['nikan','farnam','hasan','mamad']
for name in friends:
    print(f'hello_{name}')
