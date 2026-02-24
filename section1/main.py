# user_prompt = "Enter a todo:"
# todo1 = input(user_prompt)
# todo2 = input(user_prompt)
# todo3 = input(user_prompt)

# todos = [todo1, todo2, todo3]

# print(*todos)
# print(type(user_prompt))
# print(type(todos))

# user_prompt = "Enter a todo:"

# todo_list = []

# def check_todo(todos):
#             for i,t in enumerate(todos,start=1):
#                 print(f"todo{i}: {t}")
#                 # print(f"{t} index is {i-1}")
# while True:
#     todo = input(user_prompt)
#     if todo == "quit":
#         check_todo(todo_list)
#         break
#     todo_list.append(todo)
    # print("todo has cleaned")
    # print(todo_list)

    # if len(todo_list) == 3:
    #     check_todo(todo_list)
    #     break
    
#dir(str)    
    
    

todo_list = []

def show_list(todos):
    if len(todos) == 0:
        print("No todos to show.")
    else:
        for i,item in enumerate(todos):
            item = item.strip('\n')
            print(f"{i+1}-{item}")

while True:
    #Get user input and strip space chars from it
    user_action = input("Type add, show, edit, complete, clean or exit:").strip()
    
    if "add" in user_action:
        todo = user_action[4:] + "\n"
        

        # file = open("todos.txt", 'r')
        # todo_list = file.readlines()
        # file.close()

        with open("todos.txt", 'r') as file:
            todo_list = file.readlines()

        todo_list.append(todo)

        with open("todos.txt", 'w') as file:
            file.writelines(todo_list)      

    elif "show" in user_action or "display" in user_action:
        with open("todos.txt", 'r') as file:
            todo_list = file.readlines()
        show_list(todo_list)
    elif "edit" in user_action:
        with open("todos.txt", 'r') as file:
            todo_list = file.readlines()
        show_list(todo_list)

        change_num = int(input("Choice a number to edit:")) -1

        if change_num < len(todo_list):
            new_todo = input("Enter a new todo:")
            todo_list[change_num] = new_todo + '\n'

        with open('todos.txt','w') as file:
            file.writelines(todo_list)
        show_list(todo_list)
    elif "clean" in user_action:
        todo_list.clear()
        with open('todos.txt','w') as file:
            file.writelines(todo_list)
    elif "complete" in user_action or "c" in user_action:
        with open("todos.txt", 'r') as file:
            todo_list = file.readlines()
        
        while True:
            show_list(todo_list)
            
            delete_num = int(input("Choose a number to remove:"))
            
            if delete_num <= len(todo_list) and int(delete_num) > 0:
                removed_todo = todo_list[delete_num - 1].strip('\n')
                print(f"{removed_todo} was removed from the list.")
                todo_list.pop(delete_num - 1)
                with open('todos.txt', 'w') as file:
                    file.writelines(todo_list)
            else:
                print("Invalid number!")
                continue
            
            order = input("Choose continue or end:")
            if order.lower() == "end":
                break
    elif "exit" in user_action:
        break
    #_ = whatever value that is not matched with the above cases
    else:
        print("hey, you entered an unknown command")
print("Bye!")


