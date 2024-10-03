import os
import shutil

# 라벨이 저장된 디렉토리와 새 디렉토리 설정
label_dir = r'C:\yolov10-main\ultralytics\cfg\final_1\train\labels'
new_label_dir = r'C:\Users\yseun\Desktop\final_c8'

# 새 디렉토리 생성 (존재하지 않을 경우)
os.makedirs(new_label_dir, exist_ok=True)

# 원하는 클래스 번호
target_classes = {8}

# 디렉토리를 순회하면서 파일 처리
for filename in os.listdir(label_dir):
    if filename.endswith('.txt'):  # 라벨 파일 확인
        filepath = os.path.join(label_dir, filename)
        with open(filepath, 'r') as file:
            lines = file.readlines()
            # 각 라인(라벨)을 확인하고 조건에 맞는 경우 작업 수행
            for line in lines:
                class_id = int(line.split()[0])  # 클래스 ID 추출
                if class_id in target_classes:
                    # 타겟 클래스를 찾은 경우, 파일을 새 디렉토리로 복사
                    shutil.copy(filepath, os.path.join(new_label_dir, filename))
                    print(f"Copied: {filename} to {new_label_dir}")
                    break  # 해당 파일에서 한 번 찾으면 더 이상 다른 라인 확인하지 않음