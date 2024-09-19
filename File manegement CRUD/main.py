import os

def create_file(filename):
    try:
        with open(filename,'x') as cf:
             print(f"file name {filename} created successfully")
             
    except FileExistsError:
        print(f"file name {filename} already exist")
        
    except Exception as E:
        print("somthing went wrong.")
        
def list_all_file():
    files = os.listdir()
    if not files:
        print("file does not exixt") 
    else:
        for file in files:
            print(file)   
    
def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} file deleted successfully.")
        
    except FileNotFoundError:
        print(f"{filename} not found")
        
    except Exception as e:
        print("something went wrong")
        
def read_file(filename):
    try:
        with open(filename,'r') as f:
            contant = f.read()
            print(f"conntant of '{filename}' : '{contant}'")
            
    except FileNotFoundError:
        print("file not found")
        
    except Exception as E:
        print("something went wrong.")
        
def edit_file(filename):
    try:
        with open (filename,'a') as f:
            contant = input("enter data what u want:")
            f.write(contant + "\n")
            print(f"contant added in '{filename}' : '{contant}'")
            
    except FileNotFoundError:
        print("file not found")
        
    except Exception as E:
        print("something went wrong.")
        
       
def main():
    while 1:
        print("FILE MANAGEMENT APP:")
        print("1.create file")
        print("2.list all files")
        print("3.delete file")
        print("4.read file")
        print("5.edit file")
        print("6.Exit app")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            filename = input("Enter file name to create: ")
            create_file(filename)
        elif choice == '2':
            list_all_file()
        elif choice == '3':
            filename = input("Enter file name to delete file: ")
            delete_file(filename)
        elif choice == '4':
            filename = input("Enter file name to read: ")
            read_file(filename)
        elif choice == '5':
            filename = input("Enter file name to Edit file: ")
            edit_file(filename)
        elif choice == '6':
            print("closing the app")
            exit()
        else:
            print("invalid choice:",choice)
                               
if __name__ == "__main__":
    main()
               
             