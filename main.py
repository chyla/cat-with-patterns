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

print("params:", sys.argv)

files_to_open = sys.argv[1:]

print("files_to_open;", files_to_open)

if len(files_to_open) > 0:
    reader = FileReader(files_to_open[0])
else:
    reader = ConsoleReader()

while not reader.eof:
    text = reader.readline()
    print(text)

reader.close()
