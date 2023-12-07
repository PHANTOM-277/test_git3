import json
from pathlib import Path

file = Path('practice.json')

class Person:
    """a class to take information about a person"""
    def __init__(self):
        """don't do anything , just simply initialise object"""

    def set_base_info(self, name, age):
        """set base information"""
        self.name=name
        self.age = age
        self.info = {'name':name, 'age':age }

    def load_info(self, name):
        """load the dictionary saved with this person"""
        content_read = file.read_text()
        try:
            """load the json content and if the name is there in dictionary , load it and return True"""
            data = json.loads(content_read)
            data2 = data[name] #data 2 should likely hold the dictionary within 'name'
            self.info = data2
            self.name = self.info['name']
            self.age = self.info['age']
            return True
        except KeyError:
            """return false if this name does not exist"""
            return False
        except json.JSONDecodeError:
            """return false if there's nothing in file """
            return False
            

    def base_info(self):
        """display base information"""
        print(f"name : {self.name} \nage : {self.age}")

    def add_info(self, attribute, value):
        """add information"""
        self.info[attribute] = value
    
    def disp_all_info(self):
        """display all information"""
        list1 = self.info.keys()
        for x in list1:
            print(f"{x} : {self.info[x]}")

    def save_info(self):
        """save the contents in a json file"""
        try:
            content_read = file.read_text()
            data = json.loads(content_read)
            data[self.name] = self.info
            content_write = json.dumps(data, indent=2)
            file.write_text(content_write)

        except json.JSONDecodeError:
            dict = {}
            dict[self.name]= self.info
            content_write=json.dumps(dict, indent=2)
            file.write_text(content_write)

    def search_param(self, to_search):
        try:
            value = self.info[to_search]
            print(to_search,":",value)
        
        except KeyError:
            print(to_search," not a parameter for",self.name)

        
def delete_all():
    """delete the contents of practice.json completely"""
    nothing =''
    file.write_text(nothing)

def display_all_names():
    """display the names of all people whose information is stored"""
    content_read=file.read_text()
    try:
        data = json.loads(content_read)
        all_names = data.keys()
        print('Information on these people is available')
        for i in all_names:
            print(i)
    except json.JSONDecodeError:
        print("Nobody's information is available")

def take_first_input_menu():
    """function to take input for the first choice , i.e first menu choices"""
    print("Enter 1 to load a person's information ")
    print("Enter 2 to write data for a new person")
    print("Enter 3 to display the name's of all people whose information is available")
    print("Enter 4 to first delete everything in the storage file")
    a = int(input('Enter : '))
    return a

def first_menu_actions(a):
    if a==1:
        """makes a person and then loads the information using the name"""
        str1 = str(input('Enter the name : '))
        person = Person()
        a = person.load_info(str1) #takes a boolean value
        if a:
            """if person exists then only flag1 = True"""
            print('loaded',person.name)
            flag1 = True
            return person
        else:
            """if person does not exist"""
            print("This person's information does not exist")
            print("make sure the caps are correct and run the program again")
            return False

    elif a==2:
        """makes a new person"""
        str2 = str(input('Enter name : '))
        age = int(input('Enter age : '))
        person = Person()
        person.set_base_info(str2, age)
        print('initialised',person.name)
        flag1 = True
        return person
    
    elif a==3:
        """display all the names present """
        display_all_names()
    elif a==4:
        """delete all information stored"""
        delete_all()
    
    else:
        """invalid choice it is"""
        print('Invalid choice !')


def main():
    flag_menu = True
    flag1 = False #while loop will only take place if the object is created which happens if object is returned i.e a = 1 or 2
    while flag_menu:

        a = take_first_input_menu()#takes the input of first menu
        if a in [1,2]:#only if an object is initialised , then only we want the object back
            person = first_menu_actions(a)
            flag_menu= False #get out of while loop
            print(type(person))
            if person: #get out of while loop and make the next while loop run if an object is returned
                print('True')
                flag_menu = False
                flag1 = True
        else:
            """this happens if all names are displayed or storage file is cleaned or wrong input"""
            first_menu_actions(a)
            print("type 1 to get the same menu again , else enter anything")
            b = str(input('Enter : '))
            if int(b)==1:
                pass
            else:
                flag_menu = False #get out of this while loop
    
    
    if flag1:
        flag2 = True
        while flag2:
            """these are all the tasks availabe in a menu format"""
            print("Tasks available:")
            print("Enter 1 to display base information")
            print("Enter 2 to add information")
            print("Enter 3 to view all information")
            print("Enter 4 to save all information")
            print("Enter 5 to search a certain parameter")
            print("Enter 6 to exit")
            a = int(input('Enter choice : '))
            if a==1:
                person.base_info()

            elif a==2:
                info_name = str(input('Enter information type : '))
                data = str(input('Enter data : '))
                person.add_info(info_name, data)
            
            elif a==3:
                person.disp_all_info()
            
            elif a==4:
                person.save_info()
                print("saved information")

            elif a == 5:
                to_search = str(input('Enter the name of parameter to be searched : '))
                person.search_param(to_search)
            
            elif a==6:
                print('End of program')
                flag2 = False
            
            else:
                print('Invalid choice !')


main()
