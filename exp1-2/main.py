import data_analyzer
from config import M, DATA_PATH

if __name__ == '__main__':
    for m, path in zip(M, DATA_PATH):
        data_analyzer.calc_deviation(m, path)
