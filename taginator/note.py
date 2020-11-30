class Note():
    def __init__(self, name, importer, text):
        self.name = name
        self.importer = importer
        self.text = text
        self.extracted_values = {}

    def set_extracted_values(self, key, value):
        self.extracted_values[key] = value