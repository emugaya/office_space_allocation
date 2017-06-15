#!/usr/bin/env python
"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.

Usage:
    create_room <room_type> <room_name> ...
    add_person <person_id> <last_name> <first_name> <person_type> [<wants_accommodation>]
    print_room <room_name>
    print_allocations [<filename>]
    print_unallocated [<filename>]
    reallocate_person <person_identifier> <new_room_name>
    save_state <--db=sqlite_database>
    load_people <filename>

    my_program (-h | --help | --version)

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
    --baud=<n>  Baudrate [default: 9690]
    --timeout=<seconds> Time [default: 30]
"""

import sys
import cmd
from docopt import docopt, DocoptExit
from dojo.models.dojo import Dojo
import pickle

# from sqlalchemy import create_engine
# from sqlalchemy.ext.decorator import declarative_base
# from status import Status #Importing the class tables
# from sqlalchemy import sessionmaker


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn

my_dojo = Dojo()
class DojoCLI(cmd.Cmd):
    intro = '                         Welcome to Dojo!:\n' \
        + 'You can perform the list of command below:\n'\
        +'\n'\
        + '1. Create Room using: create_room <room_type> <room_name>\n'\
        +'\n'\
        +'2. Add Person using: add_person <person_id> <last_name> <first_name> <person_type> [<wants_accommodation>]\n'\
        +'\n'\
        +'3. Print out members in a room using: print_room <room_name>\n'\
        +'\n'\
        +'4. Print Allocations using: print_allocations [<filename>]\n'\
        +'\n'\
        +'5. Print out unallocated staff and fellows using: print_unallocated [<filename>]\n'\
        +'\n'\
        +'6. Reallocate Person to room: reallocate_person <person_identifier> <new_room_name>\n'\
        +'\n'\
        +'7. Save Application State to SQLite Database using: save_state <--db=sqlite_database>\n'\
        +'\n'\
        +'8. Load last state of Application from Database using: load_state <sqlite_database>\n'\
        +'\n'\
        + ' (Type help any time for a list of commands.)'
    prompt = '(Dojo: Enter Command to Proceed:) '

    @docopt_cmd
    def do_create_room(self,arg):
        """ Usage: create_room <room_type> <room_name> ..."""
        room_type = arg['<room_type>']
        room_name = arg['<room_name>']
        my_dojo.create_room(room_type,room_name)

    @docopt_cmd
    def do_add_person(self, arg):
        """Usage: add_person <person_id> <last_name> <first_name> <person_type> [<wants_accommodation>] """
        person_id = arg['<person_id>']
        last_name = arg['<last_name>']
        first_name = arg['<first_name>']
        person_type = arg['<person_type>']
        wants_accommodation = arg['<wants_accommodation>']

        my_dojo.add_person(person_id, last_name, first_name, person_type, wants_accommodation)

    @docopt_cmd
    def do_print_room(self, arg):
        """Usage: print_room <room_name> """
        room_name = arg['<room_name>']
        my_dojo.print_room(room_name)

    @docopt_cmd
    def do_print_allocations(self,arg):
        """Usage: print_allocations [<filename>] """
        filename = arg['<filename>']
        my_dojo.print_allocations(filename)

    @docopt_cmd
    def do_print_unallocated(self,arg):
        """Usage: print_unallocated [<filename>] """
        filename = arg['<filename>']
        my_dojo.print_unallocated(filename)

    @docopt_cmd
    def do_load_people(self, arg):
        """Usage: load_people <filename> """
        filename = arg['<filename>']
        my_dojo.load_people(filename)

    @docopt_cmd
    def do_reallocate_person(self,arg):
        """Usage: reallocate_person <person_identifier> <new_room_name>  """
        person_identifier = arg['<person_identifier>']
        new_room_name = arg['<new_room_name>']
        my_dojo.reallocate_person(person_identifier, new_room_name)

    @docopt_cmd
    def do_save_state(self, arg):
        """Usage: save_state <--db=sqlite_database> """
        sqlite_database_name = arg['<--db=sqlite_database>']
        my_dojo.save_state(sqlite_database_name)

    @docopt_cmd
    def do_load_state(self,arg):
        """Usage: save_state [<sqlite_database>] """
        sqlite_database = arg['<sqlite_database>']
        my_dojo.load_state(sqlite_database)


    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()

# opt = docopt(__doc__, sys.argv[1:])


DojoCLI().cmdloop()

#print(opt)
