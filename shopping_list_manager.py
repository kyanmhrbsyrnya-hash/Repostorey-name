shopping_list=[]
while True:
    item = input('کالا را وارد کنید (برای پایان "done" را بنویسید): ')
    if item == 'done':
        break 
    shopping_list.append(item)
print("لیست نهایی شما:")
print(shopping_list)
