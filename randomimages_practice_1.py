import os
import shutil
import random


#random으로 valid, train파일 분류
# 원본 데이터셋 경로
image_source_dir = r'C:\Users\yseun\Desktop\tld_db\train\images'
label_source_dir = r'C:\Users\yseun\Desktop\tld_db\train\labels'

# train과 valid 폴더 경로
train_image_dir = r'C:\yolov10-main\ultralytics\cfg\final_ori\train\images'
valid_image_dir = r'C:\yolov10-main\ultralytics\cfg\final_ori\valid\images'
train_label_dir = r'C:\yolov10-main\ultralytics\cfg\final_ori\train\labels'
valid_label_dir = r'C:\yolov10-main\ultralytics\cfg\final_ori\valid\labels'


# 폴더 생성 (이미지 및 라벨 폴더)
os.makedirs(train_image_dir, exist_ok=True)
os.makedirs(valid_image_dir, exist_ok=True)
os.makedirs(train_label_dir, exist_ok=True)
os.makedirs(valid_label_dir, exist_ok=True)

# 이미지 파일 리스트 불러오기
image_files = [f for f in os.listdir(image_source_dir) if f.endswith('.jpg')]

# 8:2 비율로 나누기
random.shuffle(image_files)
train_split = int(0.8 * len(image_files))
train_files = image_files[:train_split]
valid_files = image_files[train_split:]

# 이미지 파일 및 라벨 파일 복사
for file in train_files:
    # 이미지 복사
    shutil.copy(os.path.join(image_source_dir, file), os.path.join(train_image_dir, file))
    # 동일한 이름의 라벨 파일 복사
    label_file = file.replace('.jpg', '.txt')
    label_path = os.path.join(label_source_dir, label_file)
    if os.path.exists(label_path):
        shutil.copy(label_path, os.path.join(train_label_dir, label_file))

for file in valid_files:
    # 이미지 복사
    shutil.copy(os.path.join(image_source_dir, file), os.path.join(valid_image_dir, file))
    # 동일한 이름의 라벨 파일 복사
    label_file = file.replace('.jpg', '.txt')
    label_path = os.path.join(label_source_dir, label_file)
    if os.path.exists(label_path):
        shutil.copy(label_path, os.path.join(valid_label_dir, label_file))

print("Train 및 Valid 데이터셋 분할 및 라벨 파일 복사가 완료되었습니다.")
