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


def getLinks(strPage, strLink):
    intLoc = strPage.find('href="')
    strChar = '"'
    strPTemp = strPage[intLoc + 6:]
    intLoc2 = strPage[intLoc + 7:].find(strChar)
    strTemp = strPTemp[:intLoc2]
    strPReturn = strPage.replace(strTemp, strLink[:strLink.find('.com') + 4] + strTemp, 1)
    while intLoc != -1:
        intLoc = strPTemp.find('href="')
        strChar = '"'
        strPTemp = strPTemp[intLoc + 6:]
        intLoc2 = strPTemp[intLoc + 7:].find(strChar)
        intTarget = 8
        while intLoc2 == 0:
            intLoc2 = strPTemp[intLoc + intTarget:].find(strChar)
            intTarget += 1
        strTemp = strPTemp[:intLoc2]
        if strPReturn.find(strLink[:strLink.find('.com') + 4] + strTemp) == -1:
            if strTemp[0] != "/":
                strPReturn = strPReturn.replace(strTemp, strLink[:strLink.find('.com') + 4] + "/" + strTemp, 1)
            else:
                strPReturn = strPReturn.replace(strTemp, strLink[:strLink.find('.com') + 4] + strTemp, 1)

    return strPReturn

# tHIS IS THE IMPORTANT PART




def srcChange(strPage, strLink):
    # first run through
    intLoc1 = strPage.find("src=") + 4
    strSlice = strPage[intLoc1:]
    strChar = strSlice[0]
    strCL = strSlice[1:strSlice.find(strChar, 1)]
    if strCL.find(".com") == -1:
        strFL = strLink[:strLink.find(".com") + 4] + strCL
    else:
        strFL = strCL
    strNP = strPage.replace(strCL, strFL)
    #  other run through
    while intLoc1 != 3:
        intLoc1 = strSlice.find("src=") + 4
        strSlice = strSlice[intLoc1:]
        strChar = strSlice[0]
        strCL = strSlice[1:strSlice.find(strChar, 1)]
        if strCL.find(".com") == -1:
            strFL = strLink[:strLink.find(".com") + 4] + strCL
        else:
            strFL = strCL
        strNP = strNP.replace(strCL, strFL)

    return strNP
