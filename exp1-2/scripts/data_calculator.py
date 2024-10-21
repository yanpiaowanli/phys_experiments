import sys
import os
import pandas as pd

# 获取当前文件的目录
current_dir = os.path.dirname(os.path.abspath(__file__))
# 获取项目根目录
project_root = os.path.abspath(os.path.join(current_dir, '..', '..'))
# 将项目根目录添加到sys.path
sys.path.append(project_root)
from data.config import S, L, G, Mw

# 单位转换常量
MS_TO_S: float = 10 ** -3
CM_TO_M: float = 10 ** -2
G_TO_KG: float = 10 ** -3


def calc_deviation(m: float, path: str) -> None:
    """ 计算误差 """
    try:
        # 读取数据
        df = pd.read_csv(path)

        # 将时间从ms转换为s
        df['t1'] = df['t1'] * MS_TO_S
        df['t2'] = df['t2'] * MS_TO_S

        # 计算v1, v2, a, F
        df['v1'] = L / df['t1']  # 单位: cm/s
        df['v2'] = L / df['t2']  # 单位: cm/s
        df['a'] = (df['v2'] ** 2 - df['v1'] ** 2) / (2 * S)  # 单位: cm/s^2

        # 计算a的平均值
        avg_a = df['a'].mean()

        # 计算理论外力和实际外力
        f_ = (m + Mw) * G_TO_KG * avg_a * CM_TO_M  # 理论外力 单位: N
        f = Mw * G_TO_KG * G  # 实际外力 单位: N

        # 计算误差
        deviation = abs((f - f_) / f) * 100
        print(f'The deviation of force is: {deviation:.2g}%')

        # 将结果精确到四位有效数字
        df = df.applymap(lambda x: f'{x:.4g}' if isinstance(x, (int, float)) else x)

        # 保存结果
        output_path = os.path.join('output', os.path.basename(path).replace('.csv', '_result.csv'))
        df.to_csv(output_path, index=False)
    except Exception as e:
        print(f"An error occurred: {e}")
