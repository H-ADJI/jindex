'''
File: linkedin.py
File Created: Monday, 30th January 2023 2:50:54 pm
Author: KHALIL HADJI 
-----
Copyright:  KHALIL HADJI 2023
'''
import re
import httpx
import asyncio
import parsel
from app.utils.constants import JOB_SELECTOR, JOB_TITLE, JOB_URL, JOB_LOCATION, JOB_LISTING_DATE, COMPANY_NAME, COMPANY_URL, JOB_DETAILS_URL, JOB_PAGINATION_URL, HEADERS
from .parse import normalize_text


async def job_pagination(keywords: list[str], locations: list[str], cooldown: float = 15):
    async with httpx.AsyncClient(headers=HEADERS) as client:
        for keyword in keywords:
            for location in locations:
                params = {
                    "keywords": keyword, "location": location
                }
                job_count = 1
                progress = 0
                while job_count > 0:
                    params["start"] = progress
                    response = await client.get(JOB_PAGINATION_URL, params=params)
                    print(f"GET {response.url}")
                    await asyncio.sleep(2)
                    print("-"*20)
                    print(
                        f"request for paginating to {progress} -  status : {response.status_code}")
                    print("-"*20)

                    if response.status_code == 400:
                        break
                    elif response.status_code == 429:
                        print(f"sleeping for {cooldown}")
                        await asyncio.sleep(cooldown)
                    else:
                        progress += 25
                        selectors: parsel.SelectorList[parsel.Selector] = parsel.Selector(
                            response.text).xpath(JOB_SELECTOR)
                        if not selectors:
                            print(
                                f"no more elements, gathered {progress} elemnts")
                            break
                        for selector in selectors:
                            yield dict(
                                title=normalize_text(
                                    selector.xpath(JOB_TITLE).get()),
                                url=normalize_text(
                                    selector.xpath(JOB_URL).get()),
                                location=normalize_text(
                                    selector.xpath(JOB_LOCATION).get()),
                                listing_date=normalize_text(
                                    selector.xpath(JOB_LISTING_DATE).get()),
                                company_name=normalize_text(
                                    selector.xpath(COMPANY_NAME).get()),
                                company_url=normalize_text(
                                    selector.xpath(COMPANY_URL).get()),
                            )
