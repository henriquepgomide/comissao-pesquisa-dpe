import os
import zipfile
import re


def unzip_files(path, destination):
    """
    Extract all zip files inside a path to a given
    destination

    Parameters
    path - folder where files sit
    destination - where you want to save files
    """
    # Create folder to store raw text
    if not os.path.exists(destination):
        os.makedirs(destination)

    # Extract files
    files = os.listdir(path)
    files = [path+file for file in files]
    for file in files:
        if file.endswith('.zip'):
            with zipfile.ZipFile(file, 'r') as zip_ref:
                zip_ref.extract(zip_ref.filelist[0].filename, destination)
                os.rename(os.path.join(destination, zip_ref.filelist[0].filename),
                        os.path.join(destination, re.sub('\\D', '', file) + '.xml'))

