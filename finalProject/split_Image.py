import os
import imageio
import pandas as pd 


Imagefileinput = r'./images/'
output_directory = r'../finalProject/'
image_df = pd.read_csv('Image_labels.csv')

Image_Bening = image_df[image_df['PathologyClassification'] == 'Benign']
Image_Normal  = image_df[image_df['PathologyClassification'] == 'Normal']
Image_Malignant = image_df[image_df['PathologyClassification'] == 'Malignant']

os.makedirs(os.path.join(output_directory, 'Benign'), exist_ok=True)
os.makedirs(os.path.join(output_directory, 'Normal'), exist_ok=True)
os.makedirs(os.path.join(output_directory, 'Malignant'), exist_ok=True)

# Create directories if they don't exist
for i in list(Image_Malignant['Image_name']):
    f = []
    f.append(os.path.join(Imagefileinput, i + '.png'))
    image = imageio.imread(f.pop().replace(' ' , ''))
    imageio.imsave(os.path.join(output_directory, 'Malignant', i + '.png'), image)

for i in list(Image_Normal['Image_name']):
    f = []
    f.append(os.path.join(Imagefileinput, i + '.png'))
    image = imageio.imread(f.pop().replace(' ' , ''))
    imageio.imsave(os.path.join(output_directory, 'Normal', i + '.png'), image)

for i in list(Image_Bening['Image_name']):
    f = []
    f.append(os.path.join(Imagefileinput, i + '.png'))
    image = imageio.imread(f.pop().replace(' ' , ''))
    imageio.imsave(os.path.join(output_directory, 'Benign', i + '.png'), image)
