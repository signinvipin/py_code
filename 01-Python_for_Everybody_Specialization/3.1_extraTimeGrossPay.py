# Take hours worked input and the rate
# Calculate hourly rate for upto 40 hours
# Calculate 1.5 times rates for above it
# Output gross pay


promptHours = 'Enter Hours: '
promptRate = 'Enter Rate: '

hours = float(input(promptHours))
rate = float(input(promptRate))

if hours <= 40 :
    grossPay = hours * rate
    print('Pay: '+str(grossPay))
else :
    grossPay = (rate * 40) + ((hours-40)* 1.5*rate)
    print('Pay: '+str(grossPay))
