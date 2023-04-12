import pandas as pd
import numpy as np
from scipy.stats import mannwhitneyu


chat_id = 996494546 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    stat, pval = ttest_ind(x, y, equal_var=False, alternative="less")
    return pval < 0.01
