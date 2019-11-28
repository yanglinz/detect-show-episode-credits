from contextlib import contextmanager

import cv2


@contextmanager
def get_capturer(video_file):
    cap = cv2.VideoCapture(video_file)
    try:
        yield cap
    finally:
        cap.release()


def get_frames(video_file):
    with get_capturer(video_file) as cap:
        while(True):
            success, frame = cap.read()
            if success:
                yield frame
            else:
                break


def get_end_credit(video_file):
    frames = get_frames(video_file)
    # Only capture the last 10%
    # The video is 24 fps
    length = sum(1 for i in frames)
    print(length)
