from contextlib import contextmanager
from dataclasses import dataclass
import typing

import cv2
import pytesseract
import structlog

logger = structlog.get_logger()


@dataclass
class FrameMeta:
    data: typing.Any
    frame_num: int
    frame_position_seconds: int

    @property
    def text(self):
        return get_frame_ocr_string(self.data)

    @property
    def credit_likeliness(self):
        text = self.text

        # See if there are some keywords
        likely_text = ("director", "directed by", "produced", "produced by", "producer")
        for lt in likely_text:
            if lt in text:
                return 1

        # See if there's lots of text
        hight_text_density = len(text) > 150
        if hight_text_density:
            return 1

        return 0


def get_frame_ocr_data(image_data):
    return pytesseract.image_to_data(image_data, output_type=pytesseract.Output.DICT)


def get_frame_ocr_string(image_data):
    return pytesseract.image_to_string(image_data)


@contextmanager
def get_capturer(video_file):
    cap = cv2.VideoCapture(video_file)
    try:
        yield cap
    finally:
        cap.release()


def get_captured_frames(video_file):
    with get_capturer(video_file) as cap:
        while True:
            success, frame = cap.read()
            if success:
                yield frame
            else:
                break


def get_relevant_frames(video_file):
    duration = None
    frame_count = None
    fps = None
    logger.info("analyzing video metadata")
    with get_capturer(video_file) as cap:
        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        duration = frame_count / fps
        logger.info(
            "analyzed video metadata",
            fps=fps,
            frame_count=frame_count,
            duration=duration,
        )

    frame_threshold = frame_count * 0.7
    for i, f in enumerate(get_captured_frames(video_file)):
        # We only care about the last 30% of the video since
        # that's where the credit is most likely located
        if i < frame_threshold:
            continue

        # We only capture one second at a time
        if i % int(fps) != 0:
            continue

        frame = FrameMeta(data=f, frame_num=i, frame_position_seconds=i / fps)
        yield frame


def get_end_credit(video_file):
    frames = get_relevant_frames(video_file)

    end_credit_timestamp = None
    score_threshold = 0.8
    for f in frames:
        score = f.credit_likeliness
        logger.info(
            "analyzing video frame",
            frame_num=f.frame_num,
            frame_position_seconds=f.frame_position_seconds,
            score=score,
        )
        if score > score_threshold and not end_credit_timestamp:
            end_credit_timestamp = f.frame_position_seconds

    return end_credit_timestamp
