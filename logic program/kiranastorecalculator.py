sum = 0
while True:
    UserInput = input("Enter product price or press q for quite:\n")
    if(UserInput!='q'):
        try:
            sum = sum + int(UserInput)
            print(f"order total so far {sum}")
        except ValueError:
            print("Enter Valid Price")

    else:
        print(f"Thank you for shopping {sum}")
        break

