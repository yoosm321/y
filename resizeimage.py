import cv2
import os

# 입력 이미지와 라벨이 있는 디렉토리 경로
#input_image_directory = r'C:\yolov10-main\ultralytics\cfg\final_ori\train\images'
#input_label_directory = r'C:\yolov10-main\ultralytics\cfg\final_ori\train\labels'
input_image_v_directory = r'C:\yolov10-main\ultralytics\cfg\final_ori\valid\images'
input_label_v_directory = r'C:\yolov10-main\ultralytics\cfg\final_ori\valid\labels'

# 리사이즈된 이미지를 저장할 출력 디렉토리 경로
#output_image_directory = r'C:\yolov10-main\ultralytics\cfg\final_1\train\images'
#output_label_directory = r'C:\yolov10-main\ultralytics\cfg\final_1\train\labels'
output_image_v_directory = r'C:\yolov10-main\ultralytics\cfg\final_1\valid\images'
output_label_v_directory = r'C:\yolov10-main\ultralytics\cfg\final_1\valid\labels'

# 출력 디렉토리가 없으면 생성
#os.makedirs(output_image_directory, exist_ok=True)
#os.makedirs(output_label_directory, exist_ok=True)
os.makedirs(output_image_v_directory, exist_ok=True)
os.makedirs(output_label_v_directory, exist_ok=True)

# 입력 디렉토리의 모든 이미지 파일에 대해 반복
for filename in os.listdir(input_image_v_directory):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # 이미지 읽기
        image_path = os.path.join(input_image_v_directory, filename)
        image = cv2.imread(image_path)

        if image is None:
            print(f"{filename} 이미지를 읽을 수 없습니다. 경로를 확인하세요.")
            continue

        # 이미지 크기 리사이즈
        original_height, original_width = image.shape[:2]
        resized_image = cv2.resize(image, (640, 640))

        # 리사이즈된 이미지 저장
        cv2.imwrite(os.path.join(output_image_v_directory, f'{filename}'), resized_image)

        # 라벨 파일 처리
        label_filename = filename.rsplit('.', 1)[0] + '.txt'
        label_path = os.path.join(input_label_v_directory, label_filename)

        if os.path.exists(label_path):
            with open(label_path, 'r') as label_file:
                lines = label_file.readlines()

            with open(os.path.join(output_label_v_directory, f'{label_filename}'), 'w') as output_label_file:
                for line in lines:
                    parts = line.strip().split()
                    class_id = parts[0]  # 클래스 ID
                    x_center = float(parts[1]) * original_width  # 원본 이미지의 중심 x
                    y_center = float(parts[2]) * original_height  # 원본 이미지의 중심 y
                    width = float(parts[3]) * original_width  # 원본 이미지의 너비
                    height = float(parts[4]) * original_height  # 원본 이미지의 높이

                    # 리사이즈 후 새로운 중심 좌표 및 크기 계산
                    new_x_center = x_center * (640 / original_width)
                    new_y_center = y_center * (640 / original_height)
                    new_width = width * (640 / original_width)
                    new_height = height * (640 / original_height)

                    # 새로운 라벨 파일에 작성 (YOLO 형식)
                    output_label_file.write(f"{class_id} {new_x_center / 640} {new_y_center / 640} {new_width / 640} {new_height / 640}\n")

print("모든 이미지와 라벨이 성공적으로 리사이즈되었습니다.")
