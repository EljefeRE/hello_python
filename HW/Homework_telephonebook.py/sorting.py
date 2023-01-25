def sort_names():
    with open('user_list.txt', 'r') as file:
        lst = file.readlines()
        lst_with_lst = []
        for line in lst:
            a = line.strip().split(',')
            lst_with_lst.append(a)

        lst_with_lst = sorted(lst_with_lst,key = lambda x: x[1])
        string_ = ''
        for user in lst_with_lst:
            res = ','.join(user)
            string_ += res + '\n'
    with open('user_list.txt', 'w') as file:
        file.write(string_)

def sort_id():
    with open('user_list.txt', 'r') as file:
        lst = file.readlines()
        lst_with_lst = []
        for line in lst:
            a = line.strip().split(',')
            lst_with_lst.append(a)


        lst_with_lst = sorted(lst_with_lst,key = lambda x: x[0])
        string_ = ''
        for user in lst_with_lst:
            res = ','.join(user)
            string_ += res + '\n'
    with open('user_list.txt', 'w') as file:
        file.write(string_)