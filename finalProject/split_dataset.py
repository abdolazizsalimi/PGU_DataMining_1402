import os
import glob
import shutil
import random
# This function will create a folder structure with train and validation subdirectories for each class in the target_dir. The data will be split based on the specified train_ratio (default is 0.8 or 80% for training). You can adjust the train_ratio parameter as needed.

# After running this function, you can use the ImageDataGenerator as described in previous responses to load and preprocess the images for your CNN model.

def split_dataset(source_dirs, target_dir, train_ratio=0.7, val_ratio=0.15, test_ratio=0.15):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    for class_dir in source_dirs:
        class_name = os.path.basename(class_dir)
        class_images = glob.glob(os.path.join(class_dir, '*.png'))  # Adjust the file extension if needed
        random.shuffle(class_images)
        
        train_size = int(len(class_images) * train_ratio)
        val_size = int(len(class_images) * val_ratio)
        
        train_images = class_images[:train_size]
        val_images = class_images[train_size:(train_size + val_size)]
        test_images = class_images[(train_size + val_size):]
        
        for dest, images in [('train', train_images), ('val', val_images), ('test', test_images)]:
            dest_dir = os.path.join(target_dir, dest, class_name)
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            
            for image in images:
                shutil.copy(image, dest_dir)




source_dirs = ['./Benign/', './Malignant/', './Normal/']
target_dir = './split_dataset'
split_dataset(source_dirs, target_dir)