import os
import tarfile
import urllib.request

DOWNLOAD_ROOT = "DATA_ROOT_URL"
DATA_PATH = os.path.join("datasets", "data") # where data will be stored in your machine
DATA_URL = DOWNLOAD_ROOT + "PATH_TO_DATA"

def fetch_data(data_url=DATA_URL, data_path=DATA_PATH):
    '''It creates a datasets/data directory in your workspace, downloads a data.tgz file,
    and extracts the contents from it in this directory

    Parameters:
    data_url (str): data url
    data_path (str): path where data will be stored in your machine

    Returns:
    None

    Usage example:
    fetch_data("https://data.com", "/home/your-name/local-path")
    '''

    if not os.path.isdir(data_path):
        os.makedirs(data_path)
    tgz_path = os.path.join(data_path, "data.tgz")
    urllib.request.urlretrieve(data_url, tgz_path)
    data_tgz = tarfile.open(tgz_path)
    data_tgz.extractall(path=data_path)
    data_tgz.close()