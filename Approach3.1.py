# Library for core routines
import asyncio
# Library for controlling chrome
from pyppeteer import launch

# Define our main function
async def main():
    # Create new browser and page
    browser = await launch(headless=False)
    page = await browser.newPage()

    # Send chrome to our url
    await page.goto('https://twitter.com/elonmusk')
    # Once the page is loaded, execute some JavaScript
    await page.evaluate('''() => alert('Page opened!')''')
    
    # Loop until we kill the program
    while True: 
        await asyncio.sleep(1)

# Schedule our main function to run
asyncio.get_event_loop().run_until_complete(main())