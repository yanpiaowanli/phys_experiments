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
from data.config import L_dist, G, H


# 全局变量
df_amp = None  # 用于存储放大100倍后的数据
slope = 0  # 用于存储斜率


def preprocess(path):
    "“ 数据预处理 """
    # 使用全局变量df_amplified
    global df_amp

    # 读取数据
    df = pd.read_csv(path)

    # 将速度差平方的单位转换为100cm^2/s^2
    df_amp = df.copy()
    df_amp['vi^2-v0i^2'] = df_amp['vi^2-v0i^2'] / 100  # 单位: 100cm^2/s^2


def generate_chart(path):
    """ 生成图表 """
    # 绘制 v^2-v0^2 - s 图像
    plt.plot(df_amp['si'], df_amp['vi^2-v0i^2'], marker='+')
    plt.xlabel('s (cm)')
    plt.ylabel('(v^2 - v0^2) (100cm^2/s^2)')
    plt.title('v^2-v0^2 - s Graph')
    plt.grid(True)

    # 设置坐标轴刻度标签格式（均为4位有效数字）
    plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    plt.savefig(path)
    plt.close()


def calc_slope():
    """ 计算斜率和截距 """
    # 使用全局变量slope
    global slope

    # 计算斜率和截距
    slope, intercept = np.polyfit(df_amp['si'], df_amp['vi^2-v0i^2'], 1)
    print(f'The slope of the v^2-v0^2 - s graph is: {slope}')
    print(f'The intercept of the v^2-v0^2 - s graph is: {intercept}')
    if intercept > 0:
        print(f'The equation of the graph is: y = {slope:.4g} * x + {intercept:.4g}')
    else:
        print(f'The equation of the graph is: y = {slope:.4g} * x - {abs(intercept):.4g}')


def calc_deviation():
    """ 计算误差 """
    # 根据图像斜率计算加速度
    a = slope / 2  # 单位: m/s^2

    # 计算真实加速度
    a_ = G * (H / L_dist)  # 单位: m/s^2

    # 计算a的误差
    deviation = abs((a_ - a) / a_) * 100
    print(f'The deviation of acceleration is: {deviation:.2g}%')
