class Viewer():
    def viewListed(self, files):
        print(len(files), "imported files found")
        for name, ext in files:
            print(name)

