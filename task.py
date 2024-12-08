# first task
num1 = int(input('enter a number: '))
num2 = int(input('enter another number: '))
sum = num1 + num2
print(f"the sum of your numbers is {sum}")

# second task
mark = int(input('Please enter your score: '))

if mark >= 50:
    print("Congrats, you passed!")
else:
    print('Sorry, you failed.')

# third task
percentage = int(input('Enter your total mark percentage: '))

if percentage >= 92:
    grade = "A"
elif percentage >= 85:
    grade = "B"
elif percentage >= 75:
    grade = "C"
elif percentage >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is {grade}")

#forth task 
weekday = int(input('Enter a number: '))

match weekday:
    case 1:
        print('Sunday') 
    case 2:
        print('Monday') 
    case 3:
        print('Tuesday')
    case 4:
        print('Wednesday')
    case 5:
        print('Thursday')
    case 6:
        print('Friday')
    case 7:
        print('Saturday')
    case _:
        print('Invalid Weekday') 

#fifth task
p = int(input('enter the amount : '))
r = int(input('enter the interest percentage per annual: '))
t = int(input('How long is being invested (by years): '))
si = int((p*r*t)/100)
print(f"The Interest for your amount is {si}")

#sixth task
limit = int(input('Enter the limit: '))

num = range(1, limit+1)
odd_num = []
sum = 0

for n in num:
    if n%2 !=0:
        odd_num.append(n)
        sum += n

print(odd_num)
print(f"sum of odd numbers: {sum}")

#seventh task
row = 8

for r in range(1, row+1):
    for c in range(1, r+1):
        print(c, end=' ')
    print()    
    
#eighth task
num = int(input('Enter a number: '))

table = range(1, 11)

for n in table:
    product = n * num
    print(f"{n}*{num} = {product} ")
    
# nininth task
word = input('Enter the word: ')
forward = word.upper()
reverse = word[::-1]
backward = reverse.upper()


if forward == backward:
    print(f"{forward} is a palindrome")
else:
    print(f"{forward} is not a palindrome")
    
#tenth task
num = int(input('Enter a number: '))

if num>1:
    for i in range(2, (num//2)+1):
        if num%2 == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number")

#eleventh task
row = 4
num = 1

for r in range(1,row+1):
    for i in range(1, r+1):
        print(num, end=' ')
        num += 1
    print()

#twelvth task
def calculate_income_tax(annual_income):
    if annual_income <= 250000:
        tax = 0
    elif annual_income <= 500000:
        tax = (annual_income - 250000) * 0.05
    elif annual_income <= 1000000:
        tax = (250000 * 0.05) + (annual_income - 500000) * 0.2
    else:
        tax = (250000 * 0.05) + (500000 * 0.2) + (annual_income - 1000000) * 0.3
    return tax

annual_income = float(input("Enter the annual income: "))

tax_amount = calculate_income_tax(annual_income)

print(f"Income tax amount = {tax_amount:.2f}")
