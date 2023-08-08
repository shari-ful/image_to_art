import os
import cv2
from dataclasses import dataclass


@dataclass
class ArtImage:
    img_path: str = None
    name: str = ""

    def input_image(self, path):

        self.img_path = path
        filename = os.path.basename(path)
        self.name = os.path.splitext(filename)[0]   
        image = cv2.imread(self.img_path)

        return image

    def gray_image(self, image):

        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        return gray_image

    def invert_image(self, g_img):

        inverted_image = 255 - g_img

        return inverted_image

    def pencil_sketch(self, path):

        input_image = self.input_image(path)
        gray_image = self.gray_image(input_image)
        inverted_image = self.invert_image(gray_image)

        blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)

        inverted_blurred = 255 - blurred
        pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
        cv2.imshow(f"Sketch_{self.name}", pencil_sketch)
        key = cv2.waitKey(0)
        if key == 27:
            cv2.destroyAllWindows() 



sketch = ArtImage()
sketch.pencil_sketch("images/dog.png")