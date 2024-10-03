import cv2

# 이미지 경로 및 라벨 파일 경로
image_path = r'C:\yolov10-main\ultralytics\cfg\final_1\train\images\00000150.jpg'
label_path = r'C:\yolov10-main\ultralytics\cfg\final_1\train\labels\00000150.txt'

# 이미지 읽기
image = cv2.imread(image_path)

# 라벨 파일 읽기
with open(label_path, 'r') as file:
    lines = file.readlines()

# 이미지에 라벨 좌표 그리기 (YOLO 포맷 기준: class, center_x, center_y, width, height)
for line in lines:
    class_id, cx, cy, w, h = map(float, line.split())

    # 좌표를 원래 이미지 스케일로 변환 (YOLO 포맷은 상대 좌표)
    img_h, img_w = image.shape[:2]
    cx, cy, w, h = cx * img_w, cy * img_h, w * img_w, h * img_h

    # 좌표를 사용하여 Bounding Box 그리기
    top_left = (int(cx - w / 2), int(cy - h / 2))
    bottom_right = (int(cx + w / 2), int(cy + h / 2))

    # 박스를 이미지에 그리기
    cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)

# 이미지 출력
cv2.imshow('Labeled Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
