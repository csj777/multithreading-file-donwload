import requests
from tqdm import tqdm
import re


def download(url: str):
    '''
    根据文件下载链接下载文件

    Parameters
    ----------
    url: 文件直链
    '''
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
    }
    try:
        head = requests.head(url, headers=headers)
    except Exception:
        print(f'invalid link!')
        return
    print('downloading......')
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


if '__main__' == __name__:
    url = input('Please input download link: ')
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  #domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$',
        re.IGNORECASE)
    if re.match(regex, url) is not None:
        download(url)
    else:
        print('invalid format!')
    # url = 'http://helloflask.com/downloads/flask-tutorial-2.0.pdf'
