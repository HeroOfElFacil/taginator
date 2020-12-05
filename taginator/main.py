from . import taginator

def main():
    print("Hello. Input \'help\' if you don't know what to do.")
    tag_service = taginator.Taginator()

    while(True):
        comm = input("Enter command: ")
        if comm == "import":
            path = input("Path: ")
            tag_service.import_notes(path)

        elif comm == "list":
            tag_service.list_notes()
            
        elif comm == "show":
            file_name = input("Note name: ")
            tag_service.show_notes(file_name)

        elif comm.startswith("help"):
            tag_service.help_me(comm)

        elif comm == "exit":
            break
        else:
            print("Command not found")

if __name__ == '__main__':
    main()
