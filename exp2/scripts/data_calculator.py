import sys
import os
import math
import pandas as pd

# 获取当前文件目录
current_dir = os.path.dirname(os.path.abspath(__file__))
# 获取项目根目录
project_root = os.path.abspath(os.path.join(current_dir, '..', '..'))
# 将项目根目录添加到sys.path
sys.path.append(project_root)
from data.config import D0, M, G, L, D, B, DELTA_N, DELTA_D, DELTA_L, DELTA_D_, DELTA_B, C

# 定义单位转换常量
CM_TO_M = 1e-2
MM_TO_M = 1e-3
PA_TO_GPA = 1e-9

# 定义数理统计常量
T_95_4 = 3.18
T_95_6 = 2.57


def preprocess_c1(path):
    """ 计算并填入表格 """

    # 读取数据
    df = pd.read_csv(path)

    # 计算 ni_avg
    df['ni_avg'] = (df['ni+'] + df['ni-']) / 2

    # 计算 n_delta
    n_delta_values = []
    for i in range(4):
        n_delta = (df['ni_avg'][i + 4] - df['ni_avg'][i]) / 4
        n_delta_values.append(n_delta)
        n_delta_values.append(n_delta)
    df['n_delta'] = n_delta_values

    # 格式化数值，保留四位有效数字
    df['ni_avg'] = df['ni_avg'].map(lambda x: format(x, '.3f'))
    df['n_delta'] = df['n_delta'].map(lambda x: format(x, '.3f'))

    # 保存结果
    output_path = os.path.join('output', os.path.basename(path).replace('.csv', '_result.csv'))
    df.to_csv(output_path, index=False)

    # 计算n_delta的标准差
    df['n_delta'] = df['n_delta'].astype(float)
    n_delta_std = df['n_delta'].std()

    # 计算n_delta的不确定度
    u_n_delta = ((T_95_4 * n_delta_std) ** 2 + (2 * DELTA_N / C) ** 2) ** 0.5

    # 输出n_delta的均值和不确定度
    print(f'The value of δn is {df["n_delta"].mean():.3g} ± {u_n_delta:.3f} cm, with a confidence level of 95%')

    # 计算n_delta的相对不确定度
    u_n_delta_relative = u_n_delta / df['n_delta'].mean()
    print(f'The relative uncertainty of δn is {(u_n_delta_relative * 100):.2g}%')

    # 输出空行
    print()


def preprocess_c2(path):
    """ 计算并填入表格 """
    # 读取数据
    df = pd.read_csv(path)
    df['d_real'] = df['di'] - D0
    df['d_avg'] = df['d_real'].mean()

    # 保存结果
    output_path = os.path.join('output', os.path.basename(path).replace('.csv', '_result.csv'))
    df.to_csv(output_path, index=False, float_format='%.3g')

    # 计算d_real的标准差
    df['d_real'] = df['d_real'].astype(float)
    d_real_std = df['d_real'].std()

    # 计算d_real的不确定度
    u_d_real = ((T_95_6 * d_real_std) ** 2 + (2 * DELTA_D / C) ** 2) ** 0.5

    # 输出d_real的均值和不确定度
    print(f'The value of d is {df["d_real"].mean():.3g} ± {u_d_real:.3f} mm, with a confidence level of 95%')

    # 计算d_real的相对不确定度
    u_d_real_relative = u_d_real / df['d_real'].mean()
    print(f'The relative uncertainty of d is {(u_d_real_relative * 100):.2g}%')

    # 输出空行
    print()


def calc_youngs_modulus(path_c1, path_c2):
    """ 计算杨氏模量以及不确定度 """
    # 读取数据
    df1 = pd.read_csv(path_c1)
    df2 = pd.read_csv(path_c2)

    # 计算杨氏模量
    E = ((8 * M * G * (L * MM_TO_M) * (D * MM_TO_M)) /
         (math.pi * ((df2['d_avg'][0] * MM_TO_M) ** 2) * (B * MM_TO_M) * (df1['n_delta'].mean() * CM_TO_M))) * PA_TO_GPA

    # 计算n_delta的相对不确定度
    n_delta_std = df1['n_delta'].std()
    u_n_delta = ((T_95_4 * n_delta_std) ** 2 + (2 * DELTA_N / C) ** 2) ** 0.5
    u_n_delta_r = u_n_delta / df1['n_delta'].mean()

    # 计算d_real的相对不确定度
    d_real_std = df2['d_real'].std()
    u_d_real = ((T_95_6 * d_real_std) ** 2 + (2 * DELTA_D / C) ** 2) ** 0.5
    u_d_real_r = u_d_real / df2['d_real'].mean()

    # 计算L的相对不确定度
    u_L_r = DELTA_L / L

    # 计算D的相对不确定度
    u_D_r = DELTA_D_ / D

    # 计算b的相对不确定度
    u_b_r = DELTA_B / B

    # 计算E的相对不确定度
    u_E_r = (u_n_delta_r ** 2 + 4 * (u_d_real_r ** 2) + u_L_r ** 2 + u_D_r ** 2 + u_b_r ** 2) ** 0.5

    # 计算E的不确定度
    u_E = E * u_E_r

    # 输出E和不确定度
    print(f'The value of E is {E:.3g} ± {int(u_E.round())} GPa, with a confidence level of 95%')
    print(f'The relative uncertainty of E is {(u_E_r * 100):.2g}%')

    # 输出空行
    print()

    # 返回理论计算的杨氏模量值
    return E
