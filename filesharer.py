from filestack import Client


class FileSharer:

    def __init__(self, file_path, api_key='AfH9ZhbyrQrC5RMpp1Otwz'):
        self.file_path = file_path
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.file_path)
        return new_filelink.url