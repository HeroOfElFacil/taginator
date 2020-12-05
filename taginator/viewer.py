import os

class Viewer():
    def view_listed(self, files):
        print(len(files), "imported files found")
        for name, note in files.items():
            print(name)
            for key, value in note.extracted_values.items():
                print("\t", key, ":")
                print("\t\t", ",".join(value))
       
    def show_file(self, files, file_name):
        if file_name == "all":
            for name, note in files.items():
                print("\n", name)
                print("\n", note.text)
        else:
            try:
                for name, note in files.items():
                    if os.path.splitext(name)[0] == file_name:
                        print("\n", name)
                        print("\n", note.text)
            except:
                print("Note not found")


