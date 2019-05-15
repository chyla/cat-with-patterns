import sys

class ConsoleReader:
    def __init__(self):
        self.eof = False

    def readline(self):
        return input()

    def close(self):
        pass

class FileReader:
    def __init__(self, file_name):
        self.input_file = open(file_name)
        self.eof = False   # eof -> End Of File

    def readline(self):
        text = self.input_file.readline()
        if text == '':
            self.eof = True
        if len(text) > 0 and text[-1] == '\n':
            text = text[:-1]
        return text

    def close(self):
        self.input_file.close()


class MultiReader:
    def __init__(self, readers):
        self.readers = readers
        self.eof = False
        self.index_to_read = 0

    def readline(self):
        text = self.readers[self.index_to_read].readline()

#        print("  DEBUG: index_to_read:", self.index_to_read)
#        print("  DEBUG: len(self.readers):", len(self.readers))
#        print("  DEBUG: self.readers[self.index_to_read].eof:", self.readers[self.index_to_read].eof)
#        print("  DEBUG: len(self.readers) - 1 > self.index_to_read:", len(self.readers) - 1 > self.index_to_read)

        if self.readers[self.index_to_read].eof and len(self.readers) - 1 > self.index_to_read:
            self.index_to_read += 1
        if self.readers[self.index_to_read].eof and len(self.readers) - 1 == self.index_to_read:
            self.eof = True

        return text

    def close(self):
        for reader in self.readers:
            reader.close()


# print("params:", sys.argv)

files_to_open = sys.argv[1:]

# print("files_to_open;", files_to_open)

if len(files_to_open) > 0:
    file_readers = []
    for file_name in files_to_open:
        file_reader = FileReader(file_name)
        file_readers.append(file_reader)

    reader = MultiReader(file_readers)
else:
    reader = ConsoleReader()

while not reader.eof:
    text = reader.readline()
    print(text)

reader.close()
