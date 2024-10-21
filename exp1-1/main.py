import scripts.data_calculator as dc
import scripts.charting_toolkit as ct
from data.config import DATA_PATH, RESULT_PATH, OUTPUT_PATH


if __name__ == '__main__':
    # 预处理数据，填入表格
    dc.preprocess(path=DATA_PATH)

    # 预处理数据，对表格数据进一步处理
    ct.preprocess(path=RESULT_PATH)

    # 生成图表
    ct.generate_chart(path=OUTPUT_PATH)

    # 计算斜率
    ct.calc_slope()

    # 计算误差
    ct.calc_deviation()
