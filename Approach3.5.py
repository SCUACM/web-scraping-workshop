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

    # Scroll down a few times to load more tweets
    pages = 10
    for i in range(pages):
        # Evaluate some JavaScript to scroll to the bottom of the page
        await page.evaluate('() => window.scrollTo(0,document.body.scrollHeight)')
        # Wait a second between scrolls to allow more tweets to be loaded
        await asyncio.sleep(1)

    tweets = []

    # Select the tweet elements from the page
    tweet_elements = await page.xpath('//ol[@id="stream-items-id"]//div[@class="content"]')
    
    # Iterate through them and select the data we need
    for elem in tweet_elements:
        # Select the element handles we need
        title = await elem.xpath('.//strong[contains(@class, "fullname")]')
        comments = await elem.xpath('.//button[contains(@class, "js-actionReply")]//span[@class="ProfileTweet-actionCountForPresentation"]')
        retweets = await elem.xpath('.//button[contains(@class, "js-actionRetweet")]//span[@class="ProfileTweet-actionCountForPresentation"]')
        likes = await elem.xpath('.//button[contains(@class, "js-actionFavorite")]//span[@class="ProfileTweet-actionCountForPresentation"]')
        
        # Decode each handle, getting its text value
        name_value = await page.evaluate('(elem) => elem.innerHTML',title[0])
        comment_count = await page.evaluate('(elem) => elem.innerHTML',comments[0])
        retweet_count = await page.evaluate('(elem) => elem.innerHTML',retweets[0])
        like_count = await page.evaluate('(elem) => elem.innerHTML',likes[0])

        # Commit the data we got from this tweet to our list. We use a tuple here because of convension.
        tweets.append((name_value, comment_count, retweet_count, like_count))

    print(tweets)
    
    # Allow our browser to close gracefully
    await browser.close()

# Schedule our main function to run
asyncio.get_event_loop().run_until_complete(main())