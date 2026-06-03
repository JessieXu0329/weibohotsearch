# common.py - 公共配置文件

# 数据接口地址
URL = 'https://weibo.com/ajax/side/hotSearch'

# 请求头配置（伪装浏览器绕过反爬）
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Referer': 'https://weibo.com/',
    'Cookie': 'ULV=1761889354149:5:3:2:9344196075930.742.1761889354147:1761888815728; XSRF-TOKEN=jaMHSReIBmakX0Ik-oIciXW1; PC_TOKEN=6cc6bbebb4; SCF=AoPJaohCP7KBjfaBj0DS2PwV2ySvZ8bTEYNpvGv6dzD5j1ltiNKewXufNHoIwj-0LADBHOAuSk8OvstNpEBRjbg.; SUB=_2A25HG8PRDeRhGeBO7VoS8i_LzDmIHXVkWVkZrDV8PUNbmtB-LXijkW9NRcyxpxYKXibhnTl5_AZpQDsw0C1-nBlW; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWkejUNcy-gGXUin_xOoAm15JpX5KzhUgL.Foq7Son0eo2NS0-2dJLoI7_Z9PS0PfHVIPUNd7tt; ALF=02_1783054465; WBPSESS=kQPD-RNHDbIYmZz1BqfvFeOze9Ez5ImNEDzoGeDH1WmzRYjbozGyrQM-Yp6oN4-Yv_MHk1ve7qSSuvQ5UkXdjle97t7f1C9v5MVktC1m6tIlSOOyEit-DtYE1xWbtoDhZaVTRJDzqu_gaf6a4JZ27w=='
}