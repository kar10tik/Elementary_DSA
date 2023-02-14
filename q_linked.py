print("Welcome to the Linked List Program!")
arr=Linked_List()
ch='y'
while (ch=='y' or ch=='Y'):
    print("Choices")
    print("1. Insert a node at the beginning")
    print("2. Insert a node at the nth position")
    print("3. Insert a node at the end")
    print("4. Delete the node at the beginning")
    print("5. Delete the node at the nth position")
    print("6. Delete the node at the end")
    print("7. Search for a node")
    print("8. Display the linked list")
    print("9. Reverse the linked list")
    print("10. Exit")
    choice=int(input("Enter your choice"))
    if (choice==1):
        data=int(input("Enter the value to insert"))
        arr.insert_node_b(data)
    if (choice==2):
        data=int(input("Enter the value to insert"))
        arr.insert_node_m(data)
    if (choice==3):
        data=int(input("Enter the value to insert"))
        arr.insert_node_e(data)
    if (choice==4):
        arr.delete_node_b()
    if (choice==5):
        data=int(input("Enter the value to delete"))
        arr.delete_node_m(data)
    if (choice==6):
        arr.delete_node_e()
    if (choice==7):
        data=int(input("Enter the node to search for"))
        arr.search(data)
    if (choice==8):
        arr.display()
    if (choice==9):
        arr.revlist()
    if (choice==10):
        break
    if choice not in [i for i in range(11)]:
        print("Invalid Choice!")
    ch=input("Do you want to perform another operation?")