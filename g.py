import crawler_funcs

strRoot = input("what website should I start at?  ")
strDomain = input("what domain should I stay in?    ")
print(strRoot)

arLinkTree = [strRoot]
arLinkTree.append(crawler_funcs.getLinks(crawler_funcs.getHTML(strRoot), strDomain)[1])

arFollowed = ['1', '2']
intLevel = 1
arTemp = []

print(arLinkTree)

while True:
    strLink = arLinkTree[intLevel]

    if strLink.find(strDomain) != -1 and not strLink.find(".gif") != -1 and not strLink.find(
            ".jpg") != -1 and not strLink.find(".png") != -1:
        if " ".join(arFollowed).find(strLink) == -1 or intLevel == arLinkTree.index(strLink):

            # get html,links
            arTemp = crawler_funcs.getLinks(crawler_funcs.getHTML(strLink), inDomain=strDomain)
            # print links and indent level
            if " ".join(arFollowed).find(strLink) == -1:
                print("\n\n\n", "    " * (intLevel - 1), arLinkTree[len(arLinkTree) - 1])
                for strTLink in arTemp:
                    if strTLink.find("<") == -1 and strTLink.find(">") == -1:
                        print("    " * intLevel, strTLink)
                arFollowed.append(strLink)
    arTemp.append("1")

    # if first link not already followed add to link tree, followed  else repeat for other links
    for strTLink in arTemp:
        if " ".join(arFollowed).find(strTLink) == -1:
            arLinkTree.append(strTLink)
            arTemp.append("2")
            break

    # if new link found level +1
    if arTemp[len(arTemp) - 1] == "2":
        intLevel += 1

    # if no links remain and level != 0
    elif arTemp[len(arTemp) - 1] == "1" and intLevel != 0:
        intLevel += -1
        arFollowed.append(strLink)
        arLinkTree.pop(len(arLinkTree) - 1)
    elif arTemp[len(arTemp) - 1] == "1" and intLevel == 0:
        print("all links found")
        break
        # print that's all folks
    arTemp = []

input()
