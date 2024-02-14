import os
import gdown
import shutil

DATA_URL = "https://drive.google.com/file/d/1EpDh7MyHzXbHNw_FYhbFijYipr2evc01/view?usp=sharing"


def download_dataset(url=DATA_URL):
    gdown.download(url, 'dataset.zip', fuzzy=True) # Donwload Dataset
    shutil.unpack_archive('dataset.zip', '.') # unzip dataset
    os.remove('dataset.zip') # Remove the dataset file
