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
                self.show_file(files, name)

        else:
            if file_name in files:
                note = files[file_name]
                print("\n", file_name)
                print("\n", note.text)
                for key, value in note.extracted_values.items():
                    print("\n\t", key, ":")
                    print("\t\t", ",".join(value))
            else:
                print("Note not found")


