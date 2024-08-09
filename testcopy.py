import os
import shutil

source_folder = "C:/Users/adebb/source_folder"
destination_folder = "C:/Users/adebb/destination_folder"

extension = ".csv"

for folders, subfolders, filenames in os.walk(source_folder):

    for filename in filenames:

        if filename.endswith('{}'.format(extension)):

            shutil.move(os.path.join(folders,filename), destination_folder)
        print("file succesfully moved")
