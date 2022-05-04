import os
import zipfile

def get_files(source_path, target_path):
    for filepath,dirnames,filenames in os.walk(source_path):
        for filename in filenames:
            file = os.path.join(filepath,filename)
            f = zipfile.ZipFile(file, 'r')
            f.extractall(path=target_path)
            f.close()
            print('done:',file)
def main():
    target_path = '/home/cike/REVERIE/Matterport/v1/scans'
    source_path = '/home/cike/REVERIE/data/v1/scans'
    get_files(source_path, target_path)

if __name__ == "__main__": main()
