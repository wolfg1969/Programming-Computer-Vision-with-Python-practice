# Programming Computer Vision with Python 练习

## 安装运行环境
```bash
$ wget http://programmingcomputervision.com/downloads/pcv_data.zip
$ unzip pcv_data.zip
$ git clone https://github.com/wolfg1969/Programming-Computer-Vision-with-Python-practice.git
$ cd Programming-Computer-Vision-with-Python-practice
$ pip install --user pipenv
$ pipenv install
$ cd PCV
$ pipenv run python setup.py install
```
## 运行脚本
```bash
$ cd Programming-Computer-Vision-with-Python-practice
$ pipenv run python PCV/examples2/ch1_image_representation.py
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
