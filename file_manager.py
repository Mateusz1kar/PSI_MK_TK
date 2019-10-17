class FileManager:
    def __init__(self, file_name):
        self.file_name=file_name

    def read_file(self):
        self.otworz=open(self.file_name)
        self.dane=self.otworz.read()
        return self.dane

    def update_file(self,text_data=""):
        self.otworz=open(self.file_name)
        self.otworz.write(text_data)
        self.otworz.close()
