# Take score input 
# Check the input by try and except for input error
# Check for grade score falls
# Output the grade

try:
    prompt = 'Enter score: '
    score = float(input(prompt))

    if score <= 1.0:
        if score >= 0.9:
            grade = 'A'
        elif score >= 0.8:
            grade = 'B'
        elif score >= 0.7:
            grade = 'C'
        elif score >= 0.6:
            grade = 'D'
        elif score < 0.6:
            grade = 'F'

        print(grade)

    else:
        print('Bad score')

except:
    print('Bad score')
