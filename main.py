import os


def create():
    name = input("Enter a name for the list: ")
    createToDo(name)
    action = input("Select an action:\n1 - Create a ToDo\n2 - Modify ToDo\n3 - Delete ToDo list\n4 - Exit")
    modifyToDo(name, action)


def modify(name):
    if name != '':
        pass
    else:
        name = input("Enter a name of the list that you will be modyfing : ")
    with open(f'{name}.txt', 'r') as f:
        content = f.read()
    print(content)
    action = input(
        "Select an action:\n1 - Create a ToDo\n2 - Modify ToDo\n3 - Complete a ToDo \n4 - Delete a ToDo\n5 - Exit\n")
    modifyToDo(name, action)
    modify(name)


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
            print(f"Error: There is only {len(lines)} lines")
            return False

        line = lines[line_number - 1]

        first_char_length = len(line[0]) if line else 0

        modified_line = new_first_char + line[first_char_length:]

        lines[line_number - 1] = modified_line

        with open(f'{name}.txt', 'w', encoding='utf-8') as file:
            file.writelines(lines)

        return True

    except Exception as e:
        print(f"Error: {str(e)}")
        return False


def modifyToDo(name, action):
    if action == "1":
        content = input("Enter a content for a ToDo : ")
        with open(f'{name}.txt', 'a') as f:
                f.write(f"❌ - {content}\n")
    if action == "2":
        with open(f'{name}.txt', 'r') as f:
            line_number = int(input("Select a line for editing : "))
            new_content = input("Enter a new content : ")
            replace_line(name, line_number, f'❌ - {new_content}')
    if action == "3":
        with open(f'{name}.txt', 'r') as f:
            line_number = int(input("Select a line to complete : "))
            replace_first_char_in_line(name, line_number, "✅")
    if action == "4":
        with open(f'{name}.txt', 'r') as f:
            lines = f.readlines()
            line_number = int(input("Select a line to delete : "))
        lines.pop(line_number - 1)
        with open(f'{name}.txt', 'w') as f:
            f.writelines(lines)
    if action == "5":
        exit()
    else:
        return


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


def menu():
    action = input("Select an action:\n1 - Create a ToDo list\n2 - Open/modify an existing ToDo list\n3 - Exit\n")
    if action == "1":
        create()
    if action == "2":
        modify(name='')
    if action == "3":
        exit()
    else:
        return

version = "1.0"

print(f"""
████████╗ ██████╗ ██████╗  ██████╗ 
╚══██╔══╝██╔═══██╗██╔══██╗██╔═══██╗
   ██║   ██║   ██║██║  ██║██║   ██║
   ██║   ██║   ██║██║  ██║██║   ██║
   ██║   ╚██████╔╝██████╔╝╚██████╔╝
   ╚═╝    ╚═════╝ ╚═════╝  ╚═════╝ 
                                   \n""", version)
print(f"https://github.com/worthyworm/ToDo")

while True:
    menu()
