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
    
    # Sleep a second to allow the page to finish loading any extra info
    await asyncio.sleep(1)

    # Select tweet elements through xpath
    tweet_elements = await page.xpath('//ol[@id="stream-items-id"]//div[@class="content"]')
    # From within our first tweet element (just for now) get the comment count element
    comments = await tweet_elements[0].xpath('.//button[contains(@class, "js-actionReply")]//span[@class="ProfileTweet-actionCountForPresentation"]')
    # Send the comment element we found to chrome to be decoded
    comment_count = await page.evaluate('(elem) => elem.innerHTML',comments[0])
    # comment_count now contains the result of selecting the contents of our comment element
    print(comment_count)
    
    # Loop until we kill the program
    while True: 
        await asyncio.sleep(1)

# Schedule our main function to run
asyncio.get_event_loop().run_until_complete(main())