class Helper():
    def help(self, command):
        if command == "help":
            print("Available commands:\n\n\thelp\n\timport\n\tshow\n\tlist\n\tfilter\n\tsearch\n\tsummary\n\tsort\n\texit\n\nInput \'help [command]\' to learn more about each command.")
        elif command == "help import":
            print("\n\t\'import\' first prompts the user for a file path and then imports text files from the indicated folder and automatically processes them. "
                  "Both local and global file paths work. To import from current folder leave empty.\n")
        elif command == "help show":
            print("\n\t\'show\' first prompts the user for a file name of an imported note and then shows its content and all automatically generated tags. "
                  "Input \'all\' to show all currently imported notes.\n Shown notes can be inspected for any occurence of the specific word. Te enter an inspection mode type [y] when prompted. To exit inspection mode type [n] when prompted. \n")
        elif command == "help list":
            print("\n\t\'list\' lists all currently imported files and their automatically generated tags.\n")
        elif command == "help search":
            print("\n\t\'search\' first prompts the user to choose if they want to search by tag (notes with exact tag match), by phrase (notes with content containing matching phrase) or by date (notes with content containing matching date fragment/whole date), "
                  "then prompts them again for the tag/phrase/date to search and scope to show for and finally shows selected scope for all currently imported notes with matching tag/phrase/date. Scope can be either the entire file or just context for the search query. \n")
        elif command == "help exit":
            print("\n\t\'exit\' closes Taginator.\n")
        elif command == "help filter":
            print("\n\t\'filter\' first prompts the user whether they want to filter by tag (notes with exact tag match), by phrase (notes with content containing matching phrase) or by date (notes with content containing matching date fragment/whole date). "
                  "A list of notes fulfilling the criteria is returned. Furthermore, returned notes can be shown (content + all generated tags), searched for context for a given tag and summarized.\n")
        elif command == "help help":
            print("\n\tFunny\n")
        elif command == "help summary":
            print("\n\t\'summary\' first prompts the user for a file name of an imported note and then shows its summary. Input \'all\' to show all notes.\n")
        elif command == "help sort":
            print("\n\t\'sort\' sorts all currently imported notes by chosen order. [import] - by import, [chrono] - chronological, [antichrono] - reverse chronological\n")
        else:
            print("Command not found")
