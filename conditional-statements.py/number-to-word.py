'''
num = eval(input('enter any number between 1-10: '))
if num == 1:
    print('one')
elif num == 2:
    print('two')
elif num == 3:
    print('three')
elif num == 4:
    print('four')
elif num == 5:
    print('five')
elif num == 6:
    print('six')
elif num == 7:
    print('seven')
elif num == 8:
    print('eight')
elif num == 9:
    print('nine')
elif num == 10:
    print('ten')
else:
    print('invalid')                                    
'''
'''
num = eval(input('enter any number between 1-10: '))
if num in range(1, 11):
    if num == 1:
        print('one')
    elif num == 2:
        print('two')
    elif num == 3:
        print('three')
    elif num == 4:
        print('four')
    elif num == 5:
        print('five')
    elif num == 6:
        print('six')
    elif num == 7:
        print('seven')
    elif num == 8:
        print('eight')
    elif num == 9:
        print('nine')
    elif num == 10:
        print('ten')
else:
    print('invalid')                                    
'''

num = eval(input('enter any number between 1-10: '))
num_word = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'}
if num in num_word:
    # print(num_word[num])
    print(num_word.get(num))
else:
    print('invalid')    