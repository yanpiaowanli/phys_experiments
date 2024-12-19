import artist as at
import librarian as lb
import scissors as sc
import palette as pl
import os


if __name__ == '__main__':
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    output_dir = os.path.join(os.path.dirname(__file__), 'output')
    os.makedirs(output_dir, exist_ok=True)

    csv_files = lb.find_data(data_dir)
    at.draw_scatter_plot(csv_files, output_dir)

    img_files = lb.find_images()

    for img_file in img_files:
        sc.cut(img_file)

    # 弃用
    # for img_file in img_files:
    #     pl.enhance_image(img_file)
