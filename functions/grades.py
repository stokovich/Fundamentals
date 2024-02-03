# •	2.00 – 2.99 - "Fail"
# •	3.00 – 3.49 - "Poor"
# •	3.50 – 4.49 - "Good"
# •	4.50 – 5.49 - "Very Good"
# •	5.50 – 6.00 - "Excellent"

def convert_grades_to_word(grade):
    if 2.00 <= grade <= 2.99:
        print('Fail')
    elif 3.00 <= grade <= 3.49:
        print('Poor')
    elif 3.50 <= grade <= 4.49:
        print('Good')
    elif 4.50 <= grade <= 5.49:
        print('Very Good')
    elif 5.50 <= grade <= 6.00:
        print('Excellent')


grade_input = float(input())

convert_grades_to_word(grade_input)

