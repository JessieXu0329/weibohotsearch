# 1_fetch_data.py - 数据采集模块

import sys
import io
import requests
from common import URL, HEADERS

# 解决控制台中文乱码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def fetch_data():
    """获取微博热搜原始数据"""
    print("正在采集微博热搜数据...")
    response = requests.get(URL, headers=HEADERS)
    
    if response.status_code == 200:
        data = response.json()
        hot_list = data.get('data', {}).get('realtime', [])
        print(f"采集成功！共获取到 {len(hot_list)} 条热搜")
        return hot_list
    else:
        print(f"采集失败，状态码: {response.status_code}")
        return None

if __name__ == '__main__':
    hot_list = fetch_data()
    if hot_list:
        print(f"采集到 {len(hot_list)} 条原始数据")