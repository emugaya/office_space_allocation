# Office Space Allocation
This system will be used to automatically allocate spaces to people at random.
### Constraints
The Dojo has rooms, which can be offices or living spaces. An office can accommodate a maximum of 6 people.

A living space can accommodate a maximum of 4 people. A person to be allocated could be a fellow or staff. Staff cannot be allocated living spaces.

Fellows have a choice to choose a living space or not. This system will be used to automatically allocate spaces to people at random.
### Data Types Used:
1. Lists - Lists are used to track allocations. The names of lists are self explanatory and the code is well documented.
2. Dicts - Are used to store objects Person, and Room. For Person the person_id is the key and the Object is the value. For Room, the room name is the key, and object of that room is the value. Living spaces and Office Spaces are stored in different Dictinaries

### Runing the Application:
1. Make sure you have Python 3.5.2 or later
2. Create a virtual environment ``` virtualenv -p python3 dojocli ```
3. Clone this repo ```git clone https://github.com/emugaya/office_space_allocation.git```
4. Activate the environment by running ```source sourec dojocli/bin/activate```
5. Change directory to `office_space_allocation` by running ```cd office_space_allocation```
6. Install requirements ``` pip3 install -r requirements.txt ```
7. Run the application using ```python dojo_cli.py```

### Functions Implemented and Working:
1. ```create_room <room_type> <room_name>``` - Creates rooms in the Dojo. Using this command, the user should be able to create as many rooms as possible by specifying multiple room names after the create_room command.

2. ```add_person <person_name> <FELLOW|STAFF> [wants_accommodation] ```- Adds a person to the system and allocates the person to a random room. wants_accommodation here is an optional argument which can be either Y or N. The default value if it is not provided is N.

3. ```print_room <room_name>``` - Prints the names of all the people in room_name on the screen.

4. ```print_allocations [-o=filename]``` - Prints a list of allocations onto the screen. Specifying the optional -o option here outputs the registered allocations to a txt file.

5. ```print_unallocated [-o=filename]``` - Prints a list of unallocated people to the screen. Specifying the -o option here outputs the information to the txt file provided.

6. ```reallocate_person <person_identifier> <new_room_name>``` - Reallocate the person with person_identifier to new_room_name.

7. ```load_people ```- Adds people to rooms from a txt file. This saves lines with errors to a file errors.txt in the root folder

8. ```save_state [--db=sqlite_database]``` - Persists all the data stored in the app to a SQLite database. Specifying the --db parameter explicitly stores the data in the sqlite_database specified. This metthod takes a name of sqlite database you need to save data. It doesn't allow saving data t an already existing database. This can be enabled after ensuring that already existing records are not replicated.

9. ```load_state <sqlite_database>``` - Loads data from a database into the application. This requires some one to enter an already existing database that was saved using the save_state method.
