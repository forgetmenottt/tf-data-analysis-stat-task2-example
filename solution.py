import pandas as pd
import numpy as np
import scipy.stats as st



chat_id = 1372197133 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    varian = np.var(x, ddof=1)
    hiqv1 = st.chi2.ppf(1-alpha/2, x.size-1)
    hiqv2 = st.chi2.isf(1-alpha/2, x.size-1)
    return np.sqrt((x.size-1) * varian / hiqv1) / 6, \
           np.sqrt((x.size-1) * varian / hiqv2) / 6
