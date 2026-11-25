answer_to_question  = input("What is the answer to the Great Question of Life, the universe and everything? ")

if answer_to_question == str(42):
    print('Yes')
elif answer_to_question.lower() == 'forty-two':
    print('Yes')
elif answer_to_question.lower() == 'forty two':
    print('Yes')
else:
    print('No')    
