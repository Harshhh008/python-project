import datetime
try:
    while 1:
        def gettime():
            return datetime.datetime.now()


        def getdata(n):
            if n==1:
                c = int(input("Enter 1 for food ,2 for exersize:"))
                if c ==1:
                    value = input("type here: ")
                    with open("harsh_food.txt","a") as op:
                        op.write(str(gettime())+" "+value+"\n")
                        print("written successfully.")
                        
                if c==2:
                    value = input("type here:")
                    with open("harsh_exersize.txt","a")as op:
                        op.write(str(gettime())+" "+value+"\n")
                        print("written successfully.")
                        
            elif n==2:
                c = int(input("Enter 1 for food ,2 for exersize:"))
                if c ==1:
                    value = input("type here: ")
                    with open("aman_food.txt","a") as op:
                        op.write(str(gettime())+" "+value+"\n")
                        print("written successfully.")
                        
                if c==2:
                    value = input("type here:")
                    with open("aman_exersize.txt","a")as op:
                        op.write(str(gettime())+" "+value+"\n")
                        print("written successfully.")
                        
            elif n==3:
                c = int(input("Enter 1 for food ,2 for exersize:"))
                if c ==1:
                    value = input("type here: ")
                    with open("bhavesh_food.txt","a") as op:
                        op.write(str(gettime())+" "+value+"\n")
                        print("written successfully.")
                        
                if c==2:
                    value = input("type here:")
                    with open("bhavesh_exersize.txt","a")as op:
                        op.write(str(gettime())+" "+value+"\n")
                        print("written successfully.")
                        
            else:
                print("invalid input.please select(1-harsh),(2-aman)(2-bhavesh)")
                        
        def retrive(n):
            if n==1:
                c = int(input("enter 1 for food 2 for exersize: "))
                if c==1:
                    with open("harsh_food.txt") as op:
                        for i in op:
                            print(i)
                            
                if c==2:
                    with open("harsh_exersize.txt") as op:
                        for i in op:
                            print(i)
                            
            elif n==2:
                c = int(input("enter 1 for food 2 for exersize: "))
                if c==1:
                    with open("aman_food.txt") as op:
                        for i in op:
                            print(i)
                            
                if c==2:
                    with open("aman_exersize.txt") as op:
                        for i in op:
                            print(i)
                            
            elif n==3:
                c = int(input("enter 1 for food 2 for exersize: "))
                if c==1:
                    with open("bhavesh_food.txt") as op:
                        for i in op:
                            print(i)
                            
                if c==2:
                    with open("bhavesh_exersize.txt") as op:
                        for i in op:
                            print(i)
            else:
                print("invalid input.please select(1-harsh),(2-aman)(2-bhavesh)")
                    
        print("\tHealth Management System:")

        data = int(input("Enter 1 for get data 2 for retrive data: "))
        if data==1:
            a = int(input("Enter 1 for harsh,2 for aman ,3 for bhavesh: "))
            getdata(a)
            
        elif data==2:
            a = int(input("Enter 1 for harsh,2 for aman ,3 for bhavesh: "))
            retrive(a)
            
        else:
            print("invalid input.")
            
except Exception as e:
    print(e)
               