

# using if else , elif
points = int(input('What are your current points:'))

if points <=100:
    print('You do not qualify')

elif points > 100 and points <= 1000:
    print('You get a free phone')

elif points > 1000 and points < 2000:
    print('You get a free bike')
    # nested
    if points > 1500:
        print('You bonus Points')
    else:
        print('No bonus pints')

else:
    print('You get a TRIP to coast')




# elif used for multiple conditions