"""
Scrapes the titles and descriptions of PubMed articles in response to a keyword
"""

def pubmed(keyword, size='10', page='1'):
    """
    Returns the titles and descriptions of PubMed articles (10 per page) in response to a keyword

    Parameter keyword: what keyword to input in the PubMed search
    Precondition: keyword is a non-empty string

    Parameter size (optional): how many results to return
    Precondition: one of '10','20','50','100','200'

    Parameter page (optional): which page to get the results from
    Precondition: page is a numerical string ('1', '2', etc.)
    """

    # specify keyword in URL through user input
    import requests
    url = 'https://pubmed.ncbi.nlm.nih.gov/?term=' + keyword + '&size=' + size + '&page=' + page
    page = (requests.get(url)).text

    # find title text on webpage
    pos = 0
    pos2 = 0
    titles = []
    while 'docsum-title' in page[pos:]:
        title_start = page.find('docsum-title',pos)
        title = page.find('>',title_start)+1
        title_end = page.find('</a>',title)
        article_title = page[title:title_end]
        result = article_title.strip()

        if '<' in result:
            while '<' in result:
                stripStart = result.find('<',pos2)
                stripEnd = result.find('>',stripStart)+1
                delete = result[stripStart:stripEnd]
                result = result.replace(delete,'')
                pos2 = stripStart+1

        titles.append(result)
        pos = title_start+1

    return titles