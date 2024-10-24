import warnings
import scripts.data_calculator as dc
from data.config import M, DATA_PATH

warnings.simplefilter(action='ignore', category=FutureWarning)

if __name__ == '__main__':
    for m, path in zip(M, DATA_PATH):
        dc.calc_deviation(m, path)
