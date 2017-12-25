# Programming Computer Vision with Python 练习

## 安装运行环境
```bash
$ pip install --user pipenv
$ pipenv install
```
## 运行脚本
```bash
$ pipenv run python Chapterxx/Scriptxx.py
```

## matplotlib 在 Mac OS 下报错的解决办法

```
RuntimeError: Python is not installed as a framework.
```

修改 ~/.matplotlib/matplotlibrc
```
backend: TkAgg
```

https://stackoverflow.com/questions/21784641/installation-issue-with-matplotlib-python
