from statistics import mode
import dropbox
import os

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        
        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'ldGJz3E-2QMAAAAAAAAAAe7onCr4orvBgEIv7q7JJxe5YjzpbfAERJQvAdMz3OfK'
    transferData = TransferData(access_token)

    file_from = input('Enter the file path to transfer: ')
    file_to = input('Enter the dropbox path to transfer to: ')

    for roots, dirs, files in os.walk(file_from):
        for file in files:
            relative_path = os.path.relpath(file, file_from)
            dropboxpath = os.path.join(file_to, relative_path)
            transferData.upload_file(os.path.join(roots, file), dropboxpath)

    # transferData.upload_file(file_from, file_to)
    # print("File transfer has been completed, thank you!")    


if __name__ == '__main__':
    main()
