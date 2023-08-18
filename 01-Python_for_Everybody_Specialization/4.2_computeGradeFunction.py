# Take score input
# check for proper input
# check for grade 
# return grade string


promptScore = 'Enter score: '
score = float(input(promptScore))


def computegrade (score):
    try:
        if score <= 1.0:
            if score >= 0.9: grade = 'A'
            elif score >= 0.8: grade = 'B'
            elif score >= 0.7: grade = 'C'
            elif score >= 0.6: grade = 'D'
            elif score < 0.6: grade = 'F'
            return grade
        else:
            return 'Bad Score'
    except:
        return 'Bad Score'

print(computegrade(score))
