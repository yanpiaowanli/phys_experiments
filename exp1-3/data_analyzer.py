import pandas as pd

# 常量定义
L_dist = 86.50  # 气轨支撑点间距L 单位cm
L_width = 5.00  # 遮光板宽度l 单位cm
G = 9.801  # 重力加速度g 单位m/s^2
H = 2.00  # 垫块高度h 单位cm
M_ = 221.19  # 大滑块质量 单位g

# 路径定义
PATH = 'exp1-3.csv'  # 实验1-3数据路径


def analyze(path):
    """ 计算并填入表格 """
    # 读取数据
    df = pd.read_csv(path)

    # 将时间从ms转换为s
    df['t1'] = df['t1'] * (10 ** -3)
    df['t2'] = df['t2'] * (10 ** -3)

    # 计算v1, v2, a, F
    df['v0i'] = L_width / df['t1']  # 单位: cm/s
    df['vi'] = L_width / df['t2']  # 单位: cm/s
    df['vi^2-v0i^2'] = df['vi'] ** 2 - df['v0i'] ** 2  # 单位: cm/s^2

    # 将结果精确到四位有效数字
    df = df.applymap(lambda x: f'{x:.4g}' if isinstance(x, (int, float)) else x)

    # 保存结果
    df.to_csv(path.replace('.csv', '_result.csv'), index=False)


# 分析数据
analyze(path=PATH)
