import os


def find_all_heic_pictures():
    """Find all heic pictures in the path. The path is set to the main folder directory, it can be changed manually"""
    needed_path = os.getcwd() # if someone wants can change the folder path
    heic_pictures = []
    for file in os.listdir(needed_path):
        if file.lower().endswith('.heic'):
            heic_pictures.append(f'{needed_path}\{file}')

    return heic_pictures