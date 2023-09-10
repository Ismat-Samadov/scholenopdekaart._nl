import scrapy


class LinksSpider(scrapy.spiders.SitemapSpider):
    name = "links"
    allowed_domains = ["scholenopdekaart.nl"]
    sitemap_urls = ["https://scholenopdekaart.nl/sitemap-middelbare-scholen.xml"]

    def parse(self, response):
        yield {
            'href': response.css('a[data-automation-id="button-hoofdstuk-contact"]::attr(href)').get()
        }
