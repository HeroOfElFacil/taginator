class Helper():
    def help(self, command):
        if command == "help":
            print("Available commands:\n\n\thelp\n\timport\n\tshow\n\tlist\n\tsearch\n\texit\n\nInput \'help [command]\' to learn more about each command.")
        elif command == "help import":
            print("\n\t\'import\' first prompts the user for a file path and then imports text files from the indicated folder and automatically processes them. "
                  "Both local and global file paths work. To import from current folder leave empty.\n")
        elif command == "help show":
            print("\n\t\'show\' first prompts the user for a file name of an imported note and then shows its content and all automatically generated tags. "
                  "Input \'all\' to show all currently imported notes.\n Shown notes can be inspected for any occurence of the specific word. Te enter an inspection mode type [y] when prompted. To exit inspection mode type [n] when prompted. \n")
        elif command == "help list":
            print("\n\t\'list\' lists all currently imported files and their automatically generated tags.\n")
        elif command == "help search":
            print("\n\t\'search\' first prompts the user to choose if they want to search by tag (notes with exact tag match) or by phrase (notes with content containing matching phrase), then prompts them again for the tag/phrase to search for and finally shows all currently imported notes with matching tag/phrase.\n")
        elif command == "help exit":
            print("\n\t\'exit\' closes Taginator.\n")
        elif command == "help help":
            print("\n\tFunny\n")
        else:
            print("Command not found")