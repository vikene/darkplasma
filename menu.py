import Tkinter
def screen_menu(display_obj):
    menu_bar = Menu(display_obj)
    file_bar = Menu(menu_bar, tearoff=0)
    file_bar.add_command(label="Start Spidy!",command=menu_routine)
    menu_bar.add_cascade(label="File",menu=file_bar)
    display_obj.config(menu=menu_bar)
    return
