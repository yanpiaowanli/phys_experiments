import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
import os


def draw_scatter_plot(data_path, output_dir, col_idx_x=0, col_idx_y=1):
    """ Draw a scatter plot from a csv file """
    data = pd.read_csv(data_path)
    x_label = data.columns[col_idx_x]
    y_label = data.columns[col_idx_y]

    x = data.iloc[:, col_idx_x]
    y = data.iloc[:, col_idx_y]
    title = f"{y_label} - {x_label} Scatter Plot"
    plt.scatter(x, y, marker='+')

    x_new = np.linspace(x.min(), x.max(), 300)
    spl = make_interp_spline(x, y, k=3)
    y_smooth = spl(x_new)
    plt.plot(x_new, y_smooth, color='red')

    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    file_name = os.path.splitext(os.path.basename(data_path))[0] + '.png'
    plt.savefig(os.path.join(output_dir, file_name))
    plt.close()
    plt.show()


def draw_3_scatter_plot(data_paths, output_dir, col_idx_x=0, col_idx_y=1):
    """ Draw a scatter plot from multiple csv files """
    plt.figure()

    for data_path in data_paths:
        data = pd.read_csv(data_path)
        x_label = data.columns[col_idx_x]
        y_label = data.columns[col_idx_y]

        x = data.iloc[:, col_idx_x]
        y = data.iloc[:, col_idx_y]
        label = os.path.splitext(os.path.basename(data_path))[0]
        plt.scatter(x, y, marker='+', label=label)

        x_new = np.linspace(x.min(), x.max(), 300)
        spl = make_interp_spline(x, y, k=3)
        y_smooth = spl(x_new)
        plt.plot(x_new, y_smooth, label=f'{label} fit')

    plt.xlabel("f / Hz")
    plt.ylabel("U / V")
    plt.legend()
    file_name = f"3-{os.path.splitext(os.path.basename(data_paths[0]))[0]}.png"
    plt.savefig(os.path.join(output_dir, file_name))
    plt.close()
    plt.show()


def draw_3_scatter_plot_2(data_paths, output_dir, col_idx_x=0, col_idx_y=1):
    """ Draw a scatter plot from multiple csv files """
    plt.figure()

    for data_path in data_paths:
        data = pd.read_csv(data_path)
        data['f'] = data['f'] / 500
        data['Ur'] = data['Ur'] / data['Ur'].max()

        x = data.iloc[:, col_idx_x]
        y = data.iloc[:, col_idx_y]
        label = os.path.splitext(os.path.basename(data_path))[0]
        plt.scatter(x, y, marker='+', label=label)

        x_new = np.linspace(x.min(), x.max(), 300)
        spl = make_interp_spline(x, y, k=3)
        y_smooth = spl(x_new)
        plt.plot(x_new, y_smooth, label=f'{label} fit')

    plt.xlabel("ω/ω0")
    plt.ylabel("I(ω)/I(ω0)")
    plt.legend()
    file_name = f"new.png"
    plt.savefig(os.path.join(output_dir, file_name))
    plt.close()
    plt.show()
