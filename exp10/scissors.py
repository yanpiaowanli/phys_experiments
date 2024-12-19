import cv2
import numpy as np

# Global variables
points = []
scale_factor = 0.5  # Scaling factor
original_img = None


def select_points(event, x, y, flags, param):
    global points, scale_factor, original_img
    if event == cv2.EVENT_LBUTTONDOWN:
        # Restore the click coordinates to the original image scale
        real_x = int(x / scale_factor)
        real_y = int(y / scale_factor)
        points.append((real_x, real_y))
        print(f"Selected point: {real_x}, {real_y}")
        if len(points) == 4:
            warp_perspective(param)


def warp_perspective(path):
    global points, original_img
    # Target rectangle size (adjust as needed)
    width, height = 1000, 800
    pts1 = np.float32(points)
    pts2 = np.float32([[0, 0], [width, 0], [width, height], [0, height]])  # Stretch to target rectangle
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    result = cv2.warpPerspective(original_img, matrix, (width, height))
    cv2.imwrite(path, result)
    cv2.imshow("Result", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Main function
def cut(path):
    global original_img, scale_factor, points
    points = []
    # Read the original image
    original_img = cv2.imread(path)

    # Resize the image for display
    resized_img = cv2.resize(original_img, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_AREA)

    # Open window and set mouse callback
    cv2.imshow("Image", resized_img)
    cv2.setMouseCallback("Image", select_points, path)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
