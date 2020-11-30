class Viewer():
    def view_listed(self, files, extractors):
        print(len(files), "imported files found")
        for name, note in files.items():
            print("\t", name)
            for extractor in extractors:
                print("\t\t", extractor.get_name(), ":")
                print("\t\t\t", ",".join(extractor.extract(note)))

