import ssl
import urllib.request


def getHTML(strUrl):
    if strUrl.find("<") == -1 and strUrl.find(">") == -1:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        req = urllib.request.Request(strUrl, headers={'User-Agent': 'Chrome/35.0.1916.47'})
        page = urllib.request.urlopen(req, context=ctx)
        strPage = page.read().decode("UTF-8")
        return strPage


def getLinks(strPage, inDomain="."):
    arLinks = []
    arTemp = []
    arPage = strPage.split('"')
    for strItem in arPage:
        if strItem.find("://www.") != -1 or strItem.find("'/") != -1:
            if strItem.find(">") != -1 or strItem.find("<") != -1 or strItem.find("a href=") != -1 or strItem.find(" ") != -1:
                arNew = strItem.split("'")
                for strNewItem in arNew:
                    if strNewItem.find("://www.") != -1 or strItem.find("'/") != -1:
                        arTemp.append(strNewItem)
            else:
                arTemp.append(strItem)
    for strTItem in arTemp:
        if strTItem.find("://www.") != -1:
            arLinks.append(strTItem)
        elif inDomain != "." and strTItem.find("/") != -1 and strTItem.find("<") == -1 and strTItem.find(
                "div") == -1 and strTItem.find(">") == -1:
            if strPage.find("https://") != -1 and strTItem.find(" ") == -1:
                arLinks.append("https://www." + inDomain + strTItem)
            else:
                arLinks.append("http://www." + inDomain + strTItem)

    return arLinks
