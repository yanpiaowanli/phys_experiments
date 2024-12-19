import os


def find_images(img_path='img'):
    images = []
    for root, dirs, files in os.walk(img_path):
        for file in files:
            if file.endswith('.jpg') or file.endswith('.png'):
                images.append(os.path.join(root, file))
    return images


def find_data(data_path='data'):
    data = []
    for root, dirs, files in os.walk(data_path):
        for file in files:
            if file.endswith('.csv'):
                data.append(os.path.join(root, file))
    return data
