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

from data.config import M_


# 全局变量
df_avg = None  # 用于存储每三行数据的平均值
slope = 0   # 用于存储斜率


def preprocess(path):
    """ 数据预处理 """
    # 使用全局变量df_avg
    global df_avg

    # 读取数据
    df = pd.read_csv(path)

    # 将 'a' 列转换为浮点数，并将单位从cm/s^2转换为m/s^2
    df['a'] = (df['a'] * (10 ** -2)).astype(float)

    # 计算每三行数据的 'a' 和 'F' 的平均值
    df_avg = df.groupby(df.index // 3).mean()


def generate_chart(path):
    """ 生成图表 """
    # 绘制 F-a 图像
    plt.plot(df_avg['a'], df_avg['F'], marker='+')
    plt.xlabel('a (m/s^2)')
    plt.ylabel('F (N)')
    plt.title('F - a Graph')
    plt.grid(True)
    plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%.3f'))
    plt.savefig(path)
    plt.close()


def calc_slope():
    """ 计算斜率和截距 """
    # 使用全局变量slope
    global slope

    # 计算斜率和截距
    slope, intercept = np.polyfit(df_avg['a'], df_avg['F'], 1)
    print(f'The slope of the F - a graph is: {slope}')
    print(f'The intercept of the F - a graph is: {intercept}')
    if intercept > 0:
        print(f'The equation of the F - a graph is: F = {slope:.4g} * a + {intercept:.4g}')
    else:
        print(f'The equation of the F - a graph is: F = {slope:.4g} * a - {abs(intercept):.4g}')


def calc_deviation():
    """ 根据实际质量计算误差 """
    # 使用全局变量slope
    global slope

    # 计算m的误差
    deviation = abs((M_ - slope * (10 ** 3)) / M_) * 100
    print(f'The deviation of system mass is: {deviation:.2g}%')
