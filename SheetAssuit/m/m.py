inp = input()
if inp.isalpha() and inp.islower():
    print('ALPHA IS SMALL'.replace(' ','\n',1))
elif inp.isalpha() and inp.isupper():
    print('ALPHA IS CAPITAL'.replace(' ','\n',1))
else:
    print('IS DIGIT')