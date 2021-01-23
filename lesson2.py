# we learn control statements
# if, if else, elif, for, while
# if, if else, elif, - used for decisions

marks = int(input('What mark did you get:'))

# the if block works when condition 'marks <= 30' is true
if marks <= 30:
    print('You have Failed')
    print('They get a book')
    bonus = 10
    marks = marks + bonus
    print('You marks are now', marks)


# the else block works when condition 'marks <= 30' is false
else:
    print('You have passed')
    print('they get a mathematical set')
    bonus = 20
    marks = marks + bonus
    print('your marks are now ', marks)

# if else is for one condition



