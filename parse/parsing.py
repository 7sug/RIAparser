import requests
from bs4 import BeautifulSoup as BS
from inserting import inserting


def main_info_taker():
    main_info = {}
    r = requests.get("https://ria.ru/world/")
    html_content = BS(r.content, 'html.parser')
    for i in html_content.find_all("a", "list-item__title"):
        link = i.get("href")
        title = i.get_text()
        main_info[title] = link
    return main_info


def description_taker(main_info):
    desc = {}
    info = []
    for title, link in main_info.items():
        info.clear()
        r = requests.get(link)
        html_content = BS(r.content, "html.parser")
        news_text = html_content.find("div", "article__body").get_text()
        try:
            img = html_content.find("div", "photoview__open")
            img_link = img.get("data-photoview-src")
        except AttributeError:
            img_link = 'no images appeared'
        info.append(link)
        info.append(news_text)
        info.append(img_link)
        desc[title] = info
    return desc


main_info = main_info_taker()
desc = description_taker(main_info)
inserting.data_correcting(desc)


