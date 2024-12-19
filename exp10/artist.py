import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
import os


def draw_scatter_plot(data_paths, output_dir, col_idx_x=0, col_idx_y=1):
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

        max_y_smooth = y_smooth.max()
        max_x_smooth = x_new[y_smooth.argmax()]
        plt.annotate(f'Max: ({max_x_smooth:.4g}, {max_y_smooth:.4g})', xy=(max_x_smooth, max_y_smooth),
                     xytext=(max_x_smooth, max_y_smooth + 0.1),
                     arrowprops=dict(facecolor='black', shrink=0.05))

        plt.axvline(x=max_x_smooth, color='gray', linestyle='-.')

    plt.xlabel("f / Hz")
    plt.ylabel("U / V")
    plt.legend()
    file_name = f"{os.path.splitext(os.path.basename(data_paths[0]))[0]}.png"
    plt.savefig(os.path.join(output_dir, file_name))
    plt.close()
    plt.show()
