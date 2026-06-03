# 10_data_cleaning.py - 数据清洗模块

import sys
import io
import pandas as pd

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def data_cleaning():
    """执行数据清洗"""
    df = pd.read_csv('weibo_hot_search.csv', encoding='utf-8-sig')
    original_count = len(df)
    
    # 转换热度值为数值类型
    df['热度值'] = pd.to_numeric(df['热度值'], errors='coerce')
    
    print("=" * 50)
    print("【数据清洗】")
    print("=" * 50)
    
    # 1. 重复值处理
    duplicates = df.duplicated().sum()
    if duplicates > 0:
        df = df.drop_duplicates()
        print(f"\n1. 重复值处理: 删除 {duplicates} 条重复记录")
    else:
        print(f"\n1. 重复值处理: 无重复记录")
    
    # 2. 缺失值处理
    missing_before = df.isnull().sum().sum()
    if missing_before > 0:
        # 话题词缺失的行直接删除
        df = df.dropna(subset=['话题词'])
        # 热度值缺失的用中位数填充
        if df['热度值'].isnull().sum() > 0:
            median_heat = df['热度值'].median()
            df['热度值'] = df['热度值'].fillna(median_heat)
        # 标签缺失的用"无"填充
        if '标签' in df.columns and df['标签'].isnull().sum() > 0:
            df['标签'] = df['标签'].fillna('无')
        print(f"\n2. 缺失值处理: 处理前 {missing_before} 个缺失值")
    else:
        print(f"\n2. 缺失值处理: 无缺失值")
    
    # 3. 异常值处理
    abnormal_before = len(df[(df['热度值'] < 0) | (df['热度值'] > 10000000)])
    if abnormal_before > 0:
        df = df[(df['热度值'] >= 0) & (df['热度值'] <= 10000000)]
        print(f"\n3. 异常值处理: 删除 {abnormal_before} 条热度值异常记录")
    else:
        print(f"\n3. 异常值处理: 无异常值")
    
    # 清洗结果统计
    final_count = len(df)
    print(f"\n4. 清洗结果汇总:")
    print(f"   - 清洗前记录数: {original_count}")
    print(f"   - 清洗后记录数: {final_count}")
    print(f"   - 删除记录数: {original_count - final_count}")
    
    # 保存清洗后的数据
    df.to_csv('weibo_hot_search_cleaned.csv', index=False, encoding='utf-8-sig')
    print(f"\n清洗后的数据已保存至: weibo_hot_search_cleaned.csv")
    print("=" * 50)

if __name__ == '__main__':
    data_cleaning()