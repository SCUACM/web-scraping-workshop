from lxml import html
import requests

page = requests.get('https://twitter.com/elonmusk')
tree = html.fromstring(page.content)
comments_text = tree.xpath('//ol[@id="stream-items-id"]//div[@class="content"]')[0]

print(comments_text)
print(comments_text.text)