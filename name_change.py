import os

# 파일이 저장된 디렉토리 경로
directory = 'C:/train_data_file/data_darkness2/train/image'  # 실제 파일이 위치한 경로로 변경

# 파일 목록에서 이름 변경
for filename in os.listdir(directory):
    # "combined_result_resized_"로 시작하고 ".jpg" 또는 ".txt"로 끝나는 파일 확인
    if filename.startswith('resized_') and (filename.endswith('.jpg') or filename.endswith('.txt')):
        # 새로운 파일 이름 만들기
        #new_filename = filename.replace('combined_result_resized_', '')
        new_filename = filename.replace('resized_', '')

        # 기존 파일 경로와 새로운 파일 경로 설정
        old_file_path = os.path.join(directory, filename)
        new_file_path = os.path.join(directory, new_filename)

        # 파일 이름 변경
        os.rename(old_file_path, new_file_path)
        print(f"Renamed {filename} to {new_filename}")

print("모든 파일 이름 변경이 완료되었습니다.")