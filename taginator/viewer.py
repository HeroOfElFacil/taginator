import os

class Viewer():
    def __init__(self):
        self.flag = False

    def view_listed(self, files):
        print(len(files), "imported files found")
        for name, note in files.items():
            print(name)
            for key, value in note.extracted_values.items():
                print("\t", key, ":")
                print("\t\t", ",".join(value))
            print("\tTags:")
            print("\t\t", ",".join(note.tags))
       
    def show_file(self, files, file_name):
        if file_name == "all":
            for name, note in files.items():
                self.show_file(files, name)

        else:
            if file_name in files:
                note = files[file_name]
                print("\n", file_name)
                print("\n", note.text)
                for key, value in note.extracted_values.items():
                    print("\t", key, ":")
                    print("\t\t", ",".join(value))
                print("\tTags:")
                print("\t\t", ",".join(note.tags))
            else:
                print("Note not found")

    def show_context(self, files, file_name, keyword):
        if file_name in files:
            note = files[file_name]
            for token in note.tokens:
                if " " + keyword.lower() in token.lower():
                    if self.flag: print("File: " + file_name)
                    print("keyword: ", keyword)
                    print("context:", token, "\n")
        elif file_name == "all":
            for name, note in files.items():
                self.flag = True
                self.show_context(files, name, keyword)
                self.flag = False


        else:
            print("Note not found")           

