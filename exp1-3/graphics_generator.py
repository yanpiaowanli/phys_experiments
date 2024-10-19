import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from data_analyzer import L_dist, G, H

# 读取数据
df = pd.read_csv('exp1-3_result.csv')

# 将速度差平方的单位转换为100cm^2/s^2
df_amplified = df.copy()
df_amplified['vi^2-v0i^2'] = df_amplified['vi^2-v0i^2'] / 100  # 单位: 100cm^2/s^2

# 绘制 v^2-v0^2 - s 图像
plt.plot(df_amplified['si'], df_amplified['vi^2-v0i^2'], marker='o')
plt.xlabel('s (cm)')
plt.ylabel('(v^2 - v0^2) (100cm^2/s^2)')
plt.title('v^2-v0^2 - s graph')
plt.grid(True)
plt.show()

# 计算斜率和截距
slope, intercept = np.polyfit(df_amplified['si'], df_amplified['vi^2-v0i^2'], 1)
print(f'The slope of the v^2-v0^2 - s graph is: {slope}')
print(f'The intercept of the v^2-v0^2 - s graph is: {intercept}')

# 根据图像斜率计算加速度
a = slope / 2  # 单位: m/s^2

# 计算真实加速度
a_ = G * (H / L_dist)  # 单位: m/s^2

# 计算a的误差
deviation = abs((a_ - a) / a_) * 100
print(f'The deviation of acceleration is: {deviation:.2g}%')
