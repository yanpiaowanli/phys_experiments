import artist as at
import librarian as lb
import statistician as st
import os


if __name__ == '__main__':
    """ This is experimental. """
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    output_dir = os.path.join(os.path.dirname(__file__), 'output')
    os.makedirs(output_dir, exist_ok=True)

    # csv_files = lb.find_csv_files(data_dir)
    # for csv_file in csv_files:
    #     at.draw_scatter_plot(csv_file, output_dir)

    csv_files = [
        os.path.join(data_dir, '1-Uc.csv'),
        os.path.join(data_dir, '1-Ul.csv'),
        os.path.join(data_dir, '1-Ur.csv')
    ]
    at.draw_3_scatter_plot(csv_files, output_dir)

    csv_files = [
        os.path.join(data_dir, '2-Uc.csv'),
        os.path.join(data_dir, '2-Ul.csv'),
        os.path.join(data_dir, '2-Ur.csv')
    ]
    at.draw_3_scatter_plot(csv_files, output_dir)

    csv_files = [
        os.path.join(data_dir, '3-Ur.csv')
    ]
    at.draw_3_scatter_plot(csv_files, output_dir)

    csv_files = [
        os.path.join(data_dir, '1-Ur.csv'),
        os.path.join(data_dir, '2-Ur.csv'),
        os.path.join(data_dir, '3-Ur.csv')
    ]
    at.draw_3_scatter_plot_2(csv_files, output_dir)