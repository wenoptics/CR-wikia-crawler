import socket
from http.client import RemoteDisconnected
from http.cookiejar import CookieJar
import urllib
from urllib.error import URLError
from urllib.parse import urlencode


class WCrawl:
    def __init__(self):

        self._opener = None
        self.responseDecode = 'utf-8'

        ''' 接受Cookie，使用cookieJar '''
        cj = CookieJar()
        self._opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        self._opener.addheaders = [
            ('user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36')
        ]

    def open_url(self, url, postDataDict=None, timeout=None, retry=3):
        """
        用这个loginSession打开url
        :param retry:
        :param timeout:
        :param url: 要打开的url
        :param postDataDict: 如果是post方式，要传进来
        :return: 返回response
        """
        for _ in range(retry):

            try:
                if postDataDict is None:
                    ''' GET '''
                    response = self._opener.open(url, timeout=timeout)
                else:
                    ''' POST '''
                    postData = urlencode(postDataDict)
                    ''' python3要求POST的data是byte，所以encode一下'''
                    postData = postData.encode('ascii')
                    response = self._opener.open(url, postData, timeout=timeout)

                ''' 处理Response '''
                response = response.read()
                return response
            except RemoteDisconnected:
                continue
            except socket.timeout:
                continue
            except URLError:
                continue

        print('[e]timeout')
        raise TimeoutError('timeout after retry %d times' % retry)

    def decode(self, text):
        return text.decode(self.responseDecode)
