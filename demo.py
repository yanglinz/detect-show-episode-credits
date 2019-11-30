from src import detect

if __name__ == "__main__":
    demo_video = "assets/big-buck-bunny.mp4"
    result = detect.get_end_credit(demo_video)
    print(result)
