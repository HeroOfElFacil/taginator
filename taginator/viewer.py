class Viewer():
    def view_listed(self, files):
        print(len(files), "imported files found")
        for name, note in files.items():
            print(name)
            for key, value in note.extracted_values.items():
                print("\t", key, ":")
                print("\t\t", ",".join(value))


