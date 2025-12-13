import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os
import kaggle

def download_fashion_mnist():
    data_path = "data"
    if not os.path.exists(data_path):
        os.makedirs(data_path)
    
    print("Downloading Fashion MNIST from Kaggle...")
    # This downloads the specific dataset your team chose
    kaggle.api.dataset_download_files(
        'zalando-research/fashionmnist', 
        path=data_path, 
        unzip=True
    )
    print("Download complete. Files are in the /data folder.")

if __name__ == "__main__":
    download_fashion_mnist()



