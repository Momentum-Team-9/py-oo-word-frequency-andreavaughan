from collections import Counter

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has',
    'he', 'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to',
    'were', 'will', 'with'
]


class FileReader:
    def __init__(self, filename):
        self.filename = filename

    def read_contents(self):
        """
        This should read all the contents of the file
        and return them as one string.
        """
        with open(self.filename) as file:
            words = file.readlines()
            stringed_text = ""
            return stringed_text.join(words)


class WordList:
    def __init__(self, text):
        self.text = text
        self.extracted_words = ""
        self.stop_free_words = ""

    def extract_words(self):
        """
        This should get all words from the text. This method
        is responsible for lowercasing all words and stripping
        them of punctuation.
        """
        lowercase_text = self.text.lower().replace("\n", " ").replace("’s", "")
        letters_and_space = "abcdefghijklmnopqrstuvwxyz "
        extracted_words = ""
        for char in lowercase_text:
            if char in letters_and_space:
                extracted_words += char
        print(type(extracted_words))
        self.extracted_words = extracted_words

    def remove_stop_words(self):
        """
        Removes all stop words from our word list. Expected to
        be run after extract_words.
        """
        text_list = self.extracted_words.split(" ")
        self.stop_free_words = ([word for word in text_list if word not in STOP_WORDS])

    def get_freqs(self):
        """
        Returns a data structure of word frequencies that
        FreqPrinter can handle. Expected to be run after
        extract_words and remove_stop_words. The data structure
        could be a dictionary or another type of object.
        """
        print(Counter(self.stop_free_words))
        return Counter(self.stop_free_words)


class FreqPrinter:
    def __init__(self, freqs):
        self.freqs = freqs

    def print_freqs(self):
        """
        Prints out a frequency chart of the top 10 items
        in our frequencies data structure.

        Example:
          her | 33   *********************************
        which | 12   ************
          all | 12   ************
         they | 7    *******
        their | 7    *******
          she | 7    *******
         them | 6    ******
         such | 6    ******
       rights | 6    ******
        right | 6    ******
        """
        for word, count in sorted(self.freqs.items(), key=lambda seq: seq[1], reverse=True):
            print(f"{word:2} {' | ' 'center_alignment' : ^10} {count:2}")


if __name__ == "__main__":
    import argparse
    import sys
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        reader = FileReader(file)
        word_list = WordList(reader.read_contents())
        word_list.extract_words()
        word_list.remove_stop_words()
        printer = FreqPrinter(word_list.get_freqs())
        printer.print_freqs()
    else:
        print(f"{file} does not exist!")
        sys.exit(1)
