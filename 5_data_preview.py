# 5_data_preview.py - 前50行数据预览

import sys
import io
import pandas as pd

# 解决控制台及重定向时的中文乱码与表情符号编码问题
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

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