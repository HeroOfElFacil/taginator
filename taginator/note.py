import nltk

class Note():
    def __init__(self, name, importer, text):
        self.name = name
        self.importer = importer
        self.text = text
        self.extracted_values = {}
        self.tags = []

    def set_extracted_values(self, key, value):
        self.extracted_values[key] = value

    def add_tags(self, tags):
        self.tags.extend(tags)
     
    def add_tokens(self):
        self.tokens = nltk.sent_tokenize(self.text)
