import scrapy
import json

class SellSpider(scrapy.Spider):
    name = "sell"
    allowed_domains = ["bizbuysell.com"]

    def start_requests(self):
        url_body = {
            "bfsSearchCriteria": {
                "siteId": 20,
                "languageId": 10,
                "categories": [],
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
                        "geoPinCriteria": []
                    }
                ],
                "excludeLocations": [],
                "askingPriceMax": 0,
                "askingPriceMin": 0,
                "pageNumber": 2,
                "keyword": [],
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
                "designationTypeIds": [],
                "sortList": [],
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
            body=json.dumps(url_body),
            headers={
                "Content-Type": "application/json"
            },
            callback=self.parse
        )

    def parse(self, response):
        data = json.loads(response.body)
        values = data.get("value").get("bfsSearchResult").get("value")

        for i in values:
            yield {
                "header": i.get("header"),
                "description": i.get("")
            }
