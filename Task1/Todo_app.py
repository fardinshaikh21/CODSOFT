import mysql.connector as myconn
from mysql.connector import Error


try:

    conn = myconn.connect(host='localhost',user='root',password='Fardin@2121',database='fardin',auth_plugin='mysql_native_password')
    cursor = conn.cursor()

    def addTask():
        
        title = input("Enter task title : ").capitalize()

        query = 'insert into tasks(Task) values(%s)'
        cursor.execute(query,(title,))
        conn.commit()
        print("\nTask added Successfully...\n")   
           

    def viewTask():
        
        cursor.execute('select Id,Task,Status from tasks')
        result = cursor.fetchall()
        print("\n--- Tasks List ---\n")

        if result:
            for i in result:
                print(i)
        else:
            print("\nEmpty Task...")    
             

    def complateTask():
        
        try:

            id = int(input("Enter task id mark as complated : "))
            query = 'update tasks set Status = "Complated" where Id = %s'
            cursor.execute(query,(id,))
            conn.commit()
            print("\nStatus marked as Complated...")

        except ValueError:
            print("\nPlease enter a valid id")


    def updateTask():
       
        try:

            id = int(input("Enter task id to update task : "))
            change_title = input("Enter new task title : ").capitalize()

            query = 'update tasks set Task = %s where Id = %s'
            cursor.execute(query,(change_title,id))
            conn.commit()
            print("\nUpdate Task Successfully...")

        except ValueError:
            print("\nPlease enter a valid id")


    def deleteTask():
        try:
            
            id = int(input("Enter task id to delete task : "))

            query = 'delete from tasks where Id = %s'
            cursor.execute(query,(id,))
            conn.commit()
            print("\nDelete Task Successfully...")

        except ValueError:
            print("\nPlease enter a valid id")

    def complatedTask():

        cursor.execute("select Id,Task,Status from tasks where Status = 'Complated' ")     
        result = cursor.fetchall()

        if result:
            print("\n--- Complated Tasks are ---\n")
            for i in result:
                print(i)   
        else:
            print("\nNo Task Complated") 

    def pendingTask():

        cursor.execute("select Id,Task,Status from tasks where Status = 'Pending'")     
        result = cursor.fetchall()

        if result:
            print("\n--- Pending Tasks are ---\n")
            for i in result:
                print(i)   
        else:
            print("\nNo Task Pending")                 
   

    while True:

        try: 

            print("\n--- Welcome to Todo App ---")
            print("\nPress 1 for Add Task")
            print("Press 2 for View Task")
            print("Press 3 for Mark Complate Task")
            print("Press 4 for Update Task")
            print("Press 5 for Delete Task")
            print("Press 6 for View All Complated Task")
            print("Press 7 for View All Pending Task")
            print("Press 8 for Exit")

            choice = int(input("Enter Your Choice (1-8) : "))

            if choice == 1:
                addTask()
            elif choice == 2:
                viewTask()
            elif choice == 3:
                complateTask()
            elif choice == 4:
                updateTask()
            elif choice == 5:
                deleteTask()
            elif choice == 6:
                complatedTask()
            elif choice == 7:
                pendingTask()
            elif choice == 8:
                print("\nThanks for using Todo App")
                break
            else :
                print("\nPlease enter valid choice")

        except ValueError:
            print("\nPlease enter a number")


except Error as e:

    print("\nError : ",e)

finally:

    if conn.is_connected:
        print("Connection closed...")
        conn.close()
            