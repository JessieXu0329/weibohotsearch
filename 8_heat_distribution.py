# 8_heat_distribution.py - 热度值分布分析

import sys
import io
import pandas as pd

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def show_heat_distribution():
    """显示热度值分布情况"""
    df = pd.read_csv('weibo_hot_search.csv', encoding='utf-8-sig')
    
    # 转换热度值为数值类型
    df['热度值'] = pd.to_numeric(df['热度值'], errors='coerce')
    
    print("=" * 50)
    print("【热度值分布】")
    print("=" * 50)
    print(f"最小值: {df['热度值'].min():,.0f}")
    print(f"最大值: {df['热度值'].max():,.0f}")
    print(f"平均值: {df['热度值'].mean():,.0f}")
    print(f"中位数: {df['热度值'].median():,.0f}")
    print(f"标准差: {df['热度值'].std():,.0f}")
    
    print("\n分位数分布:")
    print(df['热度值'].quantile([0.25, 0.5, 0.75, 0.9]).to_string())
    print("=" * 50)

if __name__ == '__main__':
    show_heat_distribution()