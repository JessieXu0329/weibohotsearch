# 3_data_shape.py - 数据形状预览

import sys
import io
import pandas as pd

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def show_data_shape():
    """显示数据形状（行数、列数）"""
    df = pd.read_csv('weibo_hot_search.csv', encoding='utf-8-sig')
    
    print("=" * 50)
    print("【数据形状预览】")
    print("=" * 50)
    print(f"数据行数: {df.shape[0]} 行")
    print(f"数据列数: {df.shape[1]} 列")
    print(f"列名列表: {list(df.columns)}")
    print("=" * 50)

if __name__ == '__main__':
    show_data_shape()