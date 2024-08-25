import os
from PIL import Image
import pyheif


def find_all_heic_pictures(needed_path):
    """Find all heic pictures in the path. The path is set to the main folder directory, it can be changed manually"""
    heic_pictures = []
    for file in os.listdir(needed_path):
        if file.lower().endswith('.heic'):
            heic_pictures.append(f'{needed_path}\{file}')

            new_file_path = os.path.join(needed_path, file.lower().replace('.heic', '.JPEG'))

            width, height = 100, 100
            mode = 'RGB'
            data = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)

            data_bytes = data.tobytes()
            Image.frombytes(mode, (width, height), data_bytes).save(new_file_path, format='JPEG')

    return heic_pictures


path = os.getcwd()
all_heic_pictures = find_all_heic_pictures(path)
print(all_heic_pictures[0])
