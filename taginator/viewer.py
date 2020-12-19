import os


class Viewer():
    def __init__(self):
        self.flag = False
        self.sortflag = "import"

    def sort_by_sortflag(self, files, flag):
        if flag=="import":
            return files
        if flag=="chrono":
            return dict(sorted(files.items(), key=lambda x: x[1].filedate, reverse=False))
        if flag=="antichrono":
            return dict(sorted(files.items(), key=lambda x: x[1].filedate, reverse=True))

    def view_listed(self, files):
        files = self.sort_by_sortflag(files, self.sortflag)
        print(len(files), "imported files found")
        for name, note in files.items():
            print("\n\n"+name+"\n"+note.filedate.strftime("%Y/%m/%d %H:%m:%S"))
            for key, value in note.extracted_values.items():
                print("\t", key, ":")
                print("\t\t", ",".join(value))
            print("\tTags:")
            print("\t\t", ",".join(note.tags))

    def show_file(self, files, file_name):
        files = self.sort_by_sortflag(files, self.sortflag)
        if file_name == "all":
            for name, note in files.items():
                self.show_file(files, name)

        else:
            if file_name in files:
                note = files[file_name]
                print("\n\n", file_name+"\n"+note.filedate.strftime("%Y/%m/%d %H:%m:%S"))
                print("\n", note.text)
                for key, value in note.extracted_values.items():
                    print("\t", key, ":")
                    print("\t\t", ",".join(value))
                print("\tTags:")
                print("\t\t", ",".join(note.tags))
            else:
                print("Note not found")

    def show_context(self, files, file_name, keyword):
        files = self.sort_by_sortflag(files, self.sortflag)
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

    def search_notes(self, files, what):
        files = self.sort_by_sortflag(files, self.sortflag)
        if what == "tag" or what == "t":
            searchFor = input("tag: ")
            searchFor = searchFor.strip()
            print("\nNotes matching tag: \'" + searchFor + "\'\n")
            searchFlag = False
            for name, note in files.items():
                if searchFor.lower() in note.tags:
                    searchFlag = True
                    self.show_file(files, name)
            if not searchFlag:
                print("No notes matching tag: \'"+searchFor+"\' found!\n")

        elif what == "phrase" or what == "p":
            print("Sorry! This function isn't implemented yet.")

        elif what == "date" or what == "d":
            searchFor = input("date: ")
            DEFAULT = datetime(1, 1, 1, 0, 0, 0)
            date_normalized = parser.parse(searchFor, default = DEFAULT)
            print("\nNotes matching date: \'" + searchFor + "\'\n")
            searchFlag = False
            for name, note in files.items():
                if date_normalized in note.normalized_dates:
                    searchFlag = True
                    self.show_file(files, name)
            if not searchFlag:
                print("No notes matching date: \'" + searchFor + "\' found!\n")

        else:
            print("Invalid command")

    def show_summary(self, files):
        files = self.sort_by_sortflag(files, self.sortflag)
        for name, note in files.items():
            print("\nFile: " + name + "\t" + note.filedate.strftime("%Y/%m/%d %H:%m:%S"))
            print("Summary: " + note.summary)
