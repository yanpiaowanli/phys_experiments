import data_analyzer
import graphics_generator
from config import DATA_PATH, RESULT_PATH


if __name__ == '__main__':
    # 预处理数据，填入表格
    data_analyzer.preprocess(path=DATA_PATH)

    # 预处理数据，对表格数据进一步处理
    graphics_generator.preprocess(path=RESULT_PATH)

    # 生成图表
    graphics_generator.generate_chart()

    # 计算斜率
    graphics_generator.calc_slope()

    # 计算误差
    graphics_generator.calc_deviation()
