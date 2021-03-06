import os
import cv2
from base_camera import BaseCamera

class Camera(BaseCamera):
    video_source = 0

    def __init__(self):
        if os.environ.get('OPENCV_CAMERA_SOURCE'):
            Camera.set_video_source(int(os.environ['OPENCV_CAMERA_SOURCE']))
        super(Camera, self).__init__()

    # @staticmethod
    def set_video_source(source):
        Camera.video_source = source

    # @staticmethod
    def frames():
        camera = cv2.VideoCapture(Camera.video_source)
        camera.set(3, 720)
        camera.set(4, 540)
        Camera.video_size =  (
                    int(camera.get(cv2.CAP_PROP_FRAME_WIDTH)),
                    int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
                )
        Camera.video_fps = camera.get(cv2.CAP_PROP_FPS)
        print("video_size: ", Camera.video_size)
        print("Video_fps: ", Camera.video_fps)
        width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
        print("********************************height = {}, width = {}".format(width, height))
        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')

        while True:
            # read current frame
            _, img = camera.read()
            
            # encode as a jpeg image and return it
            # yield cv2.imencode('.jpg', img)[1].tobytes()
            yield img
