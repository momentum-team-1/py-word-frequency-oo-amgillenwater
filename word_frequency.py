STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has',
    'he', 'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to',
    'were', 'will', 'with'
]


class FileReader:
    def __init__(self, filename):
        self.filename = filename
        self.passage = self.read_contents()

    def read_contents(self):
        """
        This should read all the contents of the file
        and return them as one string.
        """
        # raise NotImplementedError("FileReader.read_contents")
        open_file = open(self.filename)
        text = open_file.read()
        open_file.close()
        return text
        

class WordList:
    def __init__(self, text):
        self.words = text
        # self.extract = self.extract_words()

    def extract_words(self):
        """
        This should get all words from the text. This method
        is responsible for lowercasing all words and stripping
        them of punctuation--will not return
        """
        words = self.words.lower()
        separated_words = words.split()
        self.separated_words = separated_words

    def remove_stop_words(self):
        """
        Removes all stop words from our word list. Expected to
        be run after extract_words--will not return
        """
        new_list = []
        for word in self.separated_words:
            if not word in STOP_WORDS:
                new_list.append(word)
        self.new_list = new_list

    def get_freqs(self):
        """
        Returns a data structure of word frequencies that
        FreqPrinter can handle. Expected to be run after
        extract_words and remove_stop_words. The data structure
        could be a dictionary or another type of object.
        """
        freqs = {}
        for item in self.new_list:
            freqs[item] = freqs.get(item, 0) + 1
        return freqs


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
        sorted_word_freqs = sorted(self.freqs.items(),key=lambda seq: seq[1], reverse=True)
        words_to_display = [freq[0] for freq in sorted_word_freqs[:10]]
        longest_word_length = max([len(word) for word in words_to_display])
        for word, count in sorted_word_freqs[:10]:
            print(word.rjust(longest_word_length + 1), "|",
                str(count).ljust(4), "*" * count)

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
