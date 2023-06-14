# output_directory = './images/'
# for filename in os.listdir(image_directory):
#     # Construct the file paths
#     input_file = os.path.join(image_directory, filename)
    
#     image = imageio.imread(input_file)
    
#     # Resize the image using skimage.transform.resize
#     resized_image = transform.resize(image, output_size)
#     new_name = f"{filename[:-4]}"
#     output_file = os.path.join(output_directory, new_name + '.png')
#     imageio.imsave(output_file, resized_image)