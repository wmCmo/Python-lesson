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
    user_action = input("Type add, show, edit, clean or exit:").strip()
    
    match user_action:
        case "add":
            todo = input("Enter a todo:").strip()
            todo_list.append(todo)
        case "show" | "display":
            if len(todo_list) == 0:
                print("No todos to show.")
            else:
                for item in todo_list:
                    print(item)
                print()
        case "edit":
            for i,t in enumerate(todo_list,1):
                print(i,'-',t)
            change_num = int(input("Choice a number to edit:")) -1
            if change_num < len(todo_list):
                new_todo = input("Enter a new todo:")
                todo_list[change_num] = new_todo
        case "clean":
            todo_list.clear()
        case "exit":
            break
        #_ = whatever value that is not matched with the above cases
        case _:
            print("hey, you entered an unknown command")
print("Bye!")


