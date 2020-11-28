from . import importer

def main():
    print("Hello")
    while(True):
        comm = input("Enter command: ")
        if comm == "import":
            path = input("Path: ")
            imp = importer.TxtImporter()
            imp.import_notes(path)
        elif comm == "list":
            pass
        elif comm == "exit":
            break
        else:
            print("Command not found")

if __name__ == '__main__':
    main()
