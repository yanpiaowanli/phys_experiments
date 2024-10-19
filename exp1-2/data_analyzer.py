import pandas as pd

# 常量定义
S = 70.00  # 光电门距离s 单位cm
L = 5.00  # 遮光板宽度l 单位cm
G = 9.801  # 重力加速度g 单位m/s^2
M1 = 142.35  # 系统1（小滑块）质量 单位g
M2 = 231.19  # 系统2（大滑块）质量 单位g
Mw = 10.00  # 施力物质量 单位g

# 路径定义
path1 = 'exp1-2-1.csv'
path2 = 'exp1-2-2.csv'


def calc_deviation(m, path):
    """ 计算误差 """
    # 读取数据
    df = pd.read_csv(path)

    # 将时间从ms转换为s
    df['t1'] = df['t1'] * (10 ** -3)
    df['t2'] = df['t2'] * (10 ** -3)

    # 计算v1, v2, a, F
    df['v1'] = L / df['t1']  # 单位: cm/s
    df['v2'] = L / df['t2']  # 单位: cm/s
    df['a'] = (df['v2'] ** 2 - df['v1'] ** 2) / (2 * S)  # 单位: cm/s^2

    # 计算a的平均值
    avg_a = df['a'].mean()

    # 计算理论外力和实际外力
    f_ = m * (10 ** -3) * avg_a * (10 ** -2)  # 理论外力 单位: N
    f = Mw * (10 ** -3) * G  # 实际外力 单位: N

    # 计算误差
    deviation = abs((f - f_) / f) * 100
    print(f'The deviation of force is: {deviation:.2g}%')

    # 将结果精确到四位有效数字
    df = df.applymap(lambda x: f'{x:.4g}' if isinstance(x, (int, float)) else x)

    # 保存结果
    df.to_csv(path.replace('.csv', '_result.csv'), index=False)


# 计算误差
calc_deviation(m=M1, path=path1)
calc_deviation(m=M2, path=path2)
