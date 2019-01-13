import cv2

class Image:

    def __init__(self, path):
        self.path = path
        self.img = cv2.imread(self.path)
    
    def load_image_rgb(self):
        """
        RGB Channels
        """
        self.img = cv2.imread(self.path, 1)
        return self.img
    
    def load_image_bw(self):
        """
        Black and White Channels
        """
        self.img = cv2.imread(self.path, 0)
        return self.img

    def load_image_alpha(self):
        """
        Transparency Properties
        """
        self.img = cv2.imread(self.path, -1)
        return self.img

    def get_dimensions(self):
        return self.img.ndim
    
    def get_shape(self):
        return self.img.shape
    
    def show_image(self, time, window_name):
        cv2.imshow(window_name, self.img)
        cv2.waitKey(time)
        cv2.destroyAllWindows()

    def resize_image(self, resolution, time, window_name):
        resized_image = cv2.resize(self.img, resolution)
        cv2.imshow(window_name, resized_image)
        cv2.waitKey(time)
        cv2.destroyAllWindows()


