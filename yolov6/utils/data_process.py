import os
import shutil
import random
from tqdm import tqdm


def random_select():
    root_dir = "../datasets/coco/images/"
    img_dir = root_dir + "val2017/"
    save_dir = root_dir + "calib_img/"
    os.makedirs(save_dir, exist_ok=True)
    img_names = os.listdir(img_dir)
    random.shuffle(img_names)
    for img_name in img_names[:1000]:
        shutil.copy(img_dir+img_name, save_dir+img_name)


if __name__ == "__main__":
    random_select()
