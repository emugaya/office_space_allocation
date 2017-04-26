#!/usr/bin/env python
"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.

Usage:
    dojo.py create_room <room_type> <room_name> ...
    dojo.py add_person <person_id> <last_name> <first_name> <person_type> [<wants_accommodation>]
    dojo.py print_room <room_name>
    dojo.py print_allocations [<filename>]
    dojo.py print_unallocated [<filename>]

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

my_dojo = Dojo()
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


class DojoCLI(cmd.Cmd):
    intro = 'Welcome to Dojo!:' \
        + ' (Type help for a list of commands that you will be using to .)'
    prompt = '(Dojo: Enter Command to Proceed:) '
    file = None

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



    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()

# opt = docopt(__doc__, sys.argv[1:])


DojoCLI().cmdloop()

#print(opt)
