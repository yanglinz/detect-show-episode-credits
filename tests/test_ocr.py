import pathlib

from PIL import Image

from src import detect


def get_frame_image_fixture(name):
    path = pathlib.Path(__file__).parent / "frames" / name
    return str(path)


def test_ocr():
    frame = get_frame_image_fixture("credit-1.png")
    data = detect.get_frame_ocr_data(frame)
    assert data
