def get_op():
    op = int(input(
        '1 - Добавить студента \n2 - Добавить предмет \n3 - Добавить оценку ученику по предмету \n4 - Показать список учеников \n'
        '5 - Показать лист оценок ученика \n6 - Показать журнал \n7 - Выход \n'))
    return op

student_dic = {}
students = []
lessons = []
def add_student():
    name = input('Введите Имя Фамилию: ')
    students.append(name)
    student_dic[name] = {}
    if lessons:
        for name_less in lessons:
            student_dic[name][name_less] = []

def add_lesson():
    name_less = input('Введите название предмета: ')
    lessons.append(name_less)
    for name in student_dic:
        student_dic[name][name_less] = []

def add_mark():
    stud = input('Введите имя ученика: ')
    lesson = input('Введите название предмета: ')
    mark = input('Введите оценку: ')
    student_dic[stud][lesson].append(mark)

def student_list():
    for name in student_dic:
        print({name})

def mark_list():
    stud_name = input('Введите имя ученика: ')
    print(student_dic[stud_name])
    
def print_main_dic():
    print(student_dic)