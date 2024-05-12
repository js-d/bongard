from PIL import Image
import os

def resize_images_in_folder(folder_path, new_size):
    for subdir, dirs, files in os.walk(folder_path):
        print(subdir)
        for file in files:
            if file.endswith(".png"):
                file_path = os.path.join(subdir, file)
                img = Image.open(file_path)
                img_resized = img.resize((new_size, new_size))
                img_resized.save(file_path)

if __name__ == "__main__":
    problems_folder = "problems"
    new_dimension = 500  # New width and height in pixels
    resize_images_in_folder(problems_folder, new_dimension)