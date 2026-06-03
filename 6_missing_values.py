# 6_missing_values.py - 缺失值检查

import sys
import io
import pandas as pd

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def check_missing_values():
    """检查缺失值情况"""
    df = pd.read_csv('weibo_hot_search.csv', encoding='utf-8-sig')
    
    print("=" * 50)
    print("【缺失值检查】")
    print("=" * 50)
    missing = df.isnull().sum()
    missing_pct = (missing / len(df)) * 100
    
    missing_df = pd.DataFrame({
        '缺失数量': missing,
        '缺失比例(%)': missing_pct
    })
    
    print(missing_df)
    print(f"\n总缺失值数量: {missing.sum()}")
    print("=" * 50)

if __name__ == '__main__':
    check_missing_values()