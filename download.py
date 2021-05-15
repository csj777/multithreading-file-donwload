import requests

url = 'https://github.com/Wox-launcher/Wox/releases/download/v1.4.1196/Wox-1.4.1196.exe'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}

print('downloading......')

response = requests.get(url, headers=headers)
content = response.content

file_name = url.split('/')[-1]
with open(file_name, mode='wb') as f:
    f.write(content)
print(f'download complete! your filename:{file_name}')
