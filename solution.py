import pandas as pd
import numpy as np


chat_id = 996494546 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    stat, pval = mannwhitneyu(x, y, alternative=alternative)
    return pval < 0.01
