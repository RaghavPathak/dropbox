import dropbox

class  TransferData :
    def __init__(self,access_token):
        self.access_token=access_token

    def upload_file(self, file_from,file_to):
        
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from,"rb")
        dbx.files_upload(f.read(),file_to)

def main():
    access_token="sl.BH0VxIplPaxcN4dqvjX_eSOuf9Z9uZvjMXVMnkN6_UJ1JKXECNMMCd8sRY59uGGVe9z4AndX_CIlzGkO-gFMHfCcmurfze6B4TdyY9ajZxwSdQZKXJ7LHq8KuXioRPMyUsIWMzw"
    transferData = TransferData(access_token)
    file_from=input("ENTER THE FILE PATH TO TRANSFER ")
    file_to=input("ENTER THE FILE PATH TO UPLOAD IT TO DROP BOX ")
    transferData.upload_file(file_from,file_to)
    print("FILE HAS BEEN MOVED :D")
main()


