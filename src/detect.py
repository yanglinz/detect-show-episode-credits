import cv2


def get_frames(video_file):
    cap = cv2.VideoCapture(video_file)
    while(True):
        has_frame, frame = cap.read()
        print(frame)
        if not has_frame:
            break


def get_end_credit(video_file):
    frames = get_frames(video_file)
