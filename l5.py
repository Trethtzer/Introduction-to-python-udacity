
import time
import requests
import bs4
import urllib


def continue_crawl(search_history, target_url, max_steps = 25) :
    #CONTINUE_CRAWL return true if we should continue searching.
    if len(search_history) > max_steps or target_url in search_history or "https://en.wikipedia.org/wiki/Philosophy" == target_url or target_url == None :
        return False
    return True


def find_first_link(url) :
    #Get the HTML
    #Add it to soup
    #find the first link if exists
    #return it
    response = requests.get(url)
    html = response.text
    soup = bs4.BeautifulSoup(html, "html.parser")
    content_div = soup.find(id="mw-content-text")
    article_link = None
    for element in content_div.find_all("p", recursive=False):
        # Find the first anchor tag that's a direct child of a paragraph.
        # It's important to only look at direct children, because other types
        # of link, e.g. footnotes and pronunciation, could come before the
        # first link to an article. Those other link types aren't direct
        # children though, they're in divs of various classes.
        if element.find("a", recursive=False):
            article_link = element.find("a", recursive=False).get('href')
            break
    if not article_link:
        return 
    # Build a full url from the relative article_link url
    first_link = urllib.parse.urljoin('https://en.wikipedia.org/', article_link)
    return first_link


def web_crawl() :
    article_chain = []
    target_url = "https://en.wikipedia.org/wiki/Mathematics"
    print(target_url)
    while continue_crawl(article_chain,target_url) :
        article_chain.append(target_url)
        time.sleep(2)
        target_url = find_first_link(target_url)
        print(target_url)
    article_chain.append(target_url)


web_crawl()