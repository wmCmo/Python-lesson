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

while True:
    user_action = input("Type add, show, edit, complete,  clean or exit:").strip()
    
    match user_action:
        case "add":
            todo = input("Enter a todo:").strip() + "\n"

            file = open("todos.txt", 'r')
            todo_list = file.readlines()
            file.close()

            todo_list.append(todo)

            file = open("todos.txt", 'w')
            file.writelines(todo_list)
            file.close()

        case "show" | "display":
            file = open("todos.txt","r")
            todo_list = file.readlines()
            file.close()

            if len(todo_list) == 0:
                print("No todos to show.")
            else:
                for i,item in enumerate(todo_list):
                    print(f"{i+1}-{item}")
        case "edit":
            for i,t in enumerate(todo_list,1):
                print(f"{i}-{t}")
            change_num = int(input("Choice a number to edit:")) -1
            if change_num < len(todo_list):
                new_todo = input("Enter a new todo:")
                todo_list[change_num] = new_todo
        case "clean":
            todo_list.clear()
        case "complete":
            while True:
                for i,t in enumerate(todo_list,start=1):
                    print(f"{i}-{t}")
                delete_num = input("Choise a number of remove:")
                del todo_list[int(delete_num)-1]
                order = input("Choise continue or end:")
                if order.lower() == "end":
                    break
        case "exit":
            break
        #_ = whatever value that is not matched with the above cases
        case _:
            print("hey, you entered an unknown command")
print("Bye!")


