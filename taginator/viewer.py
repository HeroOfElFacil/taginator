import dateutil.parser as parser
from datetime import datetime


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


    def searchPrint(self, scope, name, note, files, token, searchList):
        if(scope=="context"):
            print("\n\n"+name+"\n"+note.filedate.strftime("%Y/%m/%d %H:%m:%S")+"\n")
            for token in searchList:
                self.show_context(files, name, token)
        else:
            self.show_file(files, name)

    
    def search_notes(self, files, what, scope):
        files = self.sort_by_sortflag(files, self.sortflag)
        if what == "tag" or what == "t":
            searchFor = input("tag: ")
            searchFor = searchFor.strip()
            searchList = searchFor.split("|")
            print("\nNotes matching tags: \'" + searchFor + "\'\n")
            searchFlag = False
            for name, note in files.items():
                searchIter = 0
                for token in searchList:
                    if token.strip().lower() in note.tags:
                        searchIter += 1
                if searchIter == len(searchList):
                    self.searchPrint(scope, name, note, files, token, searchList)
                    searchFlag = True
            if not searchFlag:
                print("No notes matching tags: \'"+searchFor+"\' found!\n")

        elif what == "phrase" or what == "p":
            searchFor = input("phrase: ")
            searchFor = searchFor.strip()
            searchList = searchFor.split("|")
            print("\nNotes matching phrases: \'" + searchFor + "\'\n")
            searchFlag = False
            for name, note in files.items():
                searchIter = 0
                for token in searchList:
                    if token.strip().lower() in note.text.lower():
                        searchIter += 1
                if searchIter == len(searchList):
                    self.searchPrint(scope, name, note, files, token, searchList)
                    searchFlag = True
            if not searchFlag:
                print("No notes matching phrases: \'" + searchFor + "\' found!\n")

        elif what == "date" or what == "d":
            searchFor = input("date: ")
            DEFAULT = datetime(1, 1, 1, 0, 0, 0)
            date_normalized = parser.parse(searchFor, default = DEFAULT)
            print("\nNotes matching date: \'" + searchFor + "\'\n")
            searchFlag = False
            for name, note in files.items():
                if date_normalized in note.normalized_dates:
                    searchFlag = True
                    dateInText = note.normalized_dates[date_normalized]
                    self.searchPrint(scope, name, note, files, dateInText, [dateInText])
            if not searchFlag:
                print("No notes matching date: \'" + searchFor + "\' found!\n")

        elif what == "":
            print("\n")

        else:
            print("Invalid command")

    def filter_notes(self, files, what):
        files = self.sort_by_sortflag(files, self.sortflag)
        filteredList = []
        if what == "tag" or what == "t":
            searchFor = input("tag: ")
            searchFor = searchFor.strip()
            searchList = searchFor.split("|")
            print("\nNotes matching tags: \'" + searchFor + "\'\n")
            searchFlag = False
            for name, note in files.items():
                searchIter = 0
                for token in searchList:
                    if token.strip().lower() in note.tags:
                        searchIter += 1
                if searchIter == len(searchList):
                    filteredList.append(name)
                    searchFlag = True
            if not searchFlag:
                print("No notes matching tags: \'"+searchFor+"\' found!\n")

        elif what == "phrase" or what == "p":
            searchFor = input("phrase: ")
            searchFor = searchFor.strip()
            searchList = searchFor.split("|")
            print("\nNotes matching phrases: \'" + searchFor + "\'\n")
            searchFlag = False
            for name, note in files.items():
                searchIter = 0
                for token in searchList:
                    if token.strip().lower() in note.text.lower():
                        searchIter += 1
                if searchIter == len(searchList):
                    filteredList.append(name)
                    searchFlag = True
            if not searchFlag:
                print("No notes matching phrases: \'" + searchFor + "\' found!\n")

        elif what == "date" or what == "d":
            searchFor = input("date: ")
            DEFAULT = datetime(1, 1, 1, 0, 0, 0)
            date_normalized = parser.parse(searchFor, default = DEFAULT)
            print("\nNotes matching date: \'" + searchFor + "\'\n")
            searchFlag = False
            for name, note in files.items():
                if date_normalized in note.normalized_dates:
                    searchFlag = True
                    filteredList.append(name)
            if not searchFlag:
                print("No notes matching date: \'" + searchFor + "\' found!\n")

        elif what == "":
            print("\n")

        else:
            print("Invalid command")

        if len(filteredList) > 0:
            for name in filteredList:
                print(name)
        return filteredList

    def show_summary(self, files):
        files = self.sort_by_sortflag(files, self.sortflag)
        for name, note in files.items():
            print("\nFile: " + name + "\t" + note.filedate.strftime("%Y/%m/%d %H:%m:%S"))
            print("Summary: " + note.summary)
