import cv2
import numpy as np


def detect_deepfake(image):
    # Load image using OpenCV
    img = cv2.imread(image)

    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Use OpenCV's Laplacian algorithm to detect edges
    edges = cv2.Laplacian(gray, cv2.CV_64F)

    # Normalize the edges
    edges = cv2.normalize(edges, None, 0, 255, cv2.NORM_MINMAX)

    # Threshold the edges to create a binary image
    ret, thresh = cv2.threshold(edges, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Use OpenCV's Hough lines algorithm to detect lines in the image
    lines = cv2.HoughLinesP(thresh, 1, np.pi / 180, 50, minLineLength=50, maxLineGap=10)

    # Initialize variables to keep track of the number of lines
    horizontal_lines = 0
    vertical_lines = 0

    # Iterate through the lines and count the number of horizontal and vertical lines
    for line in lines:
        x1, y1, x2, y2 = line[0]
        if x1 == x2:
            vertical_lines += 1
        elif y1 == y2:
            horizontal_lines += 1

    # Calculate the ratio of horizontal to vertical lines
    ratio = horizontal_lines / vertical_lines

    # Check if the ratio is less than a certain threshold
    if ratio < 0.5:
        print("The image is likely to be deepfake")
    else:
        print("The image is likely to be authentic")
