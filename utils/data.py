import os
import gdown
import shutil


INRIA_DATA_URL = "https://drive.google.com/file/d/1EpDh7MyHzXbHNw_FYhbFijYipr2evc01/view?usp=sharing"
DHA_DATA_URL = "https://drive.google.com/file/d/1ltD-F7jYFIbxecge-eQIOqOiAKbFSPH9/view?usp=sharing"

def download_dataset(data='inria'):
    data = data.lower()
    assert data in ['inria', 'dha'], f"Dataset {data} is not valid."

    if data == 'inria': url = INRIA_DATA_URL
    elif data == 'dha': url = DHA_DATA_URL

    gdown.download(url, 'dataset.zip', fuzzy=True) # Donwload Dataset
    print("Unzipping!")
    shutil.unpack_archive('dataset.zip', '.') # unzip dataset
    os.remove('dataset.zip') # Remove the dataset file
    print("Setup Complete!")
