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
from data.config import G, L, D, B


# 全局变量
slope = 0  # 用于存储斜率

# 定义单位转换常量
CM_TO_M = 1e-2
MM_TO_M = 1e-3
PA_TO_GPA = 1e-9


def generate_chart(result_path, output_path):
    """ 生成图表 """
    # 读取数据
    df = pd.read_csv(result_path)
    global slope

    # 绘制n - M图
    plt.scatter(df['m'], df['ni_avg'], marker='+')
    plt.xlabel('M (kg)')
    plt.ylabel('n (cm)')
    plt.title('n - M Graph')
    plt.grid(True)

    # 线性拟合
    slope, intercept = np.polyfit(df['m'], df['ni_avg'], 1)
    fit_line = slope * df['m'] + intercept
    plt.plot(df['m'], fit_line, color='blue')
    if intercept >= 0:
        print(f'Fit Line: n_avg = {slope:.3g} × M + {intercept:.3g}')
    else:
        print(f'Fit Line: n_avg = {slope:.3g} × M - {abs(intercept):.3g}')

    # 设置坐标轴刻度标签格式（均为3位有效数字）
    plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    plt.savefig(output_path)
    print(f'The n-M graph saved to ./{output_path}')
    plt.close()

    # 输出空行
    print()


def calc_deviation(result_path, E_theory):
    """ 计算误差 """
    # 读取数据，并计算d
    df = pd.read_csv(result_path)
    d = df['d_real'].mean()

    # 根据图像斜率计算杨氏模量E，并输出
    E = ((8 * G * (L * MM_TO_M) * (D * MM_TO_M)) /
         (np.pi * ((d * MM_TO_M) ** 2) * (B * MM_TO_M) * (slope * CM_TO_M))) * PA_TO_GPA
    print(f'The value of E calculated from graph is {E:.3g} GPa')

    # 计算误差，并输出
    deviation = abs(E - E_theory) / E_theory
    print(f'The deviation of E calculated from graph is {(deviation * 100):.2g}%')

    # 输出空行
    print()
