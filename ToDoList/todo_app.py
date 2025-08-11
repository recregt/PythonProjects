to_do_list = []

while True:
    
    print("Options:\n1.Add Task:\n2.Remove Tasks:\n3.View Tasks:\n4.Exit\n")
    
    choice = input("Enter your choice: ")
    
    
    if choice == '1':
        task = input("Enter task name: ")
        to_do_list.append(task)
        print(f"\nTask '{task}' added to the list.\n")
        
    elif choice == '2':
        if not to_do_list:
            print("\nThe list is empty. Nothing to remove.\n")
        else:
            print("\nTo-Do List:")
            for index, task in enumerate(to_do_list):
                print(f"{index + 1}. {task}")
            
            try:
                task_number = int(input("Enter the number of the task to remove: "))
                if 1 <= task_number <= len(to_do_list):
                    removed_task = to_do_list.pop(task_number - 1)
                    print(f"Task '{removed_task}' has been removed.\n")
                else:
                    print("\nInvalid task number.\n")
            except ValueError:
                print("\nInvalid input. Please enter a number.\n")
        
    elif choice == '3':
        if not to_do_list:
            print("\nThe list is empty.\n")
        else:
            print("\nTo-Do List:")
            for index, task in enumerate(to_do_list):
                print(f"{index + 1}. {task}")
                
    elif choice == '4':
        print("\nExiting the application.")
        break
    
    else:
        print("\nInvalid choice. Please enter a number from 1 to 4.\n")