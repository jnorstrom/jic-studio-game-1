print("Hello World!")

name = input('Enter your name: ')

print('Hello, ', name, '!')

age = int(input("Enter your age: "))

if age < 13:
    print("It's great to be a kid")
elif age in range(12, 20):
    print("You are a teenager!")
else:
    print("Time to grow UP!!")
