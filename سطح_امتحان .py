# --- Python Assessment Exercises ---
# This file contains the solutions to the initial level assessment.

# 1. Conditional Statements (If-Elif-Else)
# Goal: Check if a number is positive, negative, or zero.
num = int(input('لطفا یک عدد وارد کنید: '))
if num < 0:
    print('عدد منفی است')
elif num > 0:
    print('عدد مثبت است')
else:
    print('صفر است')

# 2. While Loop
# Goal: Print numbers in descending order until 1.
num_loop = int(input('لطفا یک عدد وارد کنید برای شمارش معکوس: '))
while num_loop >= 1:
    print(num_loop)
    num_loop = num_loop - 1

# 3. List Operations (Correction of Syntax Errors)
# Goal: Iterating through a list of fruits.
fruits = ['apple', 'banana', 'cherry', 'orange']
for name in fruits:
    print(name)


####
# --- For Loop Practice ---
# This file focuses on iterating through lists using the 'for' loop.

# Practice: Iterating through a list of fruits
fruits = ['apple', 'banana', 'cherry', 'orange']

print("List of fruits:")
for name in fruits:
    print(f"- {name}")

# Note: In Python, the 'for' loop syntax is 'for variable in iterable:' 
# without the need for parentheses around the expression.

