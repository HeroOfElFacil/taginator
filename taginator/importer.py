import os

class Importer():
    def __init__(self):
        self.text = {}
    def import_notes(self, *args):
        pass
    def get_notes(self):
        return self.text


class TxtImporter(Importer):
    def import_notes(self, *args):
        print("Importing files...")
        filepath = args[0] if args and args[0] else os.getcwd()
        filelist = os.listdir(filepath)
        for file in filelist:
            if file.endswith(".txt"):
                print(file)  # filename
                try:
                    with open(os.path.join(filepath, file), 'r', encoding="utf-8") as f:
                        contents = f.read()
                        self.text[(file, "txt")] = contents
                except Exception as e:
                    print(e)
        print("Done!")
