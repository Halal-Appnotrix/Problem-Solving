#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    
    grades_array = []
    for grade in grades:
        the_next_multiple_of_5 = (((grade // 5)+1)*5)
        if grade < 38:
            grades_array.append(grade)
        elif (the_next_multiple_of_5 - grade) < 3:
            grades_array.append(the_next_multiple_of_5)
        else:
            grades_array.append(grade)
    
    return grades_array



if __name__ == '__main__':
    grades_count = int(input().strip())
    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print('\n'.join(map(str, result)))
 
