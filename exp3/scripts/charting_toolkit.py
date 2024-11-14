import sys
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

# 获取当前文件目录
current_dir = os.path.dirname(os.path.abspath(__file__))
# 获取项目根目录
project_root = os.path.abspath(os.path.join(current_dir, '..', '..'))
# 将项目根目录添加到sys.path
sys.path.append(project_root)

# 定义单位转换常量
CM_TO_M = 1e-2


def generate_chart(result_path, output_path):
    """ 生成图表 """
    # 读取数据
    df = pd.read_csv(result_path)

    # 绘制I - x^2图
    df['x^2'] = (df['x'].iloc[:5] * CM_TO_M) ** 2
    plt.scatter(df['x^2'].iloc[:5], df['I_exp'].iloc[:5], marker='+')
    plt.xlabel('x^2 (m^2)')
    plt.ylabel('I (kg*m^2)')
    plt.title('I - x^2 Graph')
    plt.grid(True)

    # 线性拟合
    slope, intercept = np.polyfit(df['x^2'].iloc[:5], df['I_exp'].iloc[:5], 1)
    fit_line = slope * df['x^2'].iloc[:5] + intercept
    plt.plot(df['x^2'].iloc[:5], fit_line, color='blue')
    if intercept >= 0:
        s = f'Fit Line: I = {slope:.3g} × x^2 + {intercept:.3g}'
        plt.legend([s], loc='upper left')
        print(s)
    else:
        s = f'Fit Line: I = {slope:.3g} × x^2 - {abs(intercept):.3g}'
        plt.legend([s], loc='upper left')
        print(s)

    # 设置坐标轴刻度标签格式（均为3位有效数字）
    plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%.3g'))
    plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.3g'))
    plt.savefig(output_path)

    print(f'The I-x^2 graph saved to ./{output_path}')
    plt.close()
