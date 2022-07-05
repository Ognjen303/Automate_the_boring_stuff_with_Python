import random, time

numberOfQuestions = 10
timeout = 8 # seconds

correctAnswers = 0

for i in range(1, numberOfQuestions + 1):

    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    numberOfTriesPerQuestion = 3
    start_time = time.time()

    while numberOfTriesPerQuestion > 0:


        print(f'Q{i}: {num1} x {num2} = ', end = '')
        answer = input()
        if time.time() - start_time > timeout:
            print('Out of time.')
            break

        try:
            answer = int(answer)
        except:
            print('Please input an integer number as answer')
            numberOfTriesPerQuestion -= 1
            continue

        if answer != (num1 * num2):
            print('Incorrect')
            numberOfTriesPerQuestion -= 1
            continue

        print('Correct!')
        time.sleep(1)
        correctAnswers += 1
        break # user wrote correct answer

print(f'Your score is {correctAnswers} out of {numberOfQuestions}.')
