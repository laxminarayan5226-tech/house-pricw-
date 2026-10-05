from testt import create ,connect,table,insert,delete,update ,view


while True:

    print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
    print("1. CREATE DATABASE")
    print("2. CREATE TABLE")
    print("3. INSERT DATA")
    print("4. VIEW DATA")
    print("5. UPDATE DATA")
    print("6. DELETE DATA")
    print("7. EXIT")

    choice = input("ENTER YOUR CHOICE : ").strip()

    if choice == "1":
        create()

    elif choice == "2":
        table()

    elif choice == "3":
        insert()

    elif choice == "4":
        view()

    elif choice == "5":
        update()

    elif choice == "6":
        delete()

    elif choice == "7":
        print("THANK YOU")
        break

    else:
        print("INVALID CHOICE")
