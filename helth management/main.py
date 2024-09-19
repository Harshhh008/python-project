try:
    while 1:
        def gettime():
            import datetime
            return datetime.datetime.now()

        def take(k):
            if k == 1:
                c = int(input("Enter 1 for Exrcise and 2 for food: "))
                if(c==1):
                    value = input("type here: ")
                    with open("Harsh_exersize.txt","a") as op:
                        op.write(str([str(gettime())])+" : "+value+"\n")
                    print("successfullly writern.\n")
                        
                elif(c==2):
                    value = input("type here: ")
                    with open("Harsh_food.txt","a") as op:
                        op.write(str([str(gettime())])+" : "+value+"\n")
                    print("successfully writern.\n")
                    
                
            elif k==2:
                c = int(input("Enter 1 for Exrcise and 2 for food: "))
                if(c==1):
                    value = input("type here: ")
                    with open("jimmy_exersize.txt","a") as op:
                        op.write(str([str(gettime())])+": "+value +"\n")
                    print("successfully writern.\n")
                    
                elif(c==2):
                    value = input("type here: ")
                    with open("jimmy_food.txt","a") as op:
                        op.write(str([str(gettime())])+ " : "+value+"\n")
                    print("wittern successfully.\n")
                    
            elif k==3:
                c = int(input("Enter 1 for Exrcise and 2 for food: "))
                if(c==1):
                    value = input("type here:")
                    with open("raju_exersize.txt","a") as op:
                        op.write(str([str(gettime())])+" : "+value+"\n")
                    print("writen Successfully.\n")   
                    
                if(c==2):
                    value = input("type here:")
                    with open("raju_food.txt","a") as op:
                        op.write(str([str(gettime())])+" : "+value+"\n")
                    print("writen Successfully.\n")   
            
            else:
                print("plz enter valid input (1-harsh),(2-jimmy),(3-raju) ")
                
        def retrive(k):
            if k==1:
                c = int(input("Enter 1 for Exrcise and 2 for food: "))
                if (c==1):
                    with open("Harsh_exersize.txt") as op:
                        for i in op:
                            print(i)
                        
                if (c==2):
                    with open("Harsh_food.txt") as op:
                        for i in op:
                            print(i)
                        
            elif k==2:
                c = int(input("Enter 1 for Exrcise and 2 for food: "))
                if (c==1):
                    with open("jimmy_exersize.txt") as op:
                        for i in op:
                            print(i)
                        
                if (c==2):
                    with open("jimmy_food.txt") as op:
                        for i in op:
                            print(i)
                        
            elif k==3:
                c = int(input("Enter 1 for Exrcise and 2 for food: "))
                if (c==1):
                    with open("raju_exersize.txt") as op:
                        for i in op:
                            print(i)
                        
                if (c==2):
                    with open("raju_food.txt") as op:
                        for i in op:
                            print(i)
                        
            else:
                print("Enter valid input harsh,jimmy,raju")
                
        print("Health Management System")
        a = int(input("press 1 for lock and 2 for retrive: "))
        if a==1:
            b = int(input("press 1 for harsh 2 for jimmy and 3 for raju : "))
            take(b)
            
        elif a==2:
            b = int(input("press 1 for harsh 2 for jimmy and 3 for raju : "))
            retrive(b)

        else:
            print("enter valid input")

            
except ValueError:
    print("please enter Numeric value")  
    
    
    
    