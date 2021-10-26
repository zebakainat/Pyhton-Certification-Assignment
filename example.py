from Super import Super
from User import User

user={}
admin={}


def login(user_or_admin):

    if user_or_admin=='1':
        username=input("Enter username: ")
        password=input("Enter password: ")
        if username in user:
            if user[username]==password:
                print("\nEnter your name to take the quiz:")
                ob1 =User(1,input())
                while True:
                	print("\n1.Take Quiz","\n2.Logout")
                	menu = int(input())
                	if(menu==1):
                		ob1.takeupquiz()
                		ob1.result()
                	else:
                		print("Logged Out")
                		break

            else:
                print("\n Invaild Credentials!")
        else:
            print("\n Invaild Credentials!")

    elif user_or_admin=='2':
        username=input("\n Enter username: ")
        password=input("Enter password: ")
        if username in admin:
            if admin[username]==password:
                print("*******Logged In********")
                print("Enter admin name:")
                ob = Super('s1',input())
                while True:
                	print("\n1.Create Quiz","\n2.Edit Quiz","\n3.View Quiz","\n4.Delete Quiz","\n5.Create Topic","\n6.View Topic","\n7.Edit Topic","\n8.Delete Topic","\n9.Logout\n")
	               	menu = int(input())
	               	if(menu==1):
	               		ob.add_question()
	               	elif(menu==2):
	               		ob.edit_question()
	               	elif(menu==3):
	               		ob.view_questions()
	               	elif(menu==4):
	               		ob.delete_questions()
	               	elif(menu==5):
	               		ob.create_topic()
	               	elif(menu==6):
	               		ob.view_topic()
	               	elif(menu==7):
	               		ob.edit_topic()
	               	elif(menu==8):
	               		ob.delete_topic()
	               	else:
	               		print("\nLogged Out\n ")
	               		register()
	               		break


            else:
                print("\n Invaild Credentials!!")
                login(input("Press 1 for login as user and 2 for login as admin: "))
        else:
            print("\n Invaild Credentials!!!")
            login(input("Press 1 for login as user and 2 for login as admin: "))
            
            
def register():       
    user_or_admin=input("Press 1 for register as user and 2 for register as admin: ")
    if user_or_admin=='1':
        username=input("\n Enter username: ")
        password=input("Enter password: ")
        user[username]=password
        login(input("Press 1 for login as user and 2 for login as admin: "))
    elif user_or_admin=='2':
        username=input("\n Enter username: ")
        password=input("Enter password: ")
        admin[username]=password
        login(input("Press 1 for login as user and 2 for login as admin: "))     

choice = {1:'press 1 for login',2:'press 2 for register: '}
for value in choice:
    print('\n ',str(value)+'.',choice[value])
choice_input=int(input())
if choice_input==1:
    login(input("Press 1 for login as user and 2 for login as admin: "))
elif choice_input==2:
    register()



