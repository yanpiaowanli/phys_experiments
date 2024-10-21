import sys
import os
import pandas as pd

# 获取当前文件目录
current_dir = os.path.dirname(os.path.abspath(__file__))
# 获取项目根目录
project_root = os.path.abspath(os.path.join(current_dir, '..', '..'))
# 将项目根目录添加到sys.path
sys.path.append(project_root)
from data.config import L_width

# 单位转换常量
MS_TO_S = 10 ** -3


def preprocess(path):
    """ 计算并填入表格 """
    # 读取数据
    df = pd.read_csv(path)

    # 将时间从ms转换为s
    df['t1'] = df['t1'] * MS_TO_S
    df['t2'] = df['t2'] * MS_TO_S

    # 计算v1, v2, a, F
    df['v0i'] = L_width / df['t1']  # 单位: cm/s
    df['vi'] = L_width / df['t2']  # 单位: cm/s
    df['vi^2-v0i^2'] = df['vi'] ** 2 - df['v0i'] ** 2  # 单位: cm/s^2

    # 将结果精确到四位有效数字
    df = df.applymap(lambda x: f'{x:.4g}' if isinstance(x, (int, float)) else x)

    # 保存结果
    output_path = os.path.join('output', os.path.basename(path).replace('.csv', '_result.csv'))
    df.to_csv(output_path, index=False)
