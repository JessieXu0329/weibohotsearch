# 4_data_stats.py - 数据统计摘要

import sys
import io
import pandas as pd

# 解决控制台及重定向时的中文乱码与表情符号编码问题
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

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