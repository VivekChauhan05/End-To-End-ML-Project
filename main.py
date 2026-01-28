class Twitter_Chatbot:

    __user_id = 0

    def __init__(self):
        self.id = Twitter_Chatbot.__user_id
        Twitter_Chatbot.__user_id += 1
        self.__name = "Vivek"
        self.username = ""
        self.password = ""
        self.loggedin = False
        # self.menu()


    @staticmethod
    def get_id():
        return Twitter_Chatbot.__user_id
    
    @staticmethod
    def set_id(val):
        Twitter_Chatbot.__user_id = val

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def menu(self):
        user_input = input("""Welcome to Twitter! How would you like to proceed?
                           1. Press 1 to signup
                           2. Press 2 to signin
                           3. Press 3 to write a post
                           4. Press 4 to write a message to a friend
                           5. Press any other key to exit
                           """)
        
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.write_blog_post()
        elif user_input == "4":
            self.send_msg()
        else :
            exit()
            

    def signup(self):
        email = input("Enter the email here -> ")
        password = input("Enter the password here -> ")
        self.username = email
        self.password = password
        print("You have signed up successfully !!")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == ""  and self.password == "":
            print("Please sign up first by pressing 1 in the main menu")
        else:    
            email = input("Enter the email here -> ")
            password = input("Enter the password here -> ")
            if self.username == email and self.password == password:
               print("You have signed in successfully !!")
               self.loggedin = True
            else:
                print("Please enter the correct credentials")    

        print("\n")
        self.menu()        

    def write_blog_post(self):
        if self.loggedin == True:
            text = input("Enter your message here: ")
            print(f"Following content has been posted -> {text}")
        else:
            print("You need to signin first to post something")      

        print("\n")
        self.menu()    

    def send_msg(self):
        if self.loggedin == True:
            txt = input("Enter your text here -> ")
            frnd = input("Which friend do you want to send this message -> ")
            print(f"Your message has been sent to {frnd}")
        else:
            print("You need to signin first to send a message to your friend ")    
        print("\n")
        self.menu()

# obj = Twitter_Chatbot()          



    



