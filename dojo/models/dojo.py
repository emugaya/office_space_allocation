# from myapp.dojo.models.person import Person, Staff, Fellow
# from myapp.dojo.models.room import Office, LivingSpace
# from myapp.dojo.database.database import *
import os

from dojo.models.person import Person, Staff, Fellow
from dojo.models.room import Office, LivingSpace
from dojo.database.database import *

import random
import pickle

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Dojo(object):
    """
    Dojo is an Object that is used to Automatically allocate rooms to staff and fellows in the Dojo.
    It has funtions create_room, add_person,
    """
    def __init__(self):
        self.living_space = {} # Dictionary used to store LivingSpace rooms. Room name is key and room object is value
        self.office = {} # Dictionary used to store Office rooms. Room name is key and room object is value
        self.persons ={} # Dictionary used to store Person objects. person_id is key and person object(staff or fellow) is value
        self.room_types = ['office','livingspace'] #Initialize Room types
        self.person_types =['STAFF', 'FELLOW'] # Initialize person types
        self.fellows_with_living_room_list =[] # List used to store person_id of fellow already allocated offices
        self.fellows_with_office_list = [] # List used to store person_id of fellow who was not allocated office automatically
        self.fellows_who_missed_living_space = [] # List used to store person_id of fellow who was not allocated living_space automatically and yet they wante living space
        self.fellows_who_dont_want_living_space = []#List of fellows who don't want living space
        self.fellows_who_missed_office = [] #List of fellows who missed office space
        self.staff_with_office_list =[]#List of staff who have been allocated office space successfully
        self.staff_who_missed_office_list = []#List of staff who missed office Space
        self.all_rooms_list =[] #List of all rooms in the dojo
        self.max_number_of_people_in_office = 6 # stores maximum number of people who can be in an office
        self.max_number_of_people_in_living_space = 4 # Stores maximu number of fellows who can be in a living space

    def create_room(self, room_type, *room_name):
        """"
        create_room is method used to create rooms in the dojo

        :params room_type: Room type can either be Living Space or Staff. Staff maximum
        :params *room_name: Room name accepts one or more rooms passed after defining the type of room being created.
        """
        rooms_list = list(room_name)[0]
        for room in rooms_list:
            #Check if room type provided is an office or living Space
            if room_type.lower() in self.room_types:
                room_name_1 = room
                room = room.lower().strip()
                if room not in self.all_rooms_list: #This if condition is used to create offices
                    if room_type.lower().strip() == 'office':
                        # new_room = Office(room)
                        self.office[room] = Office(room)
                        self.all_rooms_list.append(room)
                        print('An Office called ' + room_name_1 + ' has been successfully created!')
                    if room_type.lower().strip() == 'livingspace': #This if condition is used to create living spaces
                        new_room = LivingSpace(room)
                        self.living_space[room] = LivingSpace(room)
                        self.all_rooms_list.append(room)
                        print('A LivingSpace called ' + room_name_1 + ' has been successfully created!')
                else:
                    print('Room with '+ room.upper() + ' name already exists. Try again with new name!')
            else:
                print("Invalid Room Type")


    def add_person(self, person_id, last_name, first_name, person_type, wants_accommodation = ''):
        """"
        add_person method creates persons in the dojo. It Automaically calls allocate_room method to automatically allocate persons to rooms
        :params person_id: Unique Identifier of person
        :params last_name: Staff or Fellow last name
        :params first_name: Staff or Fellow first name
        :params person_type: Identifies whether your Staff or Fello
        :params wants_accommodation: Option argument for fellows to specify if they need Accomodation
        """
        person_type = person_type.strip().upper()
        if person_type in self.person_types:
            #Check if person already exists in dojo
            if person_id in self.persons:
                print('Person already exists')
            else:
                #Check if Person is Staff or Fellow and create them.
                if person_type.upper() == 'FELLOW':
                    person_id = person_id.strip().lower()
                    self.persons[person_id] = Fellow(person_id, last_name, first_name, person_type, wants_accommodation)
                    print(last_name.upper() + ' ' + first_name.upper() + ' has been successfully added.')
                    #Call Allocate room method to allocate rooms for this person
                    self.allocate_room(person_id, person_type, wants_accommodation)
                if person_type.upper() == 'STAFF':
                    person_id = person_id.strip().lower()
                    self.persons[person_id] = Staff(person_id, last_name, first_name, person_type, wants_accommodation)
                    print(last_name.upper() + ' ' + first_name.upper() + ' has been successfully added.')
                    self.allocate_room(person_id, person_type)
                    #Call Allocate room method to allocate rooms for this person
        else:
            #Alerts admin that the person type supplied is not correct
            print("Your person type is incorrect. It must be STAFF or FELLOW")

    def allocate_room(self, person_id, person_type, wants_accommodation = ''):
        """
        allocate_room method is used to automatically allocate persons to rooms
        :params person_id: Unique identifier of person in Dojo
        :params person_type: Identifies which type of staff to be written
        :params wants_accommodation: This is an optional argument used by
        fellows if they want living_space. If it's allocated for staff.
        Living room is not created.
        """
        if person_type.upper() in self.person_types:#Check if person is fellow
            offices_list = [] #Used to store offices that have available space
            for key in self.office.keys():
                if len(self.office[key].members) < self.max_number_of_people_in_office:
                    offices_list.append(key)
            if offices_list:
                #randomly selects room and adds person to room
                random_office = random.choice(offices_list)
                print(self.office[random_office].members)
                self.office[random_office].members.append(person_id) #Store person in the members list of that office
                self.persons[person_id].proom_name = random_office #Store Office Room in Persons Room attribute
                if person_type.upper() == 'FELLOW':
                    self.fellows_with_office_list.append(person_id) # Update fellows_with_office_list
                if person_type.upper() == 'STAFF':
                    self.staff_with_office_list.append(person_id) # Update staff_with_office_list
                print(self.persons[person_id].first_name + ' has been allocated office ' + random_office)
            else:
                if person_type.upper() == 'FELLOW':
                    self.fellows_who_missed_office.append(person_id) #Add Fellows name to list of fellows who have missed an office
                if person_type.upper() == 'STAFF':
                    self.staff_who_missed_office_list.append(person_id) # Add  Staff to list of fellows who missed an office
                print('There are no offices available for allocation, Create some!!!')
            #Check if Fellow Wants Accomodation
        if person_type.upper() == 'FELLOW':
            if wants_accommodation == 'Y':
                living_space_list = [] #List used to store living spaces before randomization
                for key in self.living_space.keys():
                    if len(self.living_space[key].members) < self.max_number_of_people_in_living_space:#Add living spaces to randomization list
                        living_space_list.append(key)
                if not living_space_list: #Check if living spaces are not available and inform user
                    self.fellows_who_missed_living_space.append(person_id) #Add name to persons who missed Living space
                    print ('There are no livingspaces available for allocation, Create some')
                else:
                    print(living_space_list)
                    random_living_space_room = random.choice(living_space_list)
                    print('Random living space ')
                    print(random_living_space_room)
                    self.living_space[random_living_space_room].members.append(person_id)#Add this person the members in a particular living room
                    self.persons[person_id].lroom_name = random_living_space_room #Store the persons living room in there object
                    self.fellows_with_living_room_list.append(person_id)#Add Fellow to list that stores fellows with living space
                    print(self.persons[person_id].first_name + ' has been allocated Living Space ' + random_living_space_room)
            else:
                #Store them in a list of those who don't want accomodation
                self.fellows_who_dont_want_living_space.append(person_id)

    def print_room(self,room_name):
        """
        This method prints names of members in a room supplied. It takes room name as an argument,
        and prints to the screen the members
        """
        if not isinstance(room_name,str):#Check if room_name provided is string
            print ("Room name must be a string")
        #Check if room provided is already created under offices , or livingspaces
        if room_name.lower() in self.office: #Check if room is an office
            #Print to the screen room has no members if the number of staff or fellows allocate is zero(0)
            if len(self.office[room_name].members) == 0:
                print(room_name.upper() + ' has no members')
            else:
                #Print to the screen the Room and it's members
                print ('Office Room '+ room_name.upper())
                print('-----------------------------------------------------------------')
                for name in self.office[room_name].members:
                    s = self.persons[name].last_name + ' ' +self.persons[name].first_name +','
                    print(s, end =" "  )
                print()
        elif room_name.lower() in self.living_space: #Check if room is an living space
            #Print to the screen room has no members if the number of staff or fellows allocate is zero(0)
            if len(self.living_space[room_name].members) == 0:
                print('Office ' + room_name.upper() + ' has no members')

            else:
                #Print to the screen the Room and it's members
                print ('Living Space Room '+room_name.upper())
                print('-----------------------------------------------------------------')
                for name in self.living_space[room_name].members:
                    s = self.persons[name].last_name + ' ' +self.persons[name].first_name + ','
                    print(s ,end=" ")
                print()
        else:
            #Print to the screen informing them that the room they want does not exist
            print('Your room doesn\'t exist')

    def print_allocations(self, filename=""):
        """
        print_allocations is method that prints to a .txt file or screen Rooms with allocated memebers
        It takes and optional argument filename, which if provided it saves it in the root folder of the app.
        Otherwise it prints to the screen

        :param filename: Refers to name of .txt file to be written to. It prints to the screen if this parameter is not specified
        """
        if not filename:
            #Print to the Screemn if File name not Provided
            for room_name in self.all_rooms_list:
                #Print Office Spaces first
                if room_name.lower() in self.office:
                    print('\n')
                    print('Office Room '+ room_name.upper()+'\n')
                    print('-----------------------------------------------------------------\n')
                    for name in self.office[room_name].members:
                         s = (self.persons[name].person_id + ' '
                                +self.persons[name].last_name + ' '
                                +self.persons[name].first_name +', ')
                         print(s ,end=" ")

                    print('\n')
                    #Print Office Spaces first
                if room_name.lower() in self.living_space:
                    print('\n')
                    print('Living Space Room '+room_name.upper()+'\n')
                    print('-----------------------------------------------------------------')
                    for name in self.living_space[room_name].members:
                        s =(self.persons[name].person_id + ' '
                            +self.persons[name].last_name + ' '
                            +self.persons[name].first_name + ', ')
                        print(s ,end=" ")
            print('\n')
        else:
            #Print to Filename provided.
            my_file = open(filename + ".txt", "w+") #Create and open File for Writing
            my_file.write('\n')
            my_file.write('-----------------------------------------------------------------\n')
            for room_name in self.all_rooms_list:
                #Write Offices First to file
                if room_name.lower() in self.office:
                    my_file.write('\n')
                    my_file.write ('Office Room '+ room_name.upper() +'\n')
                    my_file.write('-----------------------------------------------------------------\n')
                    for name in self.office[room_name].members:
                         my_file.write(self.persons[name].person_id + ' '
                         +self.persons[name].last_name + ' '
                         +self.persons[name].first_name +', ')
                    my_file.write('\n')
                #Write Living Spaces to File
                if room_name.lower() in self.living_space:
                    my_file.write('\n')
                    my_file.write ('Living Space Room '+room_name.upper()+"\n")
                    my_file.write('-----------------------------------------------------------------\n')
                    for name in self.living_space[room_name].members:
                        my_file.write(self.persons[name].person_id + ' '
                        +self.persons[name].last_name + ' '
                        +self.persons[name].first_name + ', ')
                    my_file.write('\n')
            my_file.close() #Close File after writing

    def print_unallocated(self, filename=''):
        """
        print_unallocated prints to the screen or file persons that are not allocated an office,
        living space or both. It prints to the screen if no file has been supplied.

        :param filename: Refers to name of .txt file to be written to. It prints to the screen if this parameter is not specified
        """
        if not filename:
            #Print to the Screen if file name not provided
            print('\n')
            #print('\n')
            print('Staff who missed office space')
            print('--------------------------------------------------------------\n')
            if len(self.staff_who_missed_office_list):
                for staff in self.staff_who_missed_office_list:
                    s =(self.persons[staff].person_id + ' '
                        + self.persons[staff].first_name + ' '
                        +self.persons[staff].last_name +", ")
                    print(s ,end=" ")
            #Print Fellows who missed office
            print('\n')
            print('Fellows who missed office space')
            print('--------------------------------------------------------------\n')
            if len(self.fellows_who_missed_office):
                for staff in self.fellows_who_missed_office:
                    s = (self.persons[staff].person_id + ' '
                        + self.persons[staff].first_name + ' '
                        +self.persons[staff].last_name+", ")
                    print(s ,end=" ")
            print('\n')
            print('Fellows who wanted but missed Living Space')
            print('--------------------------------------------------------------\n')
            if len(self.fellows_who_missed_living_space):
                for staff in self.fellows_who_missed_living_space:
                    s = (self.persons[staff].person_id + ' '
                        + self.persons[staff].first_name + ' '
                        +self.persons[staff].last_name+", ")
                    print(s ,end=" ")
            print('\n')
        else:
            #Write to File if file name is provide. File is saved in root folder
            new_file = open(filename + ".txt", "w") #Creat and open file for writing
            new_file.write('Staff who missed office space\n')
            new_file.write('--------------------------------------------------------------\n')
            if len(self.staff_who_missed_office_list):
                for staff in self.staff_who_missed_office_list:
                    new_file.write(self.persons[staff].person_id + ' '
                                    + self.persons[staff].first_name + ' '
                                    +self.persons[staff].last_name +", ")
            new_file.write('\n')
            #Write Fellow who missed office
            new_file.write('Fellows who missed office space\n')
            new_file.write('--------------------------------------------------------------\n')
            if len(self.fellows_who_missed_office):
                for staff in self.fellows_who_missed_office:
                    new_file.write(self.persons[staff].person_id + ' '
                                    + self.persons[staff].first_name + ' '
                                    +self.persons[staff].last_name +", ")
            new_file.write('\n')
            #Write Fellows who wanted Living spaces but were not automatically allocated
            new_file.write('Fellows who wanted but missed Living Space\n')
            new_file.write('--------------------------------------------------------------\n')
            if len(self.fellows_who_missed_living_space):
                for staff in self.fellows_who_missed_living_space:
                    new_file.write(self.persons[staff].person_id + ' '
                                    + self.persons[staff].first_name + ' '
                                    +self.persons[staff].last_name +", ")
            new_file.write('\n')
            new_file.close()#Close File after writing
    def reallocate_person(self, person_id, new_room_name):
        """
        reallocate_person method is used to change a Fellow from one living space to another living space,
        if the fellow opted to have living space. It also changes Fellows and staff from one room to another

        :param person_id:
        :param new_room_name:
        :return
        """
        new_room_name = new_room_name.lower().strip()
        if person_id in self.persons.keys():
            if new_room_name in self.all_rooms_list:
                #Get Current Persons Room
                current_office_room = self.persons[person_id].proom_name
            #Reallocate Person to New Room
                #Reallocate Fellow to new Living room
                if new_room_name in self.living_space:
                    current_living_space = self.persons[person_id].lroom_name
                    #Check if staff is being allocated a living space
                    if self.persons[person_id].person_type.upper() == 'STAFF':
                        print ('Staff are not supposed to be assigned Living space.')
                    else:
                        #Prevent reallocating Living space to fellows who didnt request living space
                        if current_living_space =='':
                            print("Fellow didnt opt in Livingspace program")
                        #Check if Person is already in the room being reallocated to
                        elif current_living_space == new_room_name:
                            print('Person already belongs to that room')
                        else:
                            #Delete Person From Living Room

                            #Add person to new Living Room
                            if len(self.living_space[new_room_name].members) < self.max_number_of_people_in_living_space:
                                self.living_space[current_room].members.remove(person_id)
                                self.living_space[new_room_name].members.append(person_id)
                                self.persons[person_id].lroom_name = new_room_name
                                print('Reallocation succesful')
                            else:
                                print('Rooms full to capcity')
                if new_room_name in self.office:
                    if current_office_room == new_room_name:
                        print('Person already belongs to that room')
                    else:
                        #Delete Person from current Office and assign them new Office
                        if len(self.office[new_room_name].members) < self.max_number_of_people_in_office:
                            self.office[current_office_room].members.remove(person_id)
                            self.office[new_room_name].members.append(person_id)
                            self.persons[person_id].proom_name = new_room_name
                            print('Reallocation succesful')
                        else:
                            print('Room full to capacity')
            else:
                print('Room Does\'t Exist')
        else:
            print('Person Doesn\'t Exist')

    def load_people(self, filename):
        """
        This method is used to add people(staff or fellows) to the dojo by specifying the text file that has the people to be loaded.
        It Reads the file line by line. It notifies the use lines that were not succesful
        :params filename: This is the  text filename (e.g filename.txt) that you want to load data from.
        """
        my_error_file = open('errors' + '.txt','w') #File to write lines with errors to during load_people
        if not filename:
            print('Please specify name of the file you want to read data from')
        else:
            try:
                my_file_read = open(filename + '.txt','r')
                for num, line in enumerate(my_file_read, 1):
                    line = line.strip()
                    list_of_arguments_in_file = line.split()
                    #print(list_of_arguments_in_file)
                    if len(list_of_arguments_in_file) == 5:
                        person_id = list_of_arguments_in_file[0]
                        last_name = list_of_arguments_in_file[1]
                        first_name = list_of_arguments_in_file[2]
                        person_type = list_of_arguments_in_file[3]
                        wants_accommodation = list_of_arguments_in_file[4]
                        self.add_person(person_id, last_name, first_name, person_type, wants_accommodation)
                    elif len(list_of_arguments_in_file) == 4:
                        person_id = list_of_arguments_in_file[0]
                        last_name = list_of_arguments_in_file[1]
                        first_name = list_of_arguments_in_file[2]
                        person_type = list_of_arguments_in_file[3]
                        self.add_person(person_id, last_name, first_name, person_type, wants_accommodation)
                    else:
                        my_error_file.write(line +' line number ('+ str(num)+')\n')
                        print("Arguments in this line were incorrect: line(" + str(num)+')')
                        print('Lines with errors have been saved to the file errors.txt in youre root folder')
            except:
                print('File Provided is either not a .txt or it doesnt exist')
        my_error_file.close()
    def save_state(self, sqlite_database_name):
        """
        This method is used to persist the Dojo object data to an sqlite database with the name provided.
        it takes one argument sqlite_database_name

        :params sqlite_database_name: This is the name of the sqlite database to persist data to.
        """
        if os.path.isfile('./'+sqlite_database_name+'.db'):
            print('That file name already exists, please provide a different filename')
        else:
            engine = create_engine('sqlite:///'+sqlite_database_name+'.db')
            Base.metadata.bind = engine
            DBSession = sessionmaker(bind=engine)
            session = DBSession()
            Base.metadata.create_all(engine)
            # Check whether living_space dictionary has items to be added to database and add them to the Rooms table in the database
            if len(self.living_space) > 0:
                for key in self.living_space:
                    new_room = Rooms(room_name = self.living_space[key].room_name,
                                     members = ' '.join(self.living_space[key].members),
                                     max_num = self.living_space[key].max_num, room_type ='LivingSpace')
                    session.add(new_room)
                    session.commit()
            #Checks whether office dictionary has items to be added to database and add them to the Rooms table in the database
            if len(self.office) > 0:
                for key in self.office:
                    new_room = Rooms(room_name = self.office[key].room_name,
                                      members = ' '.join(self.office[key].members),
                                      max_num = self.office[key].max_num, room_type ='Office')
                    session.add(new_room)
                    session.commit()
            #Checks whether persons dictionay has people to be added to the database and add them
            if  len(self.persons) > 0:
                for key in self.persons: #This For loop is used to traverse all keys in the persons dictionary
                    if self.persons[key].person_type.upper() == 'STAFF':#This if statement is used to add Staff to People table in the database
                        new_person = People(person_id = self.persons[key].person_id,
                                            last_name = self.persons[key].last_name,
                                            first_name = self.persons[key].first_name,
                                            person_type = 'STAFF',
                                            proom_name = self.persons[key].proom_name)
                        session.add(new_person)
                        session.commit()
                    if self.persons[key].person_type.upper() == 'FELLOW': #This if statement is used to add Staff to People table in the database
                        new_person = People(person_id = self.persons[key].person_id,
                                            last_name = self.persons[key].last_name,
                                            first_name = self.persons[key].first_name,
                                            person_type = 'FELLOW',
                                            wants_accommodation = self.persons[key].wants_accommodation,
                                            proom_name = self.persons[key].proom_name,
                                            lroom_name = self.persons[key].lroom_name)
                        session.add(new_person)
                        session.commit()
            #The if staements below are used to store list names and there values as a string in the Lists Database Table
            if len(self.fellows_with_living_room_list) > 0:
                new_list  = Lists(list_name = 'fellows_with_living_room_list',
                                    list_string = ' '.join(self.fellows_with_living_room_list))
                session.add(new_list)
                session.commit()
            if len(self.fellows_with_office_list) > 0:
                new_list  = Lists(list_name = 'fellows_with_office_list',
                                    list_string = ' '.join(self.fellows_with_office_list))
                session.add(new_list)
                session.commit()
            if len(self.fellows_who_missed_living_space) > 0:
                new_list  = Lists(list_name = 'fellows_who_missed_living_space',
                                    list_string = ' '.join(self.fellows_who_missed_living_space))
                session.add(new_list)
                session.commit()
            if len(self.fellows_who_dont_want_living_space) > 0:
                new_list  = Lists(list_name = 'fellows_who_dont_want_living_space',
                                    list_string = ' '.join(self.fellows_who_dont_want_living_space))
                session.add(new_list)
                session.commit()
            if len(self.fellows_who_missed_office) > 0:
                new_list  = Lists(list_name = 'fellows_who_missed_office',
                                    list_string = ' '.join(self.fellows_who_missed_office))
                session.add(new_list)
                session.commit()
            if len(self.staff_with_office_list) > 0:
                new_list  = Lists(list_name = 'staff_with_office_list',
                                    list_string = ' '.join(self.staff_with_office_list))
                session.add(new_list)
                session.commit()
            if len(self.staff_who_missed_office_list) > 0:
                new_list  = Lists(list_name = 'staff_who_missed_office_list',
                                    list_string = ' '.join(self.staff_who_missed_office_list))
                session.add(new_list)
                session.commit()
            if len(self.all_rooms_list) > 0:
                new_list  = Lists(list_name = 'all_rooms_list',
                                    list_string = ' '.join(self.all_rooms_list))
                session.add(new_list)
                session.commit()
            session.close() #Close Database session


    def load_state(self, sqlite_database_name):
        """
        This method is supposed to restore previous or persisted state of the Dojo data from a database provided.
        :params sqlite_database_name: The Name of database that data will be prestored from.
        """
        try:
            if os.path.isfile('./'+sqlite_database_name+'.db'): #Check if filename provided exists other wise inform user to provide correct file name
                engine = create_engine('sqlite:///'+sqlite_database_name+'.db')
                Base.metadata.bind = engine
                DBSession = sessionmaker(bind=engine)
                session = DBSession()
                Base.metadata.create_all(engine)
                for instance in session.query(Lists):
                    if instance.list_name == 'fellows_with_living_room_list':
                        self.fellows_with_living_room_list = instance.list_string.split()
                    if instance.list_name == 'fellows_with_office_list':
                        self.fellows_with_office_list = instance.list_string.split()
                    if instance.list_name == 'fellows_who_missed_living_space':
                        self.fellows_who_missed_living_space = instance.list_string.split()
                    if instance.list_name == 'fellows_who_dont_want_living_space':
                        self.fellows_who_dont_want_living_space = instance.list_string.split()
                    if instance.list_name == 'fellows_who_missed_office':
                        self.fellows_who_missed_office = instance.list_string.split()
                    if instance.list_name == 'staff_with_office_list':
                        self.staff_with_office_list = instance.list_string.split()
                    if instance.list_name == 'staff_who_missed_office_list':
                        self.staff_who_missed_office_list = instance.list_string.split()
                    if instance.list_name == 'all_rooms_list':
                        self.all_rooms_list = instance.list_string.split()
                for instance in session.query(People):
                    if instance.person_type.upper() =='STAFF':
                        self.persons[instance.person_id] = Staff(instance.person_id,
                                                                instance.last_name,
                                                                instance.first_name,
                                                                instance.proom_name)
                    if instance.person_type.upper() == "FELLOW":
                        self.persons[instance.person_id] = Fellow(instance.person_id,
                                                                instance.last_name,
                                                                instance.first_name,
                                                                instance.wants_accommodation,
                                                                instance.proom_name,
                                                                instance.lroom_name)
                for instance in session.query(Rooms):
                    if instance.room_type.upper() == 'OFFICE':
                        self.office[instance.room_name] = Office(instance.room_name)
                        self.office[instance.room_name].members = instance.members.split()
                    if instance.room_type.upper() == 'LIVINGSPACE':
                        self.living_space[instance.room_name] = LivingSpace(instance.room_name)
                        self.living_space[instance.room_name].members = instance.members.split()
                session.close()
                print('State Loaded Succesfully')
            else:
                print('Database filename provided does not exist')
        except:
            print('State loading unsuccesful. Contact administrator')
