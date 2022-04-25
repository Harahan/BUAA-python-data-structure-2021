from html.parser import HTMLParser
from urllib import request
import pandas as pd


class MyHtmlParse(HTMLParser):
    def __init__(self):
        super(MyHtmlParse, self).__init__()
        self.data = []
        self.tag_judge = 0

    def handle_starttag(self, tag, attrs):
        if tag == 'tr' or tag == 'td':
            self.tag_judge = 1
        if tag == 'p' and self.tag_judge == 1:
            self.tag_judge = 2

    def handle_data(self, data):
        if self.tag_judge == 2:
            self.data.append(data)

    def handle_endtag(self, tag):
        if tag != 'p':
            self.tag_judge = 0


html = request.urlopen("http://scse.buaa.edu.cn/bkspy/kkml.htm").read().decode('utf-8')
parser = MyHtmlParse()
parser.feed(html)
dict = {}
for i in range(7):
    dict[parser.data[i]] = []
i += 1
print(i)
while i < len(parser.data):
    for key in dict.keys():
        dict[key].append(parser.data[i])
        i += 1
        if key == '姓名' and (dict['序号'][-1] == '56' or dict['序号'][-1] == '57'):
            dict[key][-1] = dict[key][-1] + ' ' + parser.data[i]
            i += 1
df = pd.DataFrame(dict)
writer = pd.ExcelWriter('2018 年本科生开课目录.xlsx')
df.to_excel(writer, sheet_name='2018 年本科生开课目录', index=False)
writer.save()
