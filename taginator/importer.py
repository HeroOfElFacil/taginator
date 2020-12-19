from abc import ABC, abstractmethod
import os
import datetime
from . import note

class Importer(ABC):
    def __init__(self, *args):
        self.text = {}

    @abstractmethod
    def import_notes(self, *args):
        pass

    @abstractmethod
    def get_info(self):
        pass

    def get_notes(self):
        return self.text.copy()


class TxtImporter(Importer):
    def __init__(self, *args):
        super().__init__()
        self.path = args[0] if args and args[0] else os.getcwd()

    def import_notes(self, *args):
        self.text = {}
        print("Importing files...")
        filelist = os.listdir(self.path)
        for file in filelist:
            if file.endswith(".txt"):
                print(file)  # filename
                try:
                    filedate = datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(self.path, file)))
                    with open(os.path.join(self.path, file), 'r', encoding="utf-8") as f:
                        content = f.read().strip()
                        self.text[os.path.splitext(file)[0]] = note.Note(file, self, content, filedate)
                except Exception as e:
                    print(e)

        print("Done!")

    def get_info(self):
        return self.path
