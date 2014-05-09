from HTMLParser import HTMLParser
from Tkinter import *
import urllib2
import Tkinter
import tkMessageBox
import menu
import thread
from multiprocessing.pool import ThreadPool

tag_made = 0

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
       if( tag == 'script'):
           tag_made = 1
       if( tag == 'style'):
           tag_made = 1
       
    def handle_endtag(self, tag):
        if(tag== 'script'):
            tag_made=0    
        if( tag == 'style'):
           tag_made = 0
    
    def handle_data(self, data):
        xx = data
        if(tag_made == 0):
            if(xx.find("CDATA") == -1):
                if(xx.find('/*') == -1):
                    if(xx.find('!') == -1):
                        if(xx.find('\n') == -1):
                            view_me.insert(INSERT,data+'\n')

filee=  open('Data_parsed.txt','w')
parser = MyHTMLParser()
custom = "http://jeovasanctusunus.tumblr.com/"

class dialogue:
    def __init__(self, parent):

        ask_dig = self.ask_dig = Toplevel(parent)
        self.ask_dig.title("Custom URL")
        url_As = Label(ask_dig,text="Enter a URL to Scan")
        url_As.pack(padx=15)
        self.url = Entry(ask_dig,width=80)
        self.url.pack()
        self.url.focus_set()
        b = Button(ask_dig,text="Ok",command=self.ok)
        b.pack()

    def ok(self):
        custom = self.url.get()
        print self.url.get()
        self.ask_dig.destroy()


def startmee():
    d = dialogue(face_1)
    face_1.wait_window(d.ask_dig)
    start_pool =  ThreadPool(processes=1)
    as_result = start_pool.apply_async(urllib2.urlopen,(custom,))
    result = as_result.get()

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
    file_bar.add_command(label="Start Spidy!",command=startmee)
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
    window_bar = Menu(menu_bar,tearoff=0)
    window_bar.add_command(label="Zoom in       +",command=menu_routine)
    window_bar.add_command(label="Zoom out      -",command=menu_routine)
    window_bar.add_separator()
    window_bar.add_command(label="Tk",command=menu_routine)
    menu_bar.add_cascade(label="Windows",menu=window_bar)
    help_bar = Menu(menu_bar,tearoff=0)
    help_bar.add_command(label="About Spider",command=menu_routine)
    help_bar.add_separator()
    help_bar.add_command(label="Docs",command=menu_routine)
    help_bar.add_command(label="Help (online)",command=menu_routine)
    menu_bar.add_cascade(label="Help",menu=help_bar)
    
    display_obj.config(menu=menu_bar)
    

face_1 = Tkinter.Tk()
main_menu_bar(face_1)
view_me = Text(face_1)
view_me.pack()
face_1.title("Dark Plasma")
face_1.mainloop()





