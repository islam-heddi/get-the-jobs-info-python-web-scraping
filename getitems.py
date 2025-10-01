from bs4 import BeautifulSoup
import requests
import os
html_page = requests.get("https://jobtoday.com/us/jobs-python/ca_los-angeles").text

html_text = BeautifulSoup(html_page, features="lxml")

os.makedirs("out",exist_ok=True)

cards = html_text.find_all("button", class_ = "flex w-full")
for index, card in enumerate(cards):
    company_name= card.find("div", class_ ="jt-text-14 line-clamp-1 text-left font-semibold").text
    job_name = card.find("div", class_="jt-text-20 col-span-2 line-clamp-2 text-left font-semibold text-black").text
    location_name = card.find("div", class_="jt-text-14 text-left").text
    job_description = card.find("p", class_="jt-text-14 line-clamp-3 text-left text-[#929292]").text
    with open(f'./out/job {index}.txt', 'w',encoding="utf-8") as f:
        f.write(f"company name : {company_name} \n")
        f.write(f"job name : {job_name} \n")
        f.write(f"location name : {location_name} \n")
        f.write(f"description: {job_description} \n")
