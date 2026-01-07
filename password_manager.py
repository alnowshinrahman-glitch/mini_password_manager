import json 
    

def load_data():
#function:
#1. open the file n read whats inside 
#2: read what is inside
#3. convert it into something py understands n give it back to the program 

 file = open("data.json")
 passwords = json.load(file) 
 file.close()
 return passwords 

#save updated passwords 
def save_data(passwords):
 with open("data.json", "w") as file: # the w allows to read in writer mode 
  json.dump(passwords, file) # converts the dictionary into json n writes it to the file 

def add_password(passwords):
 website = input("Website: ")
 username = input("Username: ")
 password = input("Password: ")
 #adds the new entry or updates existing one
 passwords[website] ={"username": username, "password": password}
 #writes the current state of dictionary into json file
 save_data(passwords) 
 print(f"Password for {website} saved successfully!")

def view_password(passwords):
 choosen_website = input("Please enter the website you want to check: ")
 if choosen_website in passwords:
  username= passwords[choosen_website]["username"]
  password=passwords[choosen_website]["password"]

  print("Username:", username)
  print("password:", password)
 else:
  print("Website not found!") 



  

 