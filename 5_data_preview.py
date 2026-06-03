# 5_data_preview.py - 前50行数据预览

import sys
import io
import pandas as pd

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def show_data_preview():
    """显示前50行数据"""
    df = pd.read_csv('weibo_hot_search.csv', encoding='utf-8-sig')
    
    print("=" * 50)
    print("【前50行数据预览】")
    print("=" * 50)
    print(df.head(50).to_string())
    print("=" * 50)

if __name__ == '__main__':
    show_data_preview()