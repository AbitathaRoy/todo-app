import functions

prompt = "You can add, show, edit, complete or exit : ";

while True :
    user_action = input(prompt);
    user_action = user_action.strip();

    if user_action.startswith("add") or user_action.startswith("new") :
        todo = user_action[4:];

        todos = functions.get_todos();   # create a list of existing items in the file

        todos.append(todo + "\n");

        functions.write_todos(todos);

    elif user_action.startswith("show") :
        todos = functions.get_todos();

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos) :
            item = item.title();
            print((index+1), "-", item, end = '');   # can remove trailing newline characters

    elif user_action.startswith("edit") :

        try :
            num = int(user_action[5:]);
            # print(num);
        except ValueError :
            print("Invalid input! Please enter the number of the todo you want to edit.");
            continue;

        todos = functions.get_todos();

        try :
            existing_todo = todos[num-1].title();
        except IndexError :
            print("There is no todo with that number!");
            continue;

        print(num, "-", existing_todo.strip('\n'));
        new_todo = input("Enter the new todo : ");
        todos[num-1] = new_todo + '\n';

        functions.write_todos(todos);

    elif user_action.startswith("complete") : # mark a todo as complete and remove it from the todo list

        try :
            num = int(user_action[9:]);
        except ValueError :
            print("Invalid input! Please enter the number of the todo you want to complete.");
            continue;

        todos = functions.get_todos();

        try :
            print(num, "-", "Task", todos.pop(num-1).strip('\n'), "complete");
        except IndexError :
            print("There is no todo with that number!");
            continue;

        functions.write_todos(todos);

    elif "exit" in user_action :
        print("Bye!");
        break;

    else :
        print("Unknown input");
