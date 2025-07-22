import mysql.connector as myconn
from mysql.connector import Error
       
        
try:

    conn = myconn.connect(host='localhost',user='root',database='fardin',password='Fardin@2121',auth_plugin='mysql_native_password')
    cursor = conn.cursor()

    class ContactBook:

        def __init__(self, Store_name="", Phone_no="", Email="", Address=""):
            
            self.Store_name = Store_name
            self.Phone_no = Phone_no
            self.Email = Email
            self.Address = Address

        def addContact(self):
            
            query = 'insert into contact (Store_name, Phone_no, Email, Address) values (%s, %s, %s, %s)'
            values = (self.Store_name, self.Phone_no, self.Email, self.Address)
            cursor.execute(query,values)
            conn.commit()
            print("\n\nInsert Contact Successfully.\n")

        def viewContact(self):
        
            cursor.execute('select * from contact')
            rows = cursor.fetchall()
            print("\n--- Contact List ---")
            for row in rows:
                print(f"Store_name : {row[0]}, Phone_no : {row[1]}, Email : {row[2]}, Address : {row[3]}")

        def searchContact(self,phone_no):

            query = 'select * from contact where Phone_no = %s'
            cursor.execute(query, (phone_no,))   
            row = cursor.fetchone()
            if row:
                print(f"\nFound Contact:\nStore_name : {row[0]}, Phone_no : {row[1]}, Email : {row[2]}, Address : {row[3]}")
            else:
                print("\nNo contact found with that phone number.")
 

        def updateContact(self,phone_no):

            new_store_name = input("Enter new store name: ")
            query = 'update contact set Store_name = %s where Phone_no = %s'
            cursor.execute(query,(new_store_name,phone_no))
            conn.commit()
            print("\nContact updated successfully.\n")
  

        def deleteContact(self,Phone_no):
            
            query = 'delete from contact where Phone_no = %s'
            values = (self.Phone_no)
            cursor.execute(query, (phone_no,))
            conn.commit()
            print("\n\nDelete Contact Successfully.\n")    


    while True:   
        
        print("\n\nSelect Operation")
        print("Press 1 for Add Contact")
        print("Press 2 for View Contact")
        print("Press 3 for Search Contact")
        print("Press 4 for Update Contact")
        print("Press 5 for Delete Contact") 
        print("Press 6 for Exit") 

        try:
            choice = int(input("\nEnter your choice (1-6) : ")) 
        except ValueError as e:
            print("Error : ",e)
            

        if choice == 1:
            Store_name = input("Enter Store_name : ")
            Phone_no = input("Enter Phone_no : ")
            Email = input("Enter Email : ")
            Address = input("Enter Address : ")
            cb = ContactBook(Store_name,Phone_no,Email,Address)
            cb.addContact()   

        elif choice == 2:
            cb.viewContact()  

        elif choice == 3:
            phone_no = input("\nEnter Phone_no you want search : ")
            cb.searchContact(phone_no) 

        elif choice == 4:
                phone_no = input("\nEnter Phone_no you want update Store_name : ")
                cb.updateContact(phone_no)

        elif choice == 5:
            phone_no = input("\nEnter Phone_no you want delete : ")
            cb.deleteContact(phone_no) 

        elif choice == 6:
            print("Thanks for using the contact book.")
            break    

        else:
            print("Invalid choice! please select correct choice.")

except Error as e:
    print(f"Error: {e}")

finally:
    if conn and conn.is_connected():
        conn.close()
        print("Connection closed")