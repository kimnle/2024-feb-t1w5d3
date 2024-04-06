# If a number is a prime or not
number = int(input("Enter a number: ")) # 13

for i in range(2, number): # 2 - 12
    if number % i == 0: # 13 % 2 = 1, 13 % 3 = 1, 13 % 4 = 1, 13 % 12 = 1
        print("Not a prime")
        break
else:
    print("A prime")