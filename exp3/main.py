import warnings

import scripts.data_handler as dh
import scripts.charting_toolkit as ct
from data.config import DATA_C1_PATH, DATA_C2_PATH, DATA_C3_PATH, RESULT_C3_PATH, OUTPUT_PATH

warnings.simplefilter(action='ignore', category=FutureWarning)

if __name__ == '__main__':
    k, I0 = dh.calculate_c1(DATA_C1_PATH)
    dh.calculate_c2(DATA_C2_PATH, k, I0)
    dh.calculate_c3(DATA_C3_PATH, k)
    ct.generate_chart(RESULT_C3_PATH, OUTPUT_PATH)
