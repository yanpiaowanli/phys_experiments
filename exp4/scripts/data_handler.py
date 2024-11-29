import numpy as np
import pandas as pd
import sys
import os
import math

# 获取当前文件目录
current_dir = os.path.dirname(os.path.abspath(__file__))
# 获取项目根目录
project_root = os.path.abspath(os.path.join(current_dir, '..', '..'))
# 将项目根目录添加到sys.path
sys.path.append(project_root)
from data.config import FBZX_36, FBZX_21


def calc_delta_r(r, m):
    """ 计算电阻的不确定度 """
    u = 0.005 * m
    if m == 4:
        r_temp = r
        num = 1000
        for i in range(4):
            u += FBZX_36[i] * (r_temp // num) * num
            r_temp %= num
            num //= 10
    elif m == 6:
        r_temp = r * 10
        num = 100000
        for i in range(6):
            u += FBZX_21[i] * (r_temp // num) * num / 10
            r_temp %= num
            num //= 10
    return u


def round_to_sig_figs(x, sig_figs):
    """ 保留有效数字 """
    if isinstance(x, (int, float)):
        return float(f'{x:.{sig_figs}g}')
    return x


def calculate_c1(path):
    """ 计算并填入表格 """
    # 读取数据
    df = pd.read_csv(path)

    # 计算delta_R0
    df['delta_R0'] = abs(df['R0'] - df["R0'"])

    # 计算S
    df['S'] = df['delta_d'] / (df['delta_R0'] / df['R0'])

    # 计算delta_S
    df['delta_S'] = (df['R1'] / df['R2']) * (0.2 / df['delta_d']) * df['delta_R0']

    # 计算Rx
    df['Rx'] = df['R0'] * (df['R1'] / df['R2'])

    # 计算delta_x
    df['delta_x'] = ((df['Rx'] * df['R1'].apply(lambda r: calc_delta_r(r, 4)) / df['R1']) ** 2 +
                     (df['Rx'] * df['R2'].apply(lambda r: calc_delta_r(r, 4)) / df['R2']) ** 2 +
                     (df['Rx'] * df['R0'].apply(lambda r: calc_delta_r(r, 6)) / df['R0']) ** 2) ** 0.5

    # 计算不确定度u
    df['u'] = (df['delta_x'] ** 2 + df['delta_S'] ** 2) ** 0.5

    # 计算相对不确定度Ur
    df['Ur'] = df['u'] / df['Rx'] * 100

    # 将df转为四位有效数字
    df = df.applymap(lambda x: round_to_sig_figs(x, 4))

    # 计算Rx±u
    df['Rx±u'] = df['Rx'].apply(lambda x: f"{x:.1f}") + '±' + df['u'].apply(lambda x: f"{x:.1f}")

    # 保存数据表格
    output_path = os.path.join('output', os.path.basename(path).replace('.csv', '_result.csv'))
    df.to_csv(output_path, index=False)


def calculate_c2(path):
    """ 计算并填入表格 """
    # 读取数据
    df = pd.read_csv(path)

    # 计算Rx
    df['Rx'] = (df['R0'] * df["R0'"]) ** 0.5
    df = df.applymap(lambda x: round_to_sig_figs(x, 4))

    # 保存数据表格
    output_path = os.path.join('output', os.path.basename(path).replace('.csv', '_result.csv'))
    df.to_csv(output_path, index=False)


def calculate_c3(path):
    """ 计算并填入表格 """
    # 读取数据
    df = pd.read_csv(path)

    df['Rx'] = df['R0'] * df['C']
    df = df.applymap(lambda x: round_to_sig_figs(x, 4))

    # 保存数据表格
    output_path = os.path.join('output', os.path.basename(path).replace('.csv', '_result.csv'))
    df.to_csv(output_path, index=False)
