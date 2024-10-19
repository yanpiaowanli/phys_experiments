import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
df = pd.read_csv('exp1_result.csv')

# 将 'a' 列转换为浮点数，并将单位从cm/s^2转换为m/s^2
df['a'] = (df['a'] * (10**-2)).astype(float)

# 计算每三行数据的 'a' 和 'F' 的平均值
df_avg = df.groupby(df.index // 3).mean()

# 绘制 F-a 图像
plt.plot(df_avg['a'], df_avg['F'], marker='o')
plt.xlabel('a (m/s^2)')
plt.ylabel('F (N)')
plt.title('F-a Graph')
plt.grid(True)
plt.show()

# 计算斜率和截距
slope, intercept = np.polyfit(df_avg['a'], df_avg['F'], 1)
print(f'The slope of the F-a graph is: {slope}')
print(f'The intercept of the F-a graph is: {intercept}')

# 真实系统质量 单位g
M_ = 157.35

# 计算m的误差
deviation = abs((M_ - slope * (10 ** 3)) / M_) * 100
print(f'The deviation of system mass is: {deviation:.2g}%')
