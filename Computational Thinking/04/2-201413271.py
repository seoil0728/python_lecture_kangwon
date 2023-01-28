print('201413271 김석우')

first_grade = float(input('첫 번째 과목의 학점을 입력하세요. : '))
if first_grade > 4.5 or first_grade < 0:
    print('0과 4.5 사이의 값을 입력하세요.')
else:
    second_grade = float(input('두 번째 과목의 학점을 입력하세요. : '))
    if second_grade > 4.5 or second_grade < 0:
        print('0과 4.5 사이의 값을 입력하세요.')
    else:
        third_grade = float(input('세 번째 과목의 학점을 입력하세요. : '))
        if third_grade > 4.5 or third_grade < 0:
            print('0과 4.5 사이의 값을 입력하세요.')
        else:
            average = (first_grade + second_grade + third_grade) / 3
            if average == 4.5:
                total_grade = 'A+'
            elif average >= 4.0:
                total_grade = 'A'
            elif average >= 3.5:
                total_grade = 'B+'
            elif average >= 3.0:
                total_grade = 'B'
            elif average >= 2.5:
                total_grade = 'C+'
            elif average >= 2.0:
                total_grade = 'C'
            else:
                total_grade = 'F'

            print('학점은 {}점이며, {}입니다.'.format(average, total_grade))

