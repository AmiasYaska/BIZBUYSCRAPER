import scrapy
from ..items import BizbuyscraperItem
import json


class SellSpider(scrapy.Spider):
    name = "sell"
    allowed_domains = ["bizbuysell.com"]

    def start_requests(self):
        page1_body = {
            "bfsSearchCriteria": {
                "siteId": 20,
                "languageId": 10,
                "seoName": "/california-businesses-for-sale/",
                "queryString": "q=bHQ9MzAsNDAsODA%3D"
            },
            "industriesHierarchy": 0,
            "industriesFlat": 0,
            "bfsSearchResultsCounts": 0,
            "cmsFilteredData": 0,
            "rightRailBrokers": 0,
            "statesRegions": 10,
            "languageTypeId": 10
        }

        yield scrapy.Request(
            url="https://api.bizbuysell.com/bff/v2/BbsBfsSearchResults",
            method="POST",
            body=json.dumps(page1_body),
            headers={
                "Content-Type": "application/json"
            },
            callback=self.parse
        )

    def parse(self, response):
        data = json.loads(response.body)
        values = data.get("value").get("bfsSearchResult").get("value")
        print(values)

        # for value in values:
        #     biz_buy_sell = BizbuyscraperItem()
        #
        #     biz_buy_sell["header"] = value["header"]
        #     biz_buy_sell["image_url"] = value["img"]
        #     biz_buy_sell["description"] = value["description"]
        #     biz_buy_sell["price"] = value["price"]
        #     biz_buy_sell["business_location"] = value["location"]
        #     biz_buy_sell["broker_company"] = value["contactInfo"]["brokerCompany"]
        #     biz_buy_sell["broker_name"] = value["contactInfo"]["contactFullName"]
        #     biz_buy_sell["broker_phone_number"] = value["contactInfo"]["contactPhoneNumber"]["telephone"]
        #     biz_buy_sell["broker_photo_url"] = value["contactInfo"]["contactPhoto"]
        #
        #     yield biz_buy_sell
