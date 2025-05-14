class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()


    def menu(self):
        user_input = input("""Welcome to chat book?
                           1 to signup
                           2 to signup
                           3 to write a post
                           4 to messege
                           5 to exit\n""")
        
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()

    def signup(self):
        email = input("Enter you email here : ")
        pw = input("Set your password : ")
        self.username = email
        self.password = pw
        print("Successful signup done\n")
        self.menu()

    def signin(self):
        if self.username=='' and self.password=='':
            print("Signup first")
        else:
            uname = input("Enter your username : ")
            if(uname==self.username) :
                pass
            else: 
                print("Wrong Username\n")
                self.menu()
            upw = input("Enter your password : ")
            if(upw==self.password):
                print("Signed in successfully")
                self.loggedin = True
            else:
                print("Wrong password\n")
                self.menu()



obj = chatbook()
