# 使用方法
## 1.全局
### pip.conf
通过以下命令查询 `pip.conf` 位置：  
```shell
pip -v config list
```

pip 会先在 `index-url` 中寻找符合条件的文件，失败后会尝试在 `extra-index-url` 中寻找。  
根据实际情况，在 `index-url` 或 `extra-index-url` 中添加:  
```
[global]
index-url = https://...
extra-index-url =
    https://...
    file:///...
    https://adhu2018.github.io/simple/
```

### 命令行
```shell
pip config set global.extra-index-url https://adhu2018.github.io/simple/
```

## 2.requirements.txt
```
--index-url https://adhu2018.github.io/simple/
```
或  
```
--extra-index-url https://adhu2018.github.io/simple/
```

## 3.临时
```shell
pip install -i https://adhu2018.github.io/simple/ xxx
```
