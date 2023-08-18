# Take hours and rate input 
# check for input type in try and except
# calculate the gross pay 1.5 times rate per hour for above 40

promptHours = 'Enter Hours: '
promptRate = 'Enter Rate: '

try:
    hours = float(input(promptHours))
    rate = float(input(promptRate))

    if hours <= 40 :
        gpay = hours * rate
    else:
        gpay = (rate * 40) + ((hours - 40) * 1.5 * rate)
    
    print('Pay: '+str(gpay))
except:
    print('Error, please enter numeric input')
