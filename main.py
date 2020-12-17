from PIL import Image


def merge_two_images(image1_location, image2_location):
    image1 = Image.open(image1_location)
    image2 = Image.open(image2_location)
    image1_size = image1.size
    image2_size = image2.size
    image2.paste(image1, (0, 0), image1)
    image2.show()


merge_two_images("image1.png", "image2.jpeg")