import pyinputplus as pyip

totalCost = 0

print('So you would like a sandwich?')

breadPrompt = 'Which bread type would you like? Wheat and white cost 50din. Sourdough is 70din. \n'
breadType = pyip.inputMenu(['wheat', 'white', 'sourdough'], prompt = breadPrompt)

if breadType == 'sourdough':
    totalCost += 70
else:
    totalCost += 50

proteinPrompt = 'What protein type would you like?\nChicken and ham cost 100din, while turkey and tofu cost 130din.\n'
proteinType = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], prompt = proteinPrompt)

if proteinType == 'turkey' or proteinType == 'tofu':
    totalCost += 130
else:
    totalCost += 100

print('Each extra topic costs 15din.')

wantCheese = pyip.inputYesNo(prompt = 'Would you like cheese? ')

if wantCheese == 'yes':
    cheeseType = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'], prompt = 'Which cheese would you like? \n')
    totalCost += 15

wantMayo = pyip.inputYesNo('Would you like mayo? ')
if wantMayo == 'yes':
    totalCost += 15

wantMustard = pyip.inputYesNo('Would you like mustard? ')
if wantMustard == 'yes':
    totalCost += 15

wantLettuce = pyip.inputYesNo('Would you like lettuce? ')
if wantLettuce == 'yes':
    totalCost += 15

wantTomato = pyip.inputYesNo('Would you like tomatoes?' )
if wantTomato == 'yes':
    totalCost += 15

sandwichNumber = pyip.inputInt('How many sandwiches would you like? ', min = 1)
print(f'Your total cost is {sandwichNumber * totalCost}din. Enjoy your lunch!')
