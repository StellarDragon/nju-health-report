# nju-health-report
南京大学APP每日健康打卡。因为懒得获取并存储cookies，所以采用selenium模拟登录。
~~（自用还考虑什么美观性）~~
# 运行环境
- python3, selenium(chromedriver as example)
- chromedriver安装方式为，确认自己的chrome版本号，然后从如下两个链接之一下载对应版本的driver
```
http://npm.taobao.org/mirrors/chromedriver/
http://chromedriver.storage.googleapis.com/index.html
```
- 下载完毕后，将解压好的chromedriver.exe放入python安装目录的Scripts目录下。
# 使用说明
- 打开nju-health-report.py，在文件中填入统一身份认证用户名，密码，以及打卡位置（中英文均可）
- 运行程序。输出Completed即为结束。
