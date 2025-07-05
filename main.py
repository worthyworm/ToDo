import shutil
import os

def createToDo(name):
    with open(f'{name}.txt', 'a') as f:
        f.write(f"")

def is_file_empty(file_path):
    return os.path.getsize(file_path) == 0


def replace_first_char_in_line(name, line_number, new_first_char):
    try:
        with open(f'{name}.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()

        if line_number < 1 or line_number > len(lines):
            print(f"Ошибка: В файле только {len(lines)} строк")
            return False

        line = lines[line_number - 1]

        first_char_length = len(line[0]) if line else 0

        modified_line = new_first_char + line[first_char_length:]

        lines[line_number - 1] = modified_line

        with open(f'{name}.txt', 'w', encoding='utf-8') as file:
            file.writelines(lines)

        return True

    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
        return False


def modifyToDo(name, action):
    if action == "1":
        tname = input("Enter a content for a ToDo : ")
        with open(f'{name}.txt', 'a') as f:
                f.write(f"❌ - {tname}\n")
    if action == "2":
        with open(f'{name}.txt', 'r') as f:
            content = f.read()
            line_number = int(input("Select a line for editing : "))
            new_content = input("Enter a new content : ")
            replace_line(name, line_number, f'❌ - {new_content}')
    if action == "3":
        with open(f'{name}.txt', 'r') as f:
            content = f.read()
            lines = f.readlines()
            line_number = int(input("Select a line to complete : "))
            replace_first_char_in_line(name, line_number, "✅")


def replace_line(name, line_number, new_content):
    with open(f'{name}.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    if 1 <= line_number <= len(lines):
        lines[line_number - 1] = new_content + '\n'

        with open(f'{name}.txt', 'w', encoding='utf-8') as file:
            file.writelines(lines)
        return True
    else:
        print(f"Error: there is only {len(lines)} lines")
        return False


version = "1.0"
print("""
TTTTTTTTTTTTTTTTTTTTTTT              DDDDDDDDDDDDD
T:::::::::::::::::::::T              D::::::::::::DDD
T:::::::::::::::::::::T              D:::::::::::::::DD
T:::::TT:::::::TT:::::T              DDD:::::DDDDD:::::D
TTTTTT  T:::::T  TTTTTTooooooooooo     D:::::D    D:::::D    ooooooooooo
        T:::::T      oo:::::::::::oo   D:::::D     D:::::D oo:::::::::::oo
        T:::::T     o:::::::::::::::o  D:::::D     D:::::Do:::::::::::::::o
        T:::::T     o:::::ooooo:::::o  D:::::D     D:::::Do:::::ooooo:::::o
        T:::::T     o::::o     o::::o  D:::::D     D:::::Do::::o     o::::o
        T:::::T     o::::o     o::::o  D:::::D     D:::::Do::::o     o::::o
        T:::::T     o::::o     o::::o  D:::::D     D:::::Do::::o     o::::o
        T:::::T     o::::o     o::::o  D:::::D    D:::::D o::::o     o::::o
      TT:::::::TT   o:::::ooooo:::::oDDD:::::DDDDD:::::D  o:::::ooooo:::::o
      T:::::::::T   o:::::::::::::::oD:::::::::::::::DD   o:::::::::::::::o
      T:::::::::T    oo:::::::::::oo D::::::::::::DDD      oo:::::::::::oo
      TTTTTTTTTTT      ooooooooooo   DDDDDDDDDDDDD           ooooooooooo\n""", version)
print(f"https://github.com/worthyworm/ToDo")
while True:
    c = input("Select an action:\n1 - Create a ToDo list\n2 - Open/modify an existing ToDo list\n3 - Exit\n")
    if c == "1":
        name = input("Enter a name for the list: ")
        createToDo(name)
        action = input("Select an action:\n1 - Create a ToDo\n2 - Modify ToDo\n3 - Delete ToDo list\n4 - Exit")
        modifyToDo(name, action)
    if c == "2":
        name = input("Enter a name of the list that you will be modyfing : ")
        with open(f'{name}.txt', 'r') as f:
            content = f.read()
        print(content)
        action = input("Select an action:\n1 - Create a ToDo\n2 - Modify ToDo\n3 - Complete a ToDo \n4 - Delete a ToDo list\n 5 - Exit")
        modifyToDo(name, action)



