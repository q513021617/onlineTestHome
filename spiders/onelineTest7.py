import requests as req
import pymysql
import html as xhtmls
from lxml import etree

url="http://wsk.neea.edu.cn/html1/category/1507/1646-1.htm"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
}
response = req.get(url=url, headers=headers)
html = response.content.decode()  # 避免中文乱码
xhtml = etree.HTML(html)


'''
 数据库操作
'''
def conn():
    connection=pymysql.Connect(
        host="111.230.27.166",
        port=3306,
        db="onlineTest_zhiyi",
        user="onlineTest_zhiyi",
        passwd="NnNdHCbTY8sDS7Zi",
        charset="utf8"
    )

    return connection

def execute(titile,time,content):
    data=(titile,time,7,content)
    sql ='insert into news (title,time,type,context) value ("%s","%s","%d","%s")'
    connection=conn()
    cs=connection.cursor()
    cs.execute(sql%data)
    connection.commit()
    connection.close()


titles = xhtml.xpath("//*[@id='ReportIDname']/a/@title")
times = xhtml.xpath("//*[@id='ReportIDIssueTime']/text()")
urls = xhtml.xpath("//*[@id='ReportIDname']/a/@href")


'''
 爬取主页内容
'''
for i in range(0,len(titles)):
    print(titles[i]+' '+times[i]+' '+urls[i])
    urlr = "http://nit.neea.edu.cn"+urls[i]
    resp_article = req.get(url=urlr, headers=headers)
    htmlr = resp_article.content.decode()  # 避免中文乱码
    xhtmlr = etree.HTML(htmlr)
    rcontexts = xhtmlr.xpath('//*[@id="ReportIDtext"]/p/text()')
    print(''.join(rcontexts))
    execute(titles[i],times[i],''.join(rcontexts))




