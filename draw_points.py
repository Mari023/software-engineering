import numpy as np
import cv2


def create_cicle_points(img_size, r_sq):
    theta = np.linspace(0, 2 * np.pi, 100)
    r = np.sqrt(r_sq)
    x1 = r * np.cos(theta)
    x2 = r * np.sin(theta)
    pts = np.stack([x1, x2]).transpose()
    center = int(img_size / 2)
    pts1 = np.array([center, center]) + pts * center
    return pts1


def draw_points(points, img_size):
    img = np.zeros((img_size, img_size, 3), np.uint8)
    for point in points:
        cv2.circle(img, (int(point[0]), int(point[1])), 5, (255, 255, 0), -1)
    return img


img_size = 512
r_sq = 0.7

pts1 = create_cicle_points(img_size, r_sq)
img = draw_points(pts1, img_size)

cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
cv2.imshow('image', img)
cv2.waitKey()
