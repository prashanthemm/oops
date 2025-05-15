class chatbook:

    __user_id = 10001

    def __init__(self):
        self.id = chatbook.__user_id
        chatbook.__user_id += 1
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.__name = "Default User"
        # self.menu()

    @staticmethod
    def get_id():
        return chatbook.__user_id
    
    @staticmethod
    def set_id(value):
        chatbook.__user_id = value


    def get_name(self):
        return self.__name
    
    def set_name(self, value):
        self.__name = value

    def menu(self):
        user_input = input("""Welcome to chat book?
                           1 to signup
                           2 to signin
                           3 to write a post
                           4 to messege
                           5 to exit\n""")
        
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.post()
        elif user_input == "4":
            self.send()
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
            self.menu()
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
                self.menu()
            else:
                print("Wrong password\n")
                self.menu()

    def post(self):
        if self.loggedin == True:
            text = input("What\'s on your mind today : ")
            print(f"Your post : {text}\n")
            self.menu()

        else:
            print("Signin first\n")
            self.menu()

    def send(self):
        if self.loggedin == True:
            frnd = input("Type your friend\'s name : ")
            msg = input("Type your message : ")
            print(f"Your message : {msg}\n has been sent to {frnd}\n")
            self.menu()

        else:
            print("Signin first\n")
            self.menu()



# user1 = chatbook()
