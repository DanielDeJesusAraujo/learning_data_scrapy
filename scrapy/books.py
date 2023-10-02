import requests
import parsel
import os

status = {
    'maped_urls': '>>> mapped urls 0',
    'scraping_data': '>>> scraping data: 0.0%',
}


def show_status():
    os.system('clear')
    print(status['maped_urls'])
    print(status['scraping_data'])


def getThumbsUrls(url: str):
    # print('>>> getThumbsUrls')
    response = requests.get(url)
    selector = parsel.Selector(text=response.text)
    artcles_urls = selector.css('.image_container a::attr(href)').getall()
    buttonNext = selector.css('.next a::attr(href)').get()

    return {
        'artcles_urls': artcles_urls,
        'nextUrl': buttonNext
    }


def getAllThumbUrls():
    # print('>>> getAllThumbUrls')
    allThumbs = []
    page = 'https://books.toscrape.com/catalogue/page-1.html'
    hasNextPage = True

    while hasNextPage:
        # print(page)
        response = getThumbsUrls(page)
        allThumbs.extend(response['artcles_urls'])

        status['maped_urls'] = f'>>> mapped urls {len(allThumbs)}'
        show_status()
        if response['nextUrl'] == None:
            hasNextPage = False
        page = f'https://books.toscrape.com/catalogue/{response["nextUrl"]}'
    return allThumbs


def getBookInfo(url):
    # print('>>> getBookInfo')
    book_page = requests.get(url)
    selector = parsel.Selector(text=book_page.text)
    title = selector.css('.product_main h1::text').get()
    price = selector.css('.product_main p.price_color::text').get()

    return {
        'title': title,
        'price': price,
    }


def getAllBookInfos():
    # print('>>> getAllBookInfos')
    booksUrl = getAllThumbUrls()
    allBooksInfos = []

    for index in range(len(booksUrl)):
        bookInfo = getBookInfo(f'https://books.toscrape.com/catalogue/{booksUrl[index]}')
        allBooksInfos.extend(bookInfo)
        status['scraping_data'] = f'>>> scraping data: {(index * 100) / len(booksUrl)}%'
        show_status()


getAllBookInfos()
