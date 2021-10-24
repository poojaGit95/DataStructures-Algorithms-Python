import random

user = input('enter your name \n')
print('\n WELCOME ',user.upper(), 'TO WORD GUESS')
word_list = {"SECRET":"S*C**T", "FRUIT":"*RU*T", "INDIA":"I**IA", "DOLLARS":"DO**AR*", "WASHINGTON":"WAS**NG*O*",
             "NEBRASKA":"NE**AS**"}
word = random.choice(list(word_list))
question = word_list.get(word)
attempt = 2
guess = question.count('*')


print('\n YOUR QUESTION IS ', question)
i=1
while i<=attempt:
    q = question
    for j in range(guess):
        ans = input('\n Enter your guess')
        q = q.replace('*',ans,1)
        print(q)
    i=i+1
    if(q.lower()==word.lower()):
        print('\n YOU HAVE GUESSED IT RIGHT!!')
        break
    else:
        print('\n Incorrect, retry')


if(q.lower()!=word.lower()):
    print('\n Incorrect answer, you have exceeded your attempts')









































               

























