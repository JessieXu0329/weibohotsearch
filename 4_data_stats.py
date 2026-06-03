# 4_data_stats.py - 数据统计摘要

import sys
import io
import pandas as pd

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def show_data_stats():
    """显示数据统计摘要"""
    df = pd.read_csv('weibo_hot_search.csv', encoding='utf-8-sig')
    
    print("=" * 50)
    print("【数据统计摘要】")
    print("=" * 50)
    print(df.describe())
    print("=" * 50)

if __name__ == '__main__':
    show_data_stats()