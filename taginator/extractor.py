from abc import ABC, abstractmethod
import nltk
nltk.download('averaged_perceptron_tagger', quiet=True)
nltk.download('punkt', quiet=True)
from nltk.tag import pos_tag
from datetime import datetime
from gensim.summarization import keywords
from gensim.summarization.summarizer import summarize
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

    def extract_datetime(self, note):
        try:
            matches = datefinder.find_dates(note.text, source=True, base_date=datetime(1, 1, 1, 0, 0, 0))
            return {match[0]:match[1] for match in matches if self.__filter(match[0], match[1])}
        except:
            return []

class NameExtractor(Extractor):

    def extract(self, note):
        try:
            matches = pos_tag(note.text.split())
            return list(set([match[0] for match in matches if self.__filter(match[0], match[1])]))
        except:
            return []

    def get_name(self):
        return "names"

    def __filter(self, word, wordType):
        if wordType != 'NNP':
            return False
        return True

class TagExtractor(Extractor):

    def get_name(self):
        return "tag"

    def extract(self, note):
        tag_list = keywords(note.text).split('\n')
        ret_list = []
        for tag in tag_list:
            tmp = tag.split(' ')
            for s in tmp:
                ret_list.append(s)
                if s[-1] == 's':
                    if s[-3:-1] == 'ie':
                        sing = s[:-3] + 'y'
                        ret_list.append(sing)
                    else:
                        sing = s[:-1]
                        ret_list.append(sing)
        ret_list = list(set(ret_list))
        return ret_list

class SummaryExtractor(Extractor):

    def get_name(self):
        return "summary"

    def extract(self, note):
        return summarize(note.text)