import warnings
import scripts.data_calculator as dc
import scripts.charting_toolkit as ct
from data.config import DATA_PATH, RESULT_PATH, OUTPUT_PATH

warnings.simplefilter(action='ignore', category=FutureWarning)

if __name__ == '__main__':
    # 计算数据，填入表格
    dc.preprocess(DATA_PATH)

    # 预处理数据
    ct.preprocess(RESULT_PATH)

    # 生成图表
    ct.generate_chart(OUTPUT_PATH)

    # 计算斜率和截距
    ct.calc_slope()

    # 计算误差
    ct.calc_deviation()
