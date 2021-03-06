from . import importer, viewer, extractor, helper

class Taginator():
    def __init__(self):
        self.importers = []
        self.viewer = viewer.Viewer()
        self.notes = {}
        self.extractors = [extractor.DateExtractor(), extractor.NameExtractor()]
        self.helper = helper.Helper()
        self.tagextractor = extractor.TagExtractor()
        self.summarizer = extractor.SummaryExtractor()

    def list_notes(self):
        self.viewer.view_listed(self.notes)

    def import_notes(self, path):
        imp = importer.TxtImporter(path)
        imp.import_notes()
        processed = self.__process_notes(imp.get_notes())
        self.notes.update(processed)
        self.importers.append(imp)

    def __process_notes(self, dict):
        for ext in self.extractors:
            for name, note in dict.items():
                note.set_extracted_values(ext.get_name(), ext.extract(note))
                if isinstance(ext, extractor.DateExtractor):
                    note.normalized_dates = ext.extract_datetime(note)
        for name, note in dict.items():
            note.add_tags(self.tagextractor.extract(note))
            note.add_tokens()
            note.change_summary(self.summarizer.extract(note))
        return dict
    
    def show_notes(self, file_name):
        self.viewer.show_file(self.notes, file_name)
        
    def find_context(self, file_name, keyword):
        self.viewer.show_context(self.notes, file_name, keyword)

    def search(self, tagOrPhrase, scope):
        self.viewer.search_notes(self.notes, tagOrPhrase, scope)

    def filter(self, tagOrPhrase):
        return self.viewer.filter_notes(self.notes, tagOrPhrase)

    def summary(self, file_name):
        self.viewer.show_summary(self.notes if file_name == "all" else {file_name: self.notes[file_name]})

    def help_me(self, command):
        self.helper.help(command)

    def set_sortflag(self, flag):
        self.viewer.sortflag = flag
