from PyQt5.QtCore import pyqtSignal, QThread
from camera_feed import camera
import datetime
import numpy as np
import time
import cv2
import detect_custom


# Default thread (Sleep mode) - Streams bench camera feed 
class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)

    def __init__(self):
        super().__init__()
        self._run_flag = True
        self.camera = camera(0)
        self.WIDTH = 1920
        self.HEIGHT = 1080
    
    # Update signals for GUI
    update_info = pyqtSignal(int)
    update_coord = pyqtSignal(list)
    finished = pyqtSignal()
    
    def run(self):
        try:
            while self._run_flag and self.camera.Opened():
                # Update instructions tab in main GUI window
                if self.camera.Opened():
                    cap = self.camera.get_image()  # Read in as 1920x1080p
                    # Image augmentation to crop out bench area
                    pred_img, bboxes = detect_custom.ann_image(cap[:, 280:1001])

                    self.change_pixmap_signal.emit(pred_img)
                    self.update_coord.emit(bboxes)
                    self.update_info.emit(len(bboxes))
        except Exception as e:
            # Open a txt file to record down any errors
            print(e)

    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        self._run_flag = False
        if self.camera.Opened():
            self.camera.close_camera()        
            time.sleep(0.5)
            print("Closing Bench camera from Default Thread...")
    
    def __del__(self):
        print("Closing Default Thread...")


