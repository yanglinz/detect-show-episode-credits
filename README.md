# Detect Video End Credits

This a hack-day experiment to programmatically detect the approximate timestamp
of the end credits for a given video.

The end credit is a particularly useful timestamp for video players to show
additional content in the UI. For example, Netflix will displays a piece of UI
to navigate to the next episode when the end credits starts playing for the
current video.

## Dependencies

This demo takes advantage of the following core dependencies.

- [OpenCV](https://opencv.org/) - video analysis
- [Tesseract](https://github.com/tesseract-ocr/tesseract) - optical character
  recognition

## Approach

The rough approach is to:

1. Capture frames for the video for some interval e.g. 1 frame per second
2. Place a score on each frame for how likely it is a end credit frame
3. Analyze the pattern of scores to determine the beginning of the end credit

## Heuristics

To score the likelihood that a given frame is a end credit frame, we can use the
following heuristics.

1. Whether certain keywords are present. e.g. `"Produced By"`, `"Director"`,
   `"Dolby"`.
2. How many lines of text are present or text density end credit screen likely
   contain dense text count.
3. The background color of the frame since end credit screen are often (though
   not always) black.
