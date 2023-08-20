# Take input a number
# check for input type
# check if it is 'done'
# calculate total, count, and average
# return error or calculated data

## while loop is indefinite and works until
## certain condition is met

def average():
    number = None
    count = 0
    total = 0

    while number != 'done':
        try:
            prompt = 'Enter a number: '
            number = input(prompt)

            total = total + int(number)
            count = count + 1
        except:
            print('Invalid input')

    print('Total '+str(total)+' Count '+str(count)+' Average '+str(total/count))


average()
