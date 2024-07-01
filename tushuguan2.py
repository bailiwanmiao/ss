import cv2
import numpy as np

# 读取图像
image = cv2.imread('IMG20240614164102.jpg')

# 确保图像已正确读取
if image is None:
    print("Error: Could not open or find the image")
    exit()

# 将图像从BGR转换到HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 定义绿色的HSV范围（根据图像实际情况调整）
lower_green = np.array([35, 100, 100])
upper_green = np.array([77, 255, 255])

# 创建一个二值图像，其中只有绿色区域被标记为白色
mask = cv2.inRange(hsv, lower_green, upper_green)

# 使用位操作将原始图像中的非绿色区域设置为黑色
# 这里我们用掩码来提取绿色区域，并将其放置在一张全黑的背景上
result = cv2.bitwise_and(image, image, mask=mask)

# 为了确保背景完全是黑色，我们可以将非绿色区域设置为0
result[mask == 0] = [0, 0, 0]

# 显示原始图像和只包含绿色标签的图像
cv2.imshow('Original Image', image)
cv2.imshow('Image with only Green Labels', result)

# 等待用户按键，然后关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()