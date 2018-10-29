import os.path
def spaces(number_of, symbol):
    for i in range(number_of):
        print(symbol, end='')
def menu():
    spaces(20,'=')
    print("""
= 1. Make folder   =
= 2. Delete folder =
= 3. Make file     =
= 4. Delete file   =
= 5. Change dir    =
""", end='')
    spaces(20, '=')
    print()
    print('Current dirrectory is %s' % os.getcwd(), end='')
    print()
def create_dir(path, name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('File already exist')
def delete_dir(path, name):
    os.rmdir(path)
    #FROM HERE!!!
menu()
try:
    usr_choice = int(input('Choose one: '))
    while (usr_choice > 5):
        usr_choice = int(input('Choose one: '))
        if (usr_choice > 5):
            print('Enter number from 0-5!')

except (ValueError, TypeError)  as e:
    f = open('ErrorLog.txt', 'a')
    f.write(str(e))
    f.write('\n')
    f.close()
    print('Error!')

if (usr_choice == 1):
    try:
        usr_path = str(input('Enter path for directory: '))
        os.chdir(usr_path)
        usr_dir_name = str(input('Enter name for directory: '))
        if(usr_dir_name == ''):
            usr_dir_name = 'Empty'
        if(usr_path == ''):
            os.chdir(usr_path)
            usr_path = os.getcwd()
        create_dir(usr_path, usr_dir_name)
    except (FileExistsError, FileNotFoundError, WindowsError, OSError) as e:
        f = open('ErrorLog.txt', 'a')
        f.write(str(e))
        f.write('\n')
        f.close()
        print('Error!')
elif (usr_choice == 2):
    #foldef del
    pass
elif (usr_choice == 3):
    #file make
    pass
elif (usr_choice == 4):
    #file del
    pass
elif (usr_choice == 5):
    #change dir
    pass