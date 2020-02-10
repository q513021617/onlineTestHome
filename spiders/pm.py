import requests
from bs4 import BeautifulSoup
import bs4


def getHTMLText(url):
    try:
        r = requests.get(url)
        # r.raise_for_status
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("获取html异常")
        return ""


def fillUnivList(univList, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find("tbody").children:
        if isinstance(tr, bs4.element.Tag):  # tobody有的节点是空串，属于要判断类型进行过滤
            tds = tr("td")  # 等价于tr.find_all("td")
            univList.append([tds[0].string, tds[1].string, tds[2].string])  # NavigableString可以跨越多个层次


def printUnivList(univList, num):
    tplt = "{0:^6}\t{1:^10}\t{2:^6}"  #:前的数字说明使用format函数的第几个参数填充模板
    print(tplt.format("排名", "学校名称", "总分", chr(12288)))
    for i in range(num):
        u = univList[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288)))


if __name__ == '__main__':

    url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html"
    html = getHTMLText(url)
    univList = []
    fillUnivList(univList, html)
    printUnivList(univList, 20)

