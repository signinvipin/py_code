# Create a function computePay
# Takes hours and rate input 
# Calculate over-time gross pay with time and a half

promptHours  = 'Enter Hours: '
promptRate = 'Enter Rate: '

hours = float(input(promptHours))
rate = float(input(promptRate))

def computepay(hrs, rate):
    if hrs <= 40:
        grosspay = hrs * rate
    else:
        grosspay = ((40 + ((hrs - 40) * 1.5)) * rate)

    print('Pay: '+str(grosspay))

computepay(hours, rate)
