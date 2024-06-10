from zipfile import ZipFile

class FileHelper:
    @staticmethod
    def read_file(path: str):
        text_file = open(path, "r")

        lines = text_file.readlines()
        text_file.close()

        return lines

    @staticmethod
    def write_to_file(path: str, text: str):
        text_file = open(path, "w")

        text_file.writelines(text)
        text_file.close()
    
    @staticmethod
    def compress_to_zip(self, path: str, zip_path: str):
        with ZipFile(zip_path, 'w') as zip:
            zip.write(path)

# Path: main.pyd