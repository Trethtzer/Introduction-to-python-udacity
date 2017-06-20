
import time

def continue_crawl(search_history, target_url, max_steps = 25) :
    #CONTINUE_CRAWL return true if we should continue searching.
    if len(search_history) > max_steps or target_url in search_history or "https://en.wikipedia.org/wiki/Philosophy" == target_url:
        return False
    return True


def web_crawl() :
    article_chain = []
    target_url = "https://es.wikipedia.org/wiki/Pachycephalosaurus"
    while continue_crawl(article_chain,target_url) :
        article_chain.append(target_url)
        time.sleep(2)
        target_url = obtainUrl()
    article_chain.append(target_url)