# 9_tag_distribution.py - 标签分布分析

import sys
import io
import pandas as pd
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

def show_tag_distribution():
    df = pd.read_csv('weibo_hot_search.csv', encoding='utf-8-sig')
    
    print("=" * 50)
    print("【标签分布】")
    print("=" * 50)
    tag_counts = df['标签'].value_counts()
    tag_pct = (tag_counts / len(df)) * 100
    
    tag_df = pd.DataFrame({
        '数量': tag_counts,
        '占比(%)': tag_pct
    })
    print(tag_df)
    print("=" * 50)

if __name__ == '__main__':
    show_tag_distribution()