
# simple interest
for number in range(1,10,1):
    client_name = str(input('client name'))
    principle = 60000
    rate = 9
    time = 3

    print('Your Name is ', client_name)
    print('Your Principle is', principle, 'KES')
    print('The rate is at ', rate, '%')
    print('Period taken is ', time, 'Months')

    # do maths
    # we bring in arithmetic operators
    # +, -, * , /
    simple_interest = (principle * rate* time)/100
    print('You will be paying ', simple_interest, 'KES')