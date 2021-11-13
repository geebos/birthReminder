# 生日提醒订阅服务
## 使用方法
### 提交 MR
- 编辑项目下的 `birthday.txt`文件
- 追加一行，总共三个参数，每个参数之间通过空格分开：
  - 生日日期，例如1月1号生日，则填 0101
  - 生日日期类型：1表示阴历，2表示阳历
  - 邮箱加密后的字符串，复制公钥到在线网站上对邮箱进行加密，防止邮箱被搜索引擎收录
    - 加密网站：http://www.metools.info/code/c81.html
    - 公钥：
      ```text
      -----BEGIN RSA PUBLIC KEY-----
      MIIBCgKCAQEAhXag/mVU+OeP9bbY3O6i5OwJioP/LvGjmPkqwj8SvY8jkaZiSDWJ
      76uPr9HAGVipDzjOG3eZPBTsFnJg+eWjbEVogk8QttFkn5VWxwa2hVCAkv9AKmLK
      qDLpYmUmKmOnN96z+xr50pUf3VtjHFGSF2xogr567k5ZMYqaQHUjYKpdH8MS4kgN
      ibqIMlzcSMhra0sUKgY2w2Tcs0aFx3tXPTg7OkCA5x0sPlfi+Ns410F+E6O9ywfy
      u9eh0yolN0w1fJAfMM9Hxgl8YsG7bWCQ4354UWTAmryLZT23Prb3mXfTMplJdr2t
      TQszshWXhqAkntCnlFT0jAYU4c42NVov/QIDAQAB
      -----END RSA PUBLIC KEY-----
      ```
- 编辑完之后提交修改即可
### fork项目
- 将项目 fork到自己的账号下
- 然后将项目 clone到本地
- 安装依赖 `pip3 install -r requirements.txt`
- 进入项目目录执行 `python3 add_record.py`
- 提交交更改
- push到 github