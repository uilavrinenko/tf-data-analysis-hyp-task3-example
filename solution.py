import pandas as pd
import numpy as np
from scipy.stats import ttest_ind, mannwhitneyu, permutation_test


chat_id = 996494546 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    stat, pval = permutation_test((x, y), lambda x, y, axis: np.mean(x, axis=axis) - np.mean(y, axis=axis),vectorized=True,n_resamples=1000,alternative="less")
    return pval < 0.01
