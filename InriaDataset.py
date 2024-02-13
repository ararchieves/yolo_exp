import os
import numpy as np
import torch

from torch.utils.data import Dataset, DataLoader
from torchvision.io import read_image, ImageReadMode


class InriaDataset(Dataset):
    def __init__(self, base_dir='.', transform=None):
        super().__init__()
        self.image_dir = os.path.join(base_dir, 'images')
        self.house_dir = os.path.join(base_dir, 'labels', 'houses')
        self.block_dir = os.path.join(base_dir, 'labels', 'blocks')

        self.image_files = os.listdir(self.image_dir)
        self.transform = transform
        
    def __len__(self):
        return len(self.image_files)

    def __getitem__(self, idx):
        filename = self.image_files[idx].replace('.png', '')

        image = read_image(os.path.join(self.image_dir, filename + '.png'), mode=ImageReadMode.RGB) / 255
        
        # Read house Annotations 
        house_anno = []
        with open(os.path.join(self.house_dir, filename + '.txt'), 'r') as f:
            house_anno = f.readlines()

        blocks_anno = []
        # Read Block Annotations
        with open(os.path.join(self.block_dir, filename + '.txt'), 'r') as f:
            blocks_anno = f.readlines()

        # Process House and Block annotations
        house_anno = np.array([ann.split() for ann in house_anno], dtype=np.float32)
        blocks_anno = np.array([ann.split() for ann in blocks_anno], dtype=np.float32)

        # Apply image transforms
        if self.transform:
            image = self.transform(image)

        return image, house_anno, blocks_anno
    
    @staticmethod
    def collate_fn(batch):
        im, house_anno, blocks_anno  = zip(*batch)
        return torch.stack(im, 0), house_anno, blocks_anno



if __name__ == "__main__":
    import matplotlib.pyplot as plt
    
    ds = InriaDataset()
    dl = DataLoader(ds, batch_size=2, shuffle=False, collate_fn=ds.collate_fn)

    batch = next(iter(dl))
    images, houses, blocks = batch

    idx = 0
    image = images[idx]
    house = houses[idx]
    block = blocks[idx]

    fig, ax = plt.subplots(1, 2, figsize=(15, 20))

    ax[0].imshow(image.permute(1,2,0))
    ax[0].set_title("Houses")
    for item in house:
        points = item[1: -1].reshape(-1, 2) * 1000
        ax[0].scatter(points[:, 0], points[:, 1])

    ax[1].set_title("House Blocks")
    ax[1].imshow(image.permute(1,2,0))
    for item in block:
        points = item[1:].reshape(-1, 2) * 1000
        ax[1].scatter(points[:, 0], points[:, 1], s=100)

    plt.show()
