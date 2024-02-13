import gdown

DATA_URL = "https://drive.google.com/file/d/1EpDh7MyHzXbHNw_FYhbFijYipr2evc01/view?usp=sharing"


def download_data(url=DATA_URL):
    gdown.download(url, 'dataset.zip', fuzzy=True)
