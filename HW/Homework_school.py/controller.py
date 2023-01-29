import view 

def start():
    while True:
        op = view.get_op()
        if op == 1:
            view.add_student()
        elif op == 2:
            view.add_lesson()
        elif op == 3:
            view.add_mark()
        elif op == 4:
            view.student_list()
        elif op == 5:
            view.mark_list()
        elif op == 6:
            view.print_main_dic()
        elif op == 7:
            break

        