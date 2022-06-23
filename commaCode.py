def editList(spam):
    answer = ''
    for index, item in enumerate(spam):
        if index ==0 : # first element in spam
            newAnswer = item
        elif (index == len(spam) - 1): # last element in spam
            newAnswer = answer + ', and ' + item
        else:
            newAnswer = answer + ', ' + item

        answer = newAnswer

    return answer

spam = ['apples', 'bananas', 'tofu', 'cats']
print(editList(spam))
#print(editList([]))
