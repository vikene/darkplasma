from HTMLParser import HTMLParser
import urllib2
import Tkinter
import tkMessageBox

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Encountered a start tag:", tag
    def handle_endtag(self, tag):
        print "Encountered an end tag :", tag
    
    def handle_data(self, data):
       filee.write(data+'\n')

filee=  open('Data_parsed.txt','w')
parser = MyHTMLParser()

def startmee():
    result = urllib2.urlopen('http://www.bing.com/search?q=java')
    java = result.read()
  
    parser.feed(java)
    filee.close()

def Start_routine():
    tkMessageBox.showinfo("Java Spider!","Spider Program initilizing babe")
    startmee()

top = Tkinter.Tk()
C = Tkinter.Canvas(top, bg="blue", height=250, width=300)


coord = 10, 50, 240, 210
arc = C.create_arc(coord, start=0, extent=150, fill="red")
button = Tkinter.Button(top , text = "Start Spidy" , command = Start_routine)
button.pack()
C.pack()
top.mainloop()


