import numpy as np
import cv2
import time

# Camera feed class to start and connect cameras for the main GUI
class camera:
    def __init__(self, index):
        self.index = index
        # Default camera parameters 1080p 30fps 
        self.WIDTH = 1920
        self.HEIGHT = 1080
        self.FPS = 30

        self.camera = cv2.VideoCapture(0)
        self.prev_coord = np.zeros((4, 2), np.float32)
        self.warning_sign = cv2.imread("/Users/cheruichang/Desktop/aruco_a3.jpg")
        self.ison = True

    # Returns an image from the camera
    def get_image(self):
        try:
            if self.Opened():
                ret_bench, image = self.camera.read()
            else:
                return None
            if not ret_bench:
                print("Bench frame has not been read")
                return None
            else:
                return image
        except Exception as e:
            print(e)

    # Releases camera stream 
    def close_camera(self):
        try:
            self.camera.release()
            self.ison = False
        except Exception as e:
            print(e)
    
    # Check if camera stream is opened 
    def Opened(self):
        try:
            return self.ison
        except Exception as e:
            print(e)
            return False
