# Library for parsing html into a python tree
from lxml import html
# Library for fetching pages from the internet
import requests

# Fetch the html for the page
page = requests.get('https://twitter.com/elonmusk')
# parse the html into a python tree
tree = html.fromstring(page.content)
# Get an element from our python tree using xPath selection
comments_text = tree.xpath('//ol[@id="stream-items-id"]//div[@class="content"]')[0]

# Print our findings
print(comments_text)
print(comments_text.text)