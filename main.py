import glob
import os
import random

from PIL import Image

# 840
# 560


class SuccessImageGenerator:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def resize_image(self, image: Image) -> Image:
        """
        > Resize the image to 800x600 if the image is wider than it is tall, or 400x600 if the image is
        taller than it is wide, and then reduce the image by a factor of 2
        
        :param image: The image to be resized
        :type image: Image
        :return: The image is being returned.
        """
        if image.width > image.height:
            image = image.resize((800,600))
        elif image.width < image.height:
            image = image.resize((400,600))
        return image.reduce(2)

    def get_images_paths(self) -> list[str]:
        """
        It returns a list of all the image paths in the `images` directory
        :return: A list of all the image paths in the images folder.
        """
        all_image_paths = []
        file_types = ["jpg", "jpeg", "png", "gif"]
        for file_type in file_types:
            all_image_paths.extend(glob.glob(f"{os.getcwd()}/images" + f"**/*.{file_type}", recursive=True))
        return all_image_paths

    def create_success_image(self) -> None:
        """
        It creates a new image, then pastes a bunch of resized images from the images folder into it, then
        saves it as success.png
        """
        images_paths = self.get_images_paths()
        success_image = Image.new("RGB", (self.width, self.height), "white")
        for image_path in images_paths:
            image = Image.open(image_path)
            resized_image = self.resize_image(image)
            #TODO: make paste resized_image into first available empty space and if there is no space, place it anywhere
            success_image.paste(resized_image, (random.randint(0, WIDTH-resized_image.width), random.randint(0, HEIGHT-resized_image.height)))
        success_image.save("success.png")

if __name__ == "__main__":
    WIDTH = 1280
    HEIGHT = 720

    success_image_generator = SuccessImageGenerator(WIDTH, HEIGHT)
    success_image_generator.create_success_image()
