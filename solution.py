import pandas as pd
import numpy as np


chat_id = 689680916 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 0.1  
    # порог доходности нового продукта
    threshold = 500   
    # вычисляем t-статистику и p-value
    t_statistic, p_value = st.ttest_1samp(x, threshold, alternative="two-sided")
    return p_value < 2*alpha and x.mean() > threshold
