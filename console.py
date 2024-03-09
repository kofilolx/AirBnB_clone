#!/usr/bin/python3
"""Console platform for the project"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter."""
    prompt = '(hbnb)'
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
        }

    def emptyline(self):
        """"Implement no action when an empty line is encountered."""
        pass

    
    def do_quit(self, arg):
        """Exit console successfully"""
        return True


    def do_nothing(self, arg):
        """Ideal Method"""
        pass

    
    def do_EOF(self, arg):
        """Signal to exit program"""
        print("")
        return True


    def do_create(self, arg):
        """Create a new instance of basemodel class"""
