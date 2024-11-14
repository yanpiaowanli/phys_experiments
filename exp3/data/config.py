# 实验常量定义
M_cylinder = 0.88473  # 圆柱质量m 单位kg
M_barrel = 0.66562  # 圆筒质量m 单位kg
M_sphere = 1.14042  # 球体质量m 单位kg

# 无需修改的常量定义
Iz = 0.179*1e-4  # 球支座转动惯量实验值Iz 单位kg*m^2
I5_ = 0.809*1e-4  # 二滑块质心轴转动惯量理论值I5' 单位kg*m^2
M_2 = 0.477  # 二滑块质量2m 单位kg

DELTA_T = 0.002  # 仪器允差Δ 单位s
C = 3 ** 0.5  # 置信系数C 无量纲


# 路径定义
DATA_C1_PATH = 'data/exp3-1.csv'  # 实验3数据路径1
DATA_C2_PATH = 'data/exp3-2.csv'  # 实验3数据路径2
DATA_C3_PATH = 'data/exp3-3.csv'  # 实验3数据路径3

RESULT_C1_PATH = 'output/exp3-1_result.csv'  # 实验3结果输出路径1
RESULT_C2_PATH = 'output/exp3-2_result.csv'  # 实验3结果输出路径2
RESULT_C3_PATH = 'output/exp3-3_result.csv'  # 实验3结果输出路径3

OUTPUT_PATH = 'output/fig3.png'  # 实验3图表输出路径
