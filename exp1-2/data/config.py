# 常量定义
S: float = 70.00  # 光电门距离s 单位cm
L: float = 5.00  # 遮光板宽度l 单位cm
G: float = 9.801  # 重力加速度g 单位m/s^2
M: list[float] = [132.35, 221.19]  # 滑块质量m 单位g
Mw: float = 10.00  # 施力物质量mw 单位g

# 路径定义
DATA_PATH: list[str] = ['data/' + i for i in ['exp1-2-1.csv', 'exp1-2-2.csv']]  # 实验数据路径：小滑块数据路径，大滑块数据路径
