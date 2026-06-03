# 2_parse_and_save.py - 数据解析与存储模块

import sys
import io
import csv
from datetime import datetime
from common import URL, HEADERS
import requests

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def fetch_data():
    """获取原始数据"""
    response = requests.get(URL, headers=HEADERS)
    if response.status_code == 200:
        data = response.json()
        return data.get('data', {}).get('realtime', [])
    return None

def parse_data(hot_list):
    """解析数据，提取所需字段"""
    results = []
    for i, item in enumerate(hot_list):
        record = {
            '排名': i + 1,
            '话题词': item.get('word', ''),
            '热度值': item.get('raw_hot') or item.get('hot', ''),
            '标签': item.get('flag_desc', ''),
            '类别': item.get('category', ''),
            '采集时间': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        results.append(record)
    return results

def save_to_csv(data, filename='weibo_hot_search.csv'):
    """保存为CSV文件"""
    if not data:
        print("无数据可保存")
        return False
    
    with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=['排名', '话题词', '热度值', '标签', '类别', '采集时间'])
        writer.writeheader()
        writer.writerows(data)
    
    print(f"数据已保存至: {filename}")
    return True

if __name__ == '__main__':
    hot_list = fetch_data()
    if hot_list:
        parsed_data = parse_data(hot_list)
        save_to_csv(parsed_data)
        print(f"共解析并保存 {len(parsed_data)} 条数据")