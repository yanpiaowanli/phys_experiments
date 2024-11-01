import warnings
import scripts.data_calculator as dc
import scripts.charting_toolkit as ct
from data.config import DATA_C1_PATH, DATA_C2_PATH, RESULT_C1_PATH, RESULT_C2_PATH, OUTPUT_PATH

warnings.simplefilter(action='ignore', category=FutureWarning)

if __name__ == '__main__':
    # 计算数据，填入表格，并输出结果
    dc.preprocess_c1(DATA_C1_PATH)
    dc.preprocess_c2(DATA_C2_PATH)

    # 直接计算杨氏模量，并输出结果
    E = dc.calc_youngs_modulus(RESULT_C1_PATH, RESULT_C2_PATH)

    # 生成图表
    ct.generate_chart(RESULT_C1_PATH, OUTPUT_PATH)

    # 作图法计算杨氏模量，并输出误差
    ct.calc_deviation(RESULT_C2_PATH, E)
