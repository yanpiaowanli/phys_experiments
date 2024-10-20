import pandas as pd

# 常量定义
S = 70.00  # 光电门距离s 单位cm
L = 5.00  # 遮光板宽度l 单位cm
G = 9.801  # 重力加速度g 单位m/s^2
M_ = 157.35  # 真实系统质量 单位g

# 路径定义
PATH = 'exp1-1.csv'  # 实验1-1数据路径


def analyze(path):
    """ 计算并填入表格 """
    # 读取数据
    df = pd.read_csv(path)

    # 将时间从ms转换为s
    df['t1'] = df['t1'] * (10 ** -3)
    df['t2'] = df['t2'] * (10 ** -3)

    # 计算v1, v2, a, F
    df['v1'] = L / df['t1']  # 单位: cm/s
    df['v2'] = L / df['t2']  # 单位: cm/s
    df['a'] = (df['v2'] ** 2 - df['v1'] ** 2) / (2 * S)  # 单位: cm/s^2
    df['F'] = df['m'] * (10 ** -3) * G  # 单位: N

    # 将结果精确到四位有效数字
    df = df.applymap(lambda x: f'{x:.4g}' if isinstance(x, (int, float)) else x)

    # 保存结果
    df.to_csv(path.replace('.csv', '_result.csv'), index=False)


# 分析数据
analyze(path=PATH)
