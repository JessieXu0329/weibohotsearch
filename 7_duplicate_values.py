# 7_duplicate_values.py - 重复值检查

import sys
import io
import pandas as pd

# 解决控制台及重定向时的中文乱码与表情符号编码问题
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

def check_duplicates():
    """检查重复值情况"""
    df = pd.read_csv('weibo_hot_search.csv', encoding='utf-8-sig')
    
    print("=" * 50)
    print("【重复值检查】")
    print("=" * 50)
    duplicate_count = df.duplicated().sum()
    print(f"重复记录数量: {duplicate_count}")
    
    if duplicate_count > 0:
        print("\n重复记录示例:")
        print(df[df.duplicated(keep='first')].head())
    print("=" * 50)

if __name__ == '__main__':
    check_duplicates()