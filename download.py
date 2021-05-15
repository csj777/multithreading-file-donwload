import requests
from tqdm import tqdm

url = 'http://helloflask.com/downloads/flask-tutorial-2.0.pdf'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}

print('downloading......')

head = requests.head(url, headers=headers)
file_size = head.headers.get('Content-Length')
if file_size is not None:
    file_size = int(file_size)

file_name = url.split('/')[-1]
response = requests.get(url, headers=headers, stream=True)

size = 1024
bar = tqdm(total=file_size, desc=f'filename {file_name}')
with open(file_name, mode='wb') as f:
    for chunk in response.iter_content(chunk_size=size):
        f.write(chunk)
        bar.update(size)
bar.close()

print(f'download complete! your filename:{file_name}')
