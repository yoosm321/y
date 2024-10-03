import cv2
import numpy as np
import os


def adjust_brightness_contrast(image, brightness_target=128):
    # 이미지 그레이스케일로 변환하여 평균 밝기 계산
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    mean_brightness = np.mean(gray_image)
    adjusted_image = image

    # 밝기 조절 (어두운 이미지는 밝게, 밝은 이미지는 어둡게)
    if mean_brightness < brightness_target:  # 어두운 이미지라면 밝게
        adjusted_image = cv2.convertScaleAbs(image, alpha=1.25, beta=0)
    elif mean_brightness < 140.0:  # 밝은 이미지라면 어둡게
        adjusted_image = cv2.convertScaleAbs(image, alpha=1.25, beta=-5)
    elif mean_brightness > 150.0:  # 많이 밝은 이미지
        adjusted_image = cv2.convertScaleAbs(image, alpha=1.25, beta=-10)

    return adjusted_image

#붉은 색상의 이미지들 색상 보정
def white_balance(image):

    # 그레이월드 알고리즘을 통한 자동 화이트 밸런스 적용
    result_image = cv2.xphoto.createSimpleWB().balanceWhite(image)

    return result_image


def adjust_contrast(image, clip_limit=2.0, tile_grid_size=(8, 8)):
    # CLAHE (Contrast Limited Adaptive Histogram Equalization)로 명암비 조절
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)

    # 이미지를 YUV로 변환하고 명암비 조절
    yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
    yuv[:, :, 0] = clahe.apply(yuv[:, :, 0])  # 밝기 채널에만 CLAHE 적용
    contrast_adjusted_image = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR)

    return contrast_adjusted_image


# 디렉토리 내 모든 이미지 처리
def process_images_in_directory(image_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 디렉토리 내 이미지 처리
    for filename in os.listdir(image_dir):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            image_path = os.path.join(image_dir, filename)
            image = cv2.imread(image_path)

            # 화이트 밸런스 조절
            white_image = white_balance(image)

            # 밝기 조절
            #adjusted_image = adjust_brightness_contrast(white_image)

            #명암비 조절
            #final_image = adjust_contrast(adjusted_image)

            # 결과 저장
            output_path = os.path.join(output_dir, filename)
            cv2.imwrite(output_path, white_image)



# 사용 예시
image_dir = r'C:\yolov10-main\ultralytics\cfg\final_1\train\images'  # 입력 이미지 경로
output_dir = r'C:\yolov10-main\ultralytics\cfg\final_1\train\images_wb'  # 출력 경로
process_images_in_directory(image_dir, output_dir)
