def task():
    tasks = []
    print("-----TO DO LIST-----")
    
    total_task = int(input("enter how many task u want: "))
    for i in range(1,total_task+1):
        task_name = input(f"Enter task {i} = ") #enter task 1,2,3
        tasks.append(task_name)
        
    for task in tasks:
        print(f"Today's task is : {task}")     
               
    while 1:
        print("1.ADD\n2.UPDATE\n3.DELETE\n4.VIEW\n5.EXIT")
        choice = int(input("Enter ur choice: "))
        
        if choice == 1:
            add = input("Enter task you want to add: ")
            tasks.append(add)
            print("your task successfully added..")
           
        elif choice == 2:
            update = input("Enter the task name for update: ")
            if update in tasks:
                updated = input("Ënter new task: ")
                indx = tasks.index(update)
                tasks[indx] = updated
                print(f"{updated} has been successfully updated.")
                
        elif choice == 3:
            #delete task
            delete =input("Enter the task name for delete: ")
            if delete in tasks:
                indx = tasks.index(delete)
                del tasks[indx]
                print(f"{delete} has been successfully deleted.")
            
        elif choice == 4:
            for task in tasks:
                print(f"Today's task is : {task}")
                
        elif choice == 5:
            exit()
            print("app has been closed.")
            
        else:
            print(f"invalid choice: {choice}")
            
if __name__ == "__main__":
        task()    
        
        