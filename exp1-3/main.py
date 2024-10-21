import data_analyzer
import graphics_generator
from config import DATA_PATH, RESULT_PATH

if __name__ == '__main__':
    # 分析数据，填入表格
    data_analyzer.preprocess(DATA_PATH)

    # 预处理数据
    graphics_generator.preprocess(RESULT_PATH)

    # 生成图表
    graphics_generator.generate_chart()

    # 计算斜率和截距
    graphics_generator.calc_slope()

    # 计算误差
    graphics_generator.calc_deviation()
