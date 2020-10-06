from requests_html import HTMLSession

def get_price(url):
    session = HTMLSession()
    r=session.get(url)

    # Wait for js to render
    r.html.render(sleep=1)

    d = r.html.xpath('//*[@data-template-name="productDescription"]/descendant-or-self::text()').text.split(),
    product = {
        'title': r.html.xpath('//*[@id="productTitle"]/text()', first=True).strip(),
        'price': r.html.xpath('//*[@id="priceblock_ourprice"]', first=True).text,
        'description': [x.strip() for x in d]
        'ASIN': r.html.xpath('//*[@id="detailBullets_feature_div"]/ul/li[3]/span/span[2]/text()', first=True),
    
    }
    print(product)
    return product

