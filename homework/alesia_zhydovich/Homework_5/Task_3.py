students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

students_str = ', '.join(students)
subjects_str = ', '.join(subjects)

text_for_print = f'Students {students_str} study these subjects: {subjects_str}'

print(text_for_print)
