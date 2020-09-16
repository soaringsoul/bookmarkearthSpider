
# bookmarkearthSpider
a spider for crawling bookmark from https://www.bookmarkearth.com/



## 爬取网站简介：

最近发现了一个比较有趣的网站：书签地球,专注于个人书签的分享，你可以看到来自世界各地的人分享的自己收藏的书签，当然，你也可以分享自己的书签。我平时主要用来查找一些电子书资源 ，但是发现很多人都是重复分享，而且人数比较多，一个个筛选很麻烦。

于是写了这个爬虫，将所有书签爬取下来后统计下收藏人数，去重，然后写入到本地excel文件。

这是今天(2020/08/16)爬取的结果,未去重前大概是4.5万条，去重后就只有4000条左右。

有需要的可以直接下载取用

> [书签地球117页_20200816.xlsx免费下载 - 90网盘](https://link.zhihu.com/?target=https%3A//o8.cn/B9MevE) 密码：y070

![书签地球网站首页](/images/bookmarkearthweb.png)

## 如何使用

### 安装依赖

`pip install -r requirements.txt`

### 启动

`python bookmarkspider.py`

![启动](/images/run.gif)
