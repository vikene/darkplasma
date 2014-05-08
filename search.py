from HTMLParser import HTMLParser
from Tkinter import *
import urllib2
import Tkinter
import tkMessageBox
import menu

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
def menu_routine():
    tkMessageBox.showinfo("Oops!","Yet to Code ")
def main_menu_bar(display_obj):
    menu_bar = Menu(display_obj)
    file_bar = Menu(menu_bar, tearoff=0)
    file_bar.add_command(label="Start Spidy!",command=menu_routine)
    file_bar.add_command(label="Open",command=menu_routine)
    file_bar.add_command(label="Open Recent",command=menu_routine)
    file_bar.add_separator()
    file_bar.add_command(label="Save",command=menu_routine)
    file_bar.add_command(label="Save As",command=menu_routine)
    file_bar.add_command(label="Save a copy",command=menu_routine)
    file_bar.add_separator()
    file_bar.add_command(label="Import",command=menu_routine)
    file_bar.add_command(label="Export",command=menu_routine)
    file_bar.add_separator()
    file_bar.add_command(label="Close",command=menu_routine)
    file_bar.add_command(label="Exit",command=menu_routine)
    menu_bar.add_cascade(label="File",menu=file_bar)
    edit_bar = Menu(menu_bar,tearoff=0)
    edit_bar.add_command(label="Undo     Ctrl+Z",command=menu_routine)
    edit_bar.add_command(label="Redo      Ctrl+Shift+z",command=menu_routine)
    edit_bar.add_separator()
    edit_bar.add_command(label="Cut",command=menu_routine)
    edit_bar.add_command(label="Copy",command=menu_routine)
    edit_bar.add_command(label="Paste",command=menu_routine)
    edit_bar.add_separator()
    edit_bar.add_command(label="Find",command=menu_routine)
    edit_bar.add_command(label="Replace",command=menu_routine)
 
    menu_bar.add_cascade(label="Edit",menu=edit_bar)
    view_bar= Menu(menu_bar,tearoff=0)
    view_bar.add_command(label="Raw Text",command=menu_routine)
    view_bar.add_command(label="Html",command=menu_routine)
    view_bar.add_command(label="Add Css",command=menu_routine)
    view_bar.add_command(label="Convert to Xml",command=menu_routine)
    view_bar.add_separator()
    view_bar.add_command(label="Font",command=menu_routine)
    view_bar.add_command(label="Font Size",command=menu_routine)
    view_bar.add_command(label="Font Color",command=menu_routine)
    view_bar.add_command(label="Sort Options",command=menu_routine)
    view_bar.add_separator()
    view_bar.add_command(label="Preferences",command=menu_routine)
    menu_bar.add_cascade(label="View",menu=view_bar)
    data_base = Menu(menu_bar,tearoff=0)
    data_base.add_command(label="Create Database",command=menu_routine)
    data_base.add_command(label="Create Table",command=menu_routine)
    data_base.add_command(label="Search Database",command=menu_routine)
    data_base.add_command(label="Delete Database",command=menu_routine)
    data_base.add_separator()
    data_base.add_command(label="Connect to Db",command=menu_routine)
    data_base.add_command(label="Disconnect from Db",command=menu_routine)
    data_base.add_separator()
    data_base.add_command(label="Connect to Indexer",command=menu_routine)
    data_base.add_command(label="Add Url's to Indexer",command=menu_routine)
    data_base.add_command(label="Connect to Remote Indexer",command=menu_routine)
    
    menu_bar.add_cascade(label="Database",menu=data_base)
    display_obj.config(menu=menu_bar)
    

face_1 = Tkinter.Tk()
main_menu_bar(face_1)


face_1.mainloop()


