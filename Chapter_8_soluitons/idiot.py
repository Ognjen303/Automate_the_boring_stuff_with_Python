import pyinputplus as pyip

while True:
    prompt = 'Want to know how to keep an idiot busy for hours?\n'
    # .inputYesNo guarantees that returned value is yes or no
    response = pyip.inputYesNo(prompt)

    if response == 'no':
        break

print('Thank you, have a nice day.')
