from abc import ABC, abstractmethod
from nltk.tag import pos_tag
from datetime import datetime
import datefinder


class Extractor(ABC):
    @abstractmethod
    def extract(self, note):
        pass

    @abstractmethod
    def get_name(self):
        pass

class DateExtractor(Extractor):

    def extract(self, note):
        try:
            matches = datefinder.find_dates(note.text, source=True, base_date=datetime(1,1,1,0,0,0))
            return [match[1] for match in matches if self.__filter(match[0], match[1])]
        except:
            return []

    def get_name(self):
        return "dates"

    def __filter(self, date, original):
        if len(original) <= 3:
            return False
        if date.month == 1 and date.day == 1:
            return False
        return True

class NameExtractor(Extractor):

    def extract(self, note):
        try:
            matches = pos_tag(note.text.split())
            return [match[0] for match in matches if self.__filter(match[0], match[1])]
        except:
            return []

    def get_name(self):
        return "names"

    def __filter(self, word, wordType):
        if wordType != 'NNP':
            return False
        return True
