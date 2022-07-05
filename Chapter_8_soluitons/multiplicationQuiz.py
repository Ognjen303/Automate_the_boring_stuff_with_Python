import pyinputplus as pyip
import random, time

numberOfQuestions = 10
correctAnswers = 0
for questionNumber in range(1, numberOfQuestions + 1):

    # Pick two random numbersL
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)

    try:
        # Right answers are handled by allowRegexes.
        # Wrong answers are handled by blockRegexes. with a custom message.
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)],
                              blockRegexes=[('.*', 'Incorrect')],
                              timeout = 8, limit = 3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else: # else is optional in try except block and if and else if
        # This block runs if noexceptions were raised in the try block.
        print('Correct!')
        correctAnswers += 1
    time.sleep(1) # Brief pause to let user see the result.

print('Score: %s / %s' % (correctAnswers, numberOfQuestions))
