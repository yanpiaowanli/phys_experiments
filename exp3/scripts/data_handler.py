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
from data.config import M_cylinder, M_barrel, M_sphere, Iz, I5_, M_2, DELTA_T, C

# 定义单位转换常量
CM_TO_M = 1e-2
MM_TO_M = 1e-3

# 定义数理统计常量
T_95_10 = 2.26

def calculate_c1(path):
    """ 计算并填入表格 """
    # 读取数据
    df = pd.read_csv(path)

    # 计算标准圆柱体直径均值Dc_avg
    Dc_avg = df['Dc'].iloc[:3].mean()
    df.at[0, 'Dc_avg'] = round(Dc_avg, 3)

    # 计算圆柱体转动惯量理论值I1
    I1 = 1/8 * M_cylinder * (Dc_avg * MM_TO_M) ** 2
    print(f"The theoretical value of I1 is {I1:.4g} kg*m^2")

    # 计算载物盘转动周期T0_avg，并计算不确定度
    T0_avg = df['T0'].iloc[:10].mean()
    df.at[0, 'T0_avg'] = round(T0_avg, 4)

    T0_std = df['T0'].iloc[:10].std()
    u_T0 = ((T_95_10 * T0_std) ** 2 + (2 * DELTA_T / C) ** 2) ** 0.5
    print(f"The value of T0 is {T0_avg:.4f} ± {u_T0:.4f} s, with a confidence level of 95%")

    # 计算载物盘+标准圆柱体转动周期均值T1_avg
    T1_avg = df['T1'].iloc[:3].mean()
    df.at[0, 'T1_avg'] = round(T1_avg, 4)

    # 计算载物盘转动惯量I0
    I0 = I1 * T0_avg ** 2 / (T1_avg ** 2 - T0_avg ** 2)
    print(f"The value of I0 is {I0:.4g} kg*m^2")

    # 计算弹簧扭转常数k
    k = 4 * math.pi ** 2 * I1 / (T1_avg ** 2 - T0_avg ** 2)
    print(f"The value of k is {k:.4g} N*m/rad")

    # 保存数据表格
    output_path = os.path.join('output', os.path.basename(path).replace('.csv', '_result.csv'))
    df.to_csv(output_path, index=False)

    # 输出空行
    print()

    # 返回结果
    return k, I0


def calculate_c2(path, k, I0):
    """ 计算并填入表格 """
    # 读取数据
    df = pd.read_csv(path)

    # 计算金属圆筒内径均值D1_avg
    D1_avg = df['D1'].iloc[:3].mean()
    df.at[0, 'D1_avg'] = round(D1_avg, 3)

    # 计算金属圆筒外径均值D2_avg
    D2_avg = df['D2'].iloc[:3].mean()
    df.at[0, 'D2_avg'] = round(D2_avg, 3)

    # 计算球体直径均值D_avg
    D_avg = df['D'].iloc[:3].mean()
    df.at[0, 'D_avg'] = round(D_avg, 3)

    # 计算金属圆筒+载物盘转动周期均值T2_avg
    T2_avg = df['T2'].iloc[:3].mean()
    df.at[0, 'T2_avg'] = round(T2_avg, 4)

    # 计算球体转动周期均值T3_avg
    T3_avg = df['T3'].iloc[:3].mean()
    df.at[0, 'T3_avg'] = round(T3_avg, 4)

    # 计算金属圆筒转动惯量理论值I2'
    I2_ = 1/8 * M_barrel * ((D1_avg * CM_TO_M) ** 2 + (D2_avg * CM_TO_M) ** 2)
    print(f"The theoretical value of I2' is {I2_:.4g} kg*m^2")
    df.at[0, 'I_thr'] = I2_

    # 计算球体转动惯量理论值I3'
    I3_ = 1/10 * M_sphere * (D_avg * CM_TO_M) ** 2
    print(f"The theoretical value of I3' is {I3_:.4g} kg*m^2")
    df.at[1, 'I_thr'] = I3_

    # 计算金属圆筒转动惯量实验值I2
    I2 = k * T2_avg ** 2 / (4 * math.pi ** 2) - I0
    print(f"The experimental value of I2 is {I2:.4g} kg*m^2")
    df.at[0, 'I_exp'] = I2

    # 计算球体转动惯量实验值I3
    I3 = k * T3_avg ** 2 / (4 * math.pi ** 2) - Iz
    print(f"The experimental value of I3 is {I3:.4g} kg*m^2")
    df.at[1, 'I_exp'] = I3

    # 计算金属圆筒转动惯量相对误差e2
    e2 = abs(I2 - I2_) / I2_ * 100
    print(f"The relative error of I2 is {e2:.2g}%")
    df.at[0, 'e'] = e2

    # 计算球体转动惯量相对误差e3
    e3 = abs(I3 - I3_) / I3_ * 100
    print(f"The relative error of I3 is {e3:.2g}%")
    df.at[1, 'e'] = e3

    # 保存数据表格
    output_path = os.path.join('output', os.path.basename(path).replace('.csv', '_result.csv'))
    df.to_csv(output_path, index=False)

    # 输出空行
    print()


def calculate_c3(path, k):
    """ 计算并填入表格 """
    # 读取数据
    df = pd.read_csv(path)

    # 计算金属杆及支座转动周期均值T4_avg
    T4_avg = df['T4'].iloc[:3].mean()
    df.at[0, 'T4_avg'] = round(T4_avg, 4)

    # 计算金属杆及支座转动惯量实验值I4
    I4 = k * T4_avg ** 2 / (4 * math.pi ** 2)
    print(f"The experimental value of I4 is {I4:.4g} kg*m^2")
    df.at[0, 'I4'] = I4

    # 计算金属杆及砝码转动周期均值T_avg
    for i in range(5):
        T_avg = df['T'].iloc[i * 3:(i + 1) * 3].mean()
        df.at[i, 'T_avg'] = T_avg

    # 计算金属杆及砝码转动惯量实验值I_exp
    for i in range(5):
        I_exp = k * df['T_avg'].iloc[i] ** 2 / (4 * math.pi ** 2) - I4
        df.at[i, 'I_exp'] = I_exp

    # 计算金属杆及砝码转动惯量理论值I_thr
    for i in range(5):
        I_thr = I5_ + M_2 * (df['x'].iloc[i] * CM_TO_M) ** 2
        df.at[i, 'I_thr'] = I_thr

    # 计算金属杆及砝码转动惯量相对误差e
    for i in range(5):
        e = abs(df['I_exp'].iloc[i] - df['I_thr'].iloc[i]) / df['I_thr'].iloc[i] * 100
        df.at[i, 'e'] = e

    # 保存数据表格
    output_path = os.path.join('output', os.path.basename(path).replace('.csv', '_result.csv'))
    df.to_csv(output_path, index=False)

    # 输出空行
    print()
