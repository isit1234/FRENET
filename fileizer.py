import cr2
import codecs
import webbrowser

strlink = input("what site")
page = cr2.getHTML(strlink)
page = cr2.getLinks(page, strlink,)
#page = cr2.getLinks(page, strlink, 'src="')
# to open/create a new html file in the write mode

f = open('GFG.html', 'w')

# writing the code into the file
f.write(page)

# close the file
f.close()

webbrowser.open('GFG.html')
