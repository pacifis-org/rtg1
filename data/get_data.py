import os
import pandas as pd
import urllib.request
from kaggle.api.kaggle_api_extended import KaggleApi


def main():
    # We assume that the kaggle.json file is in the ~/.kaggle directory
    api = KaggleApi()
    api.authenticate()

    dataset_owner = "nikhilnayak123"
    dataset_name = "5-million-song-lyrics-dataset"
    download_path = os.path.dirname(
        os.path.realpath(__file__)
    )  # directory that this script is in

    api.dataset_download_files(
        f"{dataset_owner}/{dataset_name}", path=download_path, quiet=False
    )

    # One of our language models needs these files
    print("Downloading language model...")
    urllib.request.urlretrieve(
        "https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin",
        os.path.join(download_path, "lid.176.bin"),
    )

    if not os.path.isfile("ds2_toy.csv"):
        print("Creating toy dataset...")
        pd.read_csv(
            os.path.join(download_path, "5-million-song-lyrics-dataset.zip"),
            nrows=500000,
        ).to_csv(os.path.join(download_path, "ds2_toy.csv"), index=False)

        os.remove(os.path.join(download_path, "5-million-song-lyrics-dataset.zip"))


if __name__ == "__main__":
    main()
