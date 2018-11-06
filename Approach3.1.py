import asyncio
from pyppeteer import launch

async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto('https://twitter.com/elonmusk')
    await page.evaluate('''() => alert('Page opened!')''')
    while True: 
        await asyncio.sleep(1)

asyncio.get_event_loop().run_until_complete(main())