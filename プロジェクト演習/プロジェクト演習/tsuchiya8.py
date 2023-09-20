import cv2
import numpy as np
from PIL import Image

def m_slice(path, dir, step, extension):
    movie = cv2.VideoCapture(path)
    Fs = int(movie.get(cv2.CAP_PROP_FRAME_COUNT))
    path_head = dir + '/out_'
    ext_index = np.arange(0, Fs, step)
    count = 0

    for i in range(Fs - 1):
        flag, frame = movie.read()
        check = i == ext_index

        if flag == True:
            if True in check:
                count += 1
                path_out = path_head + str(count) + extension
                cv2.imwrite(path_out, frame)
            else:
                pass
        else:
            pass

def compare_images(image1, image2):
    gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    height, width = gray_image1.shape
    diff = cv2.absdiff(gray_image1, gray_image2)
    similarity = (np.sum(diff == 0) / (height * width)) * 100
    return similarity

def convert_to_gif(images, output_path, duration=100, loop=0):
    gif_images = [Image.open(image) for image in images if image]
    if gif_images:
        gif_images[0].save(
            output_path,
            save_all=True,
            append_images=gif_images[1:],
            duration=duration,
            loop=loop
        )

def create_mismatched_gif(images, output_path, duration=100, loop=0):
    gif_images = [Image.open(image) for image in images if image]
    if gif_images:
        gif_images[0].save(
            output_path,
            save_all=True,
            append_images=gif_images[1:],
            duration=duration,
            loop=loop
        )

if __name__ == "__main__":
    # 動画をフレームに分割して保存
    m_slice('ent_seikai.mp4', 'frames1', 10, '.png')
    m_slice('uploads/ent_kaito.mp4', 'frames2', 10, '.png')

    # 2つの動画からフレームを取得してGIFに変換
    image_files1 = [f"frames1/out_{i}.png" for i in range(1, 45)]
    output_file1 = "static/images/output1.gif"
    duration_ms1 = 200
    loop_count1 = 0
    convert_to_gif(image_files1, output_file1, duration_ms1, loop_count1)

    image_files2 = [f"frames2/out_{i}.png" for i in range(1, 45)]
    output_file2 = "static/images/output2.gif"
    duration_ms2 = 200
    loop_count2 = 0
    convert_to_gif(image_files2, output_file2, duration_ms2, loop_count2)

    # 画像の比較と一致度の判定
    mismatched_images = []
    similarity_percentages = []

    for i in range(60):
        correct_image_path = f'frames1/out_{i+1}.png'
        test_image_path = f'frames2/out_{i+1}.png'

        # 画像の読み込み
        correct_image = cv2.imread(correct_image_path)
        test_image = cv2.imread(test_image_path)

        # 画像の比較
        similarity_percentage = compare_images(correct_image, test_image)
        similarity_percentages.append(similarity_percentage)

        if similarity_percentage < 99:
            mismatched_images.append(f'out_{i+1}.png')

    # 一致度を出力
    total_frames = len(similarity_percentages)
    matching_frames = total_frames - len(mismatched_images)
    matching_percentage = (matching_frames / total_frames) * 100

    print(f"一致度: {matching_percentage}%")

    if len(mismatched_images) == 0:
        result = "100%です"
    else:
        result = "100%ではありません"

        with open('mismatched_images.txt', 'w') as f:
            f.write('\n'.join(mismatched_images))

    # 一致しなかったフレームをGIFとして出力
    if mismatched_images:
        mismatched_gif_output = "mismatched_images.gif"
        create_mismatched_gif([f"frames2/{img}" for img in mismatched_images], mismatched_gif_output, duration_ms2, loop_count2)
