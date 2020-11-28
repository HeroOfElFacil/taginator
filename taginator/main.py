from . import importer, viewer

def main():
    print("Hello")
    #tworzenie obiektów klas tutaj, póki co, żeby imp pamiętał pliki z różnych importów
    imp = importer.TxtImporter()
    v = viewer.Viewer()

    while(True):
        comm = input("Enter command: ")
        if comm == "import":
            path = input("Path: ")
            #imp = importer.TxtImporter()
            imp.import_notes(path)
        elif comm == "list":
            v.viewListed(imp.text)
            # #also wersja łopatologiczna, dla niezmodyfikowanej komendy import i bez klasy Viewer(
            # try:
            #     imp
            # except:
            #     print("0 imported files found")
            # else:
            #     print(len(imp.text),"imported files found")
            #     for file, ext in imp.text:
            #         print(file)

        elif comm == "exit":
            break
        else:
            print("Command not found")

if __name__ == '__main__':
    main()
