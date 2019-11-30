#!/usr/bin/env python3

from src import detect

if __name__ == "__main__":
    demo_video = "assets/big-buck-bunny.mp4"
    result = detect.get_end_credit(demo_video)
    print("\n\n")
    print("video end credit start timestamp:", result)
