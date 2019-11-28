from contextlib import contextmanager

import cv2
import pytesseract


@contextmanager
def get_capturer(video_file):
    cap = cv2.VideoCapture(video_file)
    try:
        yield cap
    finally:
        cap.release()


def get_frames(video_file):
    with get_capturer(video_file) as cap:
        while True:
            success, frame = cap.read()
            if success:
                yield frame
            else:
                break


def get_frame_ocr_data(frame):
    return pytesseract.image_to_data(frame, output_type=pytesseract.Output.DICT)


def get_frame_ocr_string(frame):
    return pytesseract.image_to_string(frame)


def get_end_credit(video_file):
    frames = get_frames(video_file)
    # Only capture the last 10%
    # The video is 24 fps
    frame = next(frames)
    print(pytesseract.get_frame_ocr_data(frame))
