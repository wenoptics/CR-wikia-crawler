import urllib.request

def get_html_string(url):
    # use iPhone
    user_agent = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'

    headers = {'User-Agent': user_agent}

    data = None  # urllib.parse.urlencode(values)

    req = urllib.request.Request(url, data, headers)

    response = urllib.request.urlopen(req)
    the_page = response.read()

    return the_page

