# Take hours and rate per hour input 
# compute gross pay of user

promptHour = 'Enter Hours: '
promptRate = 'Enter Rate: '

hours = input(promptHour)
rate = input(promptRate)

pay = int(hours)*int(rate)

print('Pay: '+str(pay))
