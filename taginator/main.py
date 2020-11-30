from . import taginator

def main():
    print("Hello")
    tag_service = taginator.Taginator()

    while(True):
        comm = input("Enter command: ")
        if comm == "import":
            path = input("Path: ")
            tag_service.import_notes(path)
        elif comm == "list":
            tag_service.list_notes()

        elif comm == "exit":
            break
        else:
            print("Command not found")

if __name__ == '__main__':
    main()
