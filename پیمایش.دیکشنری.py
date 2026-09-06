products = {
    "Laptop": 1500,
    "Mouse": 200,
    "Keyboard": 1200
}
for keys,values in products.items():
    if(values>=1000):
        print(keys,values,values*0.9)



####
students = {
    "Ali": 18,
    "Sara": 20,
    "Reza": 15,
    "Nika": 19
}
while True:
    key=input('لطفا اسم شخص رو .ارد کنید')
    print(students.get(key,'اسم یافت نشد'))
    if(key=='exite'):
        break



####
