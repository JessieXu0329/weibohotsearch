# 3_data_shape.py - 数据形状预览

import sys
import io
import pandas as pd

# 解决控制台及重定向时的中文乱码与表情符号编码问题
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

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