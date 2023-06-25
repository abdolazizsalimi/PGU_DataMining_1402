import numpy as np
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.utils import to_categorical

def custom_generator(filepaths, labels, datagen, batch_size):
    while True:
        # Shuffle the data at the beginning of each epoch
        indexes = np.random.permutation(len(filepaths))
        filepaths, labels = np.array(filepaths)[indexes], np.array(labels)[indexes]

        for start in range(0, len(filepaths), batch_size):
            end = min(start + batch_size, len(filepaths))
            batch_filepaths = filepaths[start:end]
            batch_labels = labels[start:end]

            batch_images = []
            for filepath in batch_filepaths:
                img = load_img(filepath, target_size=(512, 512))
                img_array = img_to_array(img)
                batch_images.append(img_array)

            batch_images = np.array(batch_images)
            batch_labels = to_categorical(batch_labels, num_classes=3)

            # Apply the datagen transformations to the batch of images
            for i, (img, label) in enumerate(datagen.flow(batch_images, batch_labels, batch_size=batch_size, shuffle=False)):
                yield img, label
                if i >= (len(batch_images) // batch_size):
                    break