import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from data_analyzer import L_dist, G, H

# 路径定义
PATH = 'exp1-3_result.csv'  # 实验1-3数据路径

# 全局变量
df_amplified = None  # 用于存储放大100倍后的数据
slope = 0  # 用于存储斜率


# 自定义格式化函数 TODO: 待修改，有bug
def format_sigfig(x, pos):
    formatted = f'{x:.4g}'
    if '.' in formatted:
        return formatted.ljust(5, '0')
    else:
        return f'{formatted}.00'


def preprocess(path):
    "“ 数据预处理 """
    # 使用全局变量df_amplified
    global df_amplified

    # 读取数据
    df = pd.read_csv(path)

    # 将速度差平方的单位转换为100cm^2/s^2
    df_amplified = df.copy()
    df_amplified['vi^2-v0i^2'] = df_amplified['vi^2-v0i^2'] / 100  # 单位: 100cm^2/s^2


def generate_chart():
    """ 生成图表 """
    # 绘制 v^2-v0^2 - s 图像
    plt.plot(df_amplified['si'], df_amplified['vi^2-v0i^2'], marker='+')
    plt.xlabel('s (cm)')
    plt.ylabel('(v^2 - v0^2) (100cm^2/s^2)')
    plt.title('v^2-v0^2 - s Graph')
    plt.grid(True)

    # 设置坐标轴刻度标签格式（均为4位有效数字）
    plt.gca().xaxis.set_major_formatter(FuncFormatter(format_sigfig))
    plt.gca().yaxis.set_major_formatter(FuncFormatter(format_sigfig))
    plt.show()


def calc_slope():
    """ 计算斜率和截距 """
    # 使用全局变量slope
    global slope

    # 计算斜率和截距
    slope, intercept = np.polyfit(df_amplified['si'], df_amplified['vi^2-v0i^2'], 1)
    print(f'The slope of the v^2-v0^2 - s graph is: {slope}')
    print(f'The intercept of the v^2-v0^2 - s graph is: {intercept}')


def calc_deviation():
    """ 计算误差 """
    # 根据图像斜率计算加速度
    a = slope / 2  # 单位: m/s^2

    # 计算真实加速度
    a_ = G * (H / L_dist)  # 单位: m/s^2

    # 计算a的误差
    deviation = abs((a_ - a) / a_) * 100
    print(f'The deviation of acceleration is: {deviation:.2g}%')


# 数据预处理
preprocess(path=PATH)
# 生成图表
generate_chart()
# 计算斜率和截距
calc_slope()
# 计算误差
calc_deviation()
