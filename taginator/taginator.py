from . import importer, viewer, extractor

class Taginator():
    def __init__(self):
        self.importers = []
        self.viewer = viewer.Viewer()
        self.notes = {}
        self.extractors = [extractor.DateExtractor()]

    def list_notes(self):
        for imp in self.importers:
            print("Source:", imp.get_info())
            self.viewer.view_listed(imp.get_notes(), self.extractors)

    def import_notes(self, path):
        imp = importer.TxtImporter(path)
        imp.import_notes()
        self.importers.append(imp)

