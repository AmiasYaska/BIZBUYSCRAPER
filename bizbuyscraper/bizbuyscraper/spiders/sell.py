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

        for page in range(2, 101):
            other_pages_body = {
                "bfsSearchCriteria": {
                    "siteId": 20,
                    "languageId": 10,
                    "categories": "",
                    "locations": [
                        {
                            "geoType": 20,
                            "regionId": "5",
                            "countryCode": "US",
                            "countryId": "US",
                            "stateCode": "CA",
                            "legacyRegionId": 18,
                            "legacyRegionCode": "CA",
                            "metroAreaId": 0,
                            "regionName": "California",
                            "regionNameSeo": "california",
                            "displayName": "California",
                            "geoPinCriteria": ""
                        }
                    ],
                    "excludeLocations": "",
                    "askingPriceMax": 0,
                    "askingPriceMin": 0,
                    "pageNumber": page,
                    "keyword": "",
                    "cashFlowMin": 0,
                    "cashFlowMax": 0,
                    "grossIncomeMin": 0,
                    "grossIncomeMax": 0,
                    "daysListedAgo": 0,
                    "establishedAfterYear": 0,
                    "listingsWithNoAskingPrice": 0,
                    "homeBasedListings": 0,
                    "includeRealEstateForLease": 0,
                    "listingsWithSellerFinancing": 0,
                    "realEstateIncluded": 0,
                    "showRelocatableListings": False,
                    "relatedFranchises": 0,
                    "listingTypeIds": [
                        30,
                        40,
                        80
                    ],
                    "designationTypeIds": "",
                    "sortList": "",
                    "absenteeOwnerListings": 0
                },
                "industriesHierarchy": 10,
                "industriesFlat": 10,
                "bfsSearchResultsCounts": 0,
                "cmsFilteredData": 0,
                "rightRailBrokers": 0,
                "statesRegions": 10,
                "languageTypeId": 10
            }

            yield scrapy.Request(
                url="https://api.bizbuysell.com/bff/v2/BbsBfsSearchResults",
                method="POST",
                body=json.dumps(other_pages_body),
                headers={
                    "Content-Type": "application/json"
                },
                callback=self.parse
            )

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

        for value in values:
            biz_buy_sell = BizbuyscraperItem()

            biz_buy_sell["header"] = value["header"]
            biz_buy_sell["image_url"] = value["img"]
            biz_buy_sell["description"] = value["description"]
            biz_buy_sell["price"] = value["price"]
            biz_buy_sell["business_location"] = value["location"]

            contact_info = value.get("contactInfo", {})

            if contact_info:
                biz_buy_sell["broker_company"] = contact_info.get("brokerCompany", "")
                biz_buy_sell["broker_name"] = contact_info.get("contactFullName", "")
                biz_buy_sell["broker_phone_number"] = contact_info.get("contactPhoneNumber", {}).get("telephone", "")
                biz_buy_sell["broker_photo_url"] = contact_info.get("contactPhoto", "")

            yield biz_buy_sell
