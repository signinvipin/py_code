# Create a function to find min and max input
# Take input and find if mix or max
# print min and max






def minMax():
    min = None
    max = None
    while True: 
        try:
            prompt = 'Enter a number: '
            number = input(prompt)

            if number == 'done': break

            if min is None or min > int(number):
                min = int(number)

            if max is None or max < int(number):
                max = int(number)
        except:
            print('Invalid input')
    print('Min: '+str(min)+', Max: '+str(max))

minMax()
