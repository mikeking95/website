from requests_html import HTMLSession
from lxml import html
import datetime
from datetime import datetime as dt
import arrow
import scrapy
from myproject.items import CkkItem


def fetch_map(url):
    '''Fetch sitemap and return parsed txt'''
    response=session.get(url)
    return response

def parse_xml(response):
    '''
    Reads the fetched sitemap and checks for new Products
    Returns list of urls added in the last N default(-7) days.
    '''
    urls = response.html.xpath('//loc/text()')
    dates = [arrow.get(date) for date in response.html.xpath('//lastmod/text()')]
    urls_to_crawl=[]
    for x in enumerate(dates):
        if x[1].date() - datetime.timedelta(days=-7) > datetime.date.today():
            urls_to_crawl.append(urls[x[0]])
    return urls_to_crawl

def parse_all(response):
    urls = response.html.xpath('//loc/text()')
    return urls

def get_urls_to_crawl(days=-7):
    '''
    Fetch sitemaps and determine what urls to crawl.
    
    Returns a list of urls to use in the spider.
    '''
    session = HTMLSession()
    kk_sitemap = 'https://knifekits.com/vcom/smproducts.xml'
    hs_sitemap = 'https://holstersmith.com/vcom/smproducts.xml'
    
    kk_urls =  parse_xml(fetch_map(kk_sitemap))
    hs_urls =  parse_xml(fetch_map(hs_sitemap))
    # all_kk = parse_all(fetch_map(kk_sitemap))
    # all_hs = parse_all(fetch_map(hs_sitemap))
    return kk_urls + hs_urls


class CkkSpider(scrapy.Spider):
    name = 'ckk'
    allowed_domains = ['knifekits.com', 'holstersmith.com']
    # session=HTMLSession()
    start_urls = get_urls_to_crawl()
    
    # img_url = f'https://www.{shop}/vcom/'
    # parse thru each of the posts
    def parse(self, response):

        today = dt.today()
        item = CkkItem()
        
        # item["raw_desc"]= response.xpath('//div[@itemprop="description"]').get()
        txt  = response.xpath('//div[@itemprop="description"]/descendant-or-self::*/text()').getall()
        desc_txt = [t.strip() for t in txt if len(t)>2]
        
        item["crawl_date"]= today.strftime('%Y-%m-%d')
        item['description']  = [x for x in desc_txt if len(x)>0]
        item["price"]= response.xpath('//*[@itemprop="price"]/@content').get()
        item["sku"]= response.xpath(".//*[@itemprop='model']/text()").get()
        item["metaKeywords"]  = response.xpath(".//meta[@name='keywords']/@content").get()
        item["breadcrumbs"] = response.xpath('//*[@class="breadcrumb"]/descendant::text()').getall()[2::2]
        
        item["image"]  = response.xpath('.//div[@class="piGalMain"]/img/@src').get()
        item["images"]  = response.xpath('//*[@data-target="#image-gallery"]/@data-image').getall()
        item["category"]  = item["breadcrumbs"][1]
        item["subcategory"]= item["breadcrumbs"][2]
        item["name"]  = response.xpath('//h1/descendant::span[@itemprop="name"]/text()').get()
        item["url"] = response.url
        
        yield item
    