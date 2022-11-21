def control_pass(list,user,pas):
    list_new=[]
    for i in list:
        i=i.replace('\n','')
        list_new.append(i)
    for i in list_new:
        if i == user:
            index=list_new.index(user)
            if pas == list_new[index+1]:
                print('evrika')
            else:
                print("Invalid password.Please enter password.")
                return control_pass(list,user,pas)
            
    print(list_new)


def log_pass():
    user=input('Enter user: ')

    pas=input('Enter password: ')
    with open('users.txt','r+',encoding='utf-8') as us:
        file_line = us.readlines()
        some_list=[]
        for file in file_line:
            if file=='\n':
                continue
            else:
                some_list.append(file)

    print(some_list)
    control_pass(some_list,user,pas)






log_pass()

