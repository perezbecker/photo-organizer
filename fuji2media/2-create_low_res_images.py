import os  
from PIL import Image, ExifTags  
  
def create_low_res_images(input_dir, output_dir, scale_factor=0.3):  
    if not os.path.exists(output_dir):  
        os.makedirs(output_dir)  
  
    for filename in os.listdir(input_dir):  
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):  
            img = Image.open(os.path.join(input_dir, filename))  
  
            # Get orientation from exif data  
            for orientation in ExifTags.TAGS.keys():  
                if ExifTags.TAGS[orientation] == 'Orientation':  
                    break  
  
            try:  
                exif = dict(img._getexif().items())  
                if exif[orientation] == 3:  
                    img = img.rotate(180, expand=True)  
                elif exif[orientation] == 6:  
                    img = img.rotate(270, expand=True)  
                elif exif[orientation] == 8:  
                    img = img.rotate(90, expand=True)  
            except (AttributeError, KeyError, IndexError):  
                # Cases: image don't have getexif  
                pass  
  
            low_res_img = img.resize((int(img.width * scale_factor), int(img.height * scale_factor)), Image.ANTIALIAS)  
            low_res_img.save(os.path.join(output_dir, filename))  
  
if __name__ == "__main__":  
    input_directory = "./photos"  
    output_directory = "./low_res_photos"  
    create_low_res_images(input_directory, output_directory)  