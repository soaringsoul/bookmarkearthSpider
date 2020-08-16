import requests
import re
import pandas as pd
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import time
import pprint


# index_url = "https://www.bookmarkearth.com/page?currentPage=1"


class BookmarkSpider(object):
    def __init__(self):
        self.ua = UserAgent()
        self.index_url = "https://www.bookmarkearth.com/page?currentPage=1"

    def main(self):
        pagenums = self.get_pagenums()
        # pagenums = 1
        print("共有【%s】 个页面需要解析" % pagenums)
        url_lst = ["https://www.bookmarkearth.com/page?currentPage=%s" % (i + 1) for i in range(pagenums)]
        bookmarks_lst = []
        for url in url_lst:
            soup = self.start_requests(url)
            bookmarks = self.parse_bookmark(soup)
            print("此页面共获取到%s个书签" % len(bookmarks))
            print('获取到的前五个书签名称为：%s' % bookmarks[:5])
            bookmarks_lst.extend(bookmarks)
            print("\n"*2)
        df = pd.DataFrame(bookmarks_lst, columns=['书签名称', '链接'])
        df = self.bookmarks_clean(df)
        df.to_excel("书签地球%s页_%s.xlsx" % (pagenums, time.strftime("%Y%m%d%H%M%S")), index=False)

    def start_requests(self, url):
        headers = {"User-Agent": self.ua.random}
        response = requests.get(url, headers=headers)
        print("【请求页面】： %s" %  url)
        return BeautifulSoup(response.content, 'lxml')

    def parse_bookmark(self, soup):
        bookmark_lst = soup.find_all(rel='noreferrer nofollow')
        url_pat = r"[a-zA-z]+://[^\s]*"
        bookmarks = []
        for bookmark in bookmark_lst:
            name = bookmark.text
            url = bookmark.attrs.get('href')
            if re.match(url_pat, url) is not None:
                bookmarks.append([name, url])
        return bookmarks


    def get_pagenums(self):
        soup = self.start_requests(self.index_url)
        pagenum_texts = soup.find(attrs={'class': 'white-space'})

        # '当前 1/117页'
        pagenum = pagenum_texts.text.split("/")[-1].strip("页")
        return int(pagenum)

    def bookmarks_clean(self,df):
        urls_count = df['链接'].value_counts()
        urls_count_dict = urls_count.to_dict()
        df['收藏人数'] = df['链接'].apply(lambda x: urls_count_dict.get(x))
        df.sort_values(by=['收藏人数'], ascending=False, inplace=True)
        df.drop_duplicates(['链接'], inplace=True)
        return df


if __name__ == "__main__":
    bookmarkspider = BookmarkSpider()
    bookmarkspider.main()
