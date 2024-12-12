import cv2
import numpy as np

# 全局变量
points = []
scale_factor = 0.3  # 缩放比例
original_img = None
path = 'img\\exp4\\original.jpg'


# 鼠标回调函数
def select_points(event, x, y, flags, param):
    global points, scale_factor, original_img
    if event == cv2.EVENT_LBUTTONDOWN:
        # 将点击坐标还原到原始图像的比例
        real_x = int(x / scale_factor)
        real_y = int(y / scale_factor)
        points.append((real_x, real_y))
        print(f"选中点: {real_x}, {real_y}")
        if len(points) == 4:
            warp_perspective()


def warp_perspective():
    global points, original_img
    # 目标矩形的尺寸（调整为所需的尺寸）
    width, height = 1000, 800
    pts1 = np.float32(points)
    pts2 = np.float32([[0, 0], [width, 0], [width, height], [0, height]])  # 拉伸到目标矩形
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    result = cv2.warpPerspective(original_img, matrix, (width, height))
    cv2.imwrite(path, result)
    cv2.imshow("Result", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 主函数
def main():
    global original_img, scale_factor
    # 读取原图
    original_img = cv2.imread(path)

    # 缩放图像用于显示
    resized_img = cv2.resize(original_img, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_AREA)

    # 打开窗口并设置鼠标回调
    cv2.imshow("Image", resized_img)
    cv2.setMouseCallback("Image", select_points)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
