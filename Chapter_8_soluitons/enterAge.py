while True:
    print('Enter your age:')
    age = input()
    try:
        age = int(age)
    except:
        print('Please enter a valid numerical age.')
        continue
    if age < 1:
        print('Please enter a positive number for age.')
        continue
    break

print(f'Your age is {age}')
