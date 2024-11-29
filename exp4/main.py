import warnings

import scripts.data_handler as dh
from data.config import DATA_C1_PATH, DATA_C2_PATH, DATA_C3_PATH, RESULT_C3_PATH

warnings.simplefilter(action='ignore', category=FutureWarning)

if __name__ == '__main__':
    dh.calculate_c1(DATA_C1_PATH)
    dh.calculate_c2(DATA_C2_PATH)
    dh.calculate_c3(DATA_C3_PATH)
