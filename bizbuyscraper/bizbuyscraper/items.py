# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst


class BizbuyscraperItem(scrapy.Item):
    header = scrapy.Field(
        output_processor=TakeFirst()
    )

    image_url = scrapy.Field(
        output_processor=TakeFirst()
    )

    description = scrapy.Field(
        output_processor=TakeFirst()
    )

    price = scrapy.Field(
        output_processor=TakeFirst()
    )

    location = scrapy.Field(
        output_processor=TakeFirst()
    )

    broker_company = scrapy.Field(
        output_processor=TakeFirst()
    )

    broker_name = scrapy.Field(
        output_processor=TakeFirst()
    )

    broker_phone_number = scrapy.Field(
        output_processor=TakeFirst()
    )

    broker_photo_url = scrapy.Field(
        output_processor=TakeFirst()
    )


