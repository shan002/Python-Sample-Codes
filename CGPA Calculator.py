gpas = {}
str = input("Number of theory courses: ")
credits_list = str.split()
# print(credits_list)
credits_theory = []
for item in credits_list:
    if '*' in item:
        c, mul = item.split('*')
        credits_theory += [float(c) for _ in range(int(mul))]
    else:
        credits_theory.append(float(item))
print(credits_theory)

str = input("Number of sessional courses: ")
credits_list = str.split()
# print(credits_list)
credits_lab = []
for item in credits_list:
    if '*' in item:
        c, mul = item.split('*')
        credits_lab += [float(c) for i in range(int(mul))]
    else:
        credits_lab.append(float(item))
print(credits_lab)

print("Theory Courses:")
print('-'*len("Theory Courses:"))
i = 1
for credit in credits_theory:
    print(f'{i}. Credit = {credit}')
    gpa = float(input('GPA: '))
    course_name = input('Course: ')
    if course_name == '':
        course_name = f'T{i}'
    gpas[course_name] = [credit, gpa]
    i += 1
    print('')


print("\n\nSessional Courses:")
print('-'*len("Sessional Courses:"))
i = 1
for credit in credits_lab:
    print(f'{i}. Credit = {credit}')
    gpa = float(input('GPA: '))
    course_name = input('Course: ')
    if course_name == '':
        course_name = f'L{i}'
    gpas[course_name] = [credit, gpa]
    i += 1
    print('')
print(gpas)


total_sum = 0
total_credit = 0
for course in gpas:
    total_sum += gpas[course][0] * gpas[course][1]
    total_credit += gpas[course][0]

print('-'*10)
print(f'\nTotal Credit: {total_credit}')
print('CGPA: ', total_sum/total_credit)

input()
