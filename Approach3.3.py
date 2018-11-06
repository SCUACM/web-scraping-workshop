import asyncio
from pyppeteer import launch

async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto('https://twitter.com/elonmusk')
    await asyncio.sleep(1)

    tweet_elements = await page.xpath('//ol[@id="stream-items-id"]//div[@class="content"]')
    comments = await tweet_elements[0].xpath('.//button[contains(@class, "js-actionReply")]//span[@class="ProfileTweet-actionCountForPresentation"]')
    comment_count = await page.evaluate('(elem) => elem.innerHTML',comments[0])

    print(comment_count)
    while True: 
        await asyncio.sleep(1)

asyncio.get_event_loop().run_until_complete(main())