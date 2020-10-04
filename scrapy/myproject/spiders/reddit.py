# spiders/__init__.py

from datetime import datetime as dt
import scrapy
from myproject.items import RedditItem

class PostSpider(scrapy.Spider):
    name = 'reddite'
    allowed_domains = ['reddit.com']

    reddit_urls = [
        ('datascience', 'week'),
        ('python', 'week'),
        ('programming', 'week'),
        ('machinelearning', 'week')
    ]

    start_urls = ['https://www.reddit.com/r/' + sub + '/top/?sort=top&t=' + period for sub, period in reddit_urls]

    def parse(self, response):
        # get the subreddit from the URL
        sub = response.url.split('/')[4]

        # parse thru each of the posts
        for post in response.css('div.thing'):
            item = RedditItem()

            item['date'] = dt.today()
            item['date_str'] = item['date'].strftime('%Y-%m-%d')
            item['sub'] = sub
            item['title'] = post.css('a.title::text').extract_first()

            item['url'] = post.css('a.title::attr(href)').extract_first()
            ## if self-post, add reddit base url (as it's relative by default)
            if item['url'][:3] == '/r/':
                item['url'] = 'https://www.reddit.com' + item['url']

            item['score'] = int(post.css('div.unvoted::text').extract_first())
            item['commentsUrl'] = post.css('a.comments::attr(href)').extract_first()

            yield item
            