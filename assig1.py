def user_input():
    print("Please Choose Below Options...")
    print("1 for returning list of prime numbers")
    print("2 for Temperature Conversion")
    print("3 for CRUD operations on a file & 4 for Exit")
    option = input()
    try:
        # Below Code For Prime Numbers
        if option == '1':
            try:
                initial = int(input("Please Enter Starting Number: "))
                final = int(input("Please Enter the final range Number: "))
                print(f"Prime Number between {initial} & {final} are:")
                for number in range(initial, final):
                    if number > 1:
                        for num in range(2, number):
                            if (number % num) == 0:
                                break
                        else:
                            print(number, end=" ")
            except Exception as ex:
                print(f'You Got Exception which is :{ex}')
        # Below Code For Temperature Conversion
        elif option == '2':
            print("U've choosen temperature conversion")
            try:
                number = float(input("Please Enter Number to be converted: "))
                print("Please choose the following option: '1' for Celcius to Farrenhite and "
                      "'2' for Farrenhite to Celcius")
                opt = float(input())
                if opt == 1:
                    To_celcius = (5 / 9 * (number - 32))
                    print(f'Converted Temperature to Celcius is: {To_celcius}')
                elif opt == 2:
                    To_Farr = (9 / 5 * (number + 32))
                    print(f'Converted Temperature to Farrenhite is: {To_Farr}')
            except Exception as ex:
                print(f'You Got Exception which is :{ex}')
        # Below Code For CRUD Operations on a File.....
        elif option == '3':
            print("You have choosen option of CRUD for text file, which is below...")
            file = open("Customer.txt", 'w')
            file.write("Customer_ID, Customer_Name, Customer_Address, Customer_PinCode, Customer_Credit")
            display = file.read()
            print(display)
            print("Please Look Below Options...")
            print("1 For inserting a record")
            print("2 For displaying a file")
            print("3 For updating a record in file")
            print("4 For deleting a record from file.")
            opt = int(input())
            if opt == 1:
                #                 file = open("Customer.txt", 'w')
                #                 data = input("Please give the data\n")
                #                 file.write(data)
                file2 = open("Customer.txt", 'a')
                data = input("Enter the data which you wanna insert: ")
                file2.write("\n")
                file2.write(data)
                updated = open("Customer.txt", 'r')
                updated = updated.read()
                print(updated)
            elif opt == 2:
                print("Displaying the contents of file Below.")
                final = open("Customer.txt", 'r')
                print("-" * 10)
                final = final.read()

                print(final)
            elif opt == 3:
                #                 file2 = open("Customer.txt", 'a')
                #                 data = input("Enter the data which you wanna insert: ")
                #                 file2.write("\n")
                #                 file2.write(data)
                #                 updated = open("Customer.txt", 'r')
                #                 updated = updated.read()
                #                 print(updated)
                cid = input("Enter customer id to be updated with: ")
                file = open("Customer.txt", 'r+')
                sentence = file.readlines()
                for word in sentence:
                    if cid in word:
                        replaced_record = input("Enter Details You Wann Update: ")
                        result = word.replace(sentence, replaced_record)
                        break

            elif opt == 4:
                file = open("Customer.txt", 'r+')
                file.seek(0)
                file.truncate()
                print("Data been deleted from Customers.txt text file.")
        # Below Code For Exiting Function....
        elif option == '4':
            print("Exiting Bye!")
    except Exception as ex:
        print(f"Please choose from the options provided\n You got error which is: {ex}")