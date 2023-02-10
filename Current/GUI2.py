# Required libraries for program to run.

from tkinter.ttk import Style, Treeview
import Groupseparation
import basicradicals
import acidradicals
from SaltAnalysisProcedure import radicals
from Youtube import Youtubelink
from colourcon import getsettings
import userrecommendation

from tkinter import ttk
import tkinter as tk
import time
import http.client as httplib
import tkinter.font as font
import webbrowser
import os

def temp():
    PATH = os.path.dirname(__file__)
    # Required other python scripts.
    usersettings = getsettings(os.path.join(PATH,'colourconfig.txt'))

    Treeviewcolour = usersettings[0]
    Treeviewfont = usersettings[1]

    def fixed_map(option):
        # Fix for setting text colour for Tkinter 8.6.9
        # From: https://core.tcl.tk/tk/info/509cafafae
        #
        # Returns the style map for 'option' with any styles starting with
        # ('!disabled', '!selected', ...) filtered out.

        # style.map() returns an empty list for missing options, so this
        # should be future-safe.
        style = ttk.Style()
        return [elm for elm in style.map('Treeview', query_opt=option) if
        elm[:2] != ('!disabled', '!selected')]



    def checkInternetHttplib(url="www.google.com", timeout=3):
        """ This checks weather an internet connection is established
        with www.google.com"""

        conn = httplib.HTTPConnection(url, timeout=timeout)
        try:
            conn.request("HEAD", "/")
            conn.close()
            return True
        except:

            return False


    def send(table):
        '''This helps create the systematic salt analysis'''
        a = chosen_basic.get()
        b = chosen_acidic.get()

        Groupseparation.chart(a, Master)
        test = radicals(a, b)

        seperator = '_'*200
        # These are the names of functions defined in
        # SaltAnalysisProcedure.py
        table.insert('', 'end', values=('TEST FOR ACID RADICALS', '', '', ''))

        exec_methods_acidic_dry = ['Dry_Testtube_Heating',
                                'Dil_HCl',
                                'Special_Sulphide',
                                'Special_Nitrite',
                                'Conc_Sulphuric',
                                'Sulphate',
                                'Phosphate',
                                'Oxalate',
                                'Acetate',
                                'Special_Acetate']

        table.insert('', 'end', values=('DRY TESTS', '', '', ''))

        for method in exec_methods_acidic_dry:
            try:
                a = getattr(test, method)()
                b = list(a.values())
                m = list(a.keys())[0]
                table.insert('', 'end', values=(m, '', '', ''))

                for i in b:
                    if type(i[0]) == str:
                        i.insert(0, '')
                        table.insert('', 'end', values=(i), tags=str(method))

                    if type(i[0]) == list:
                        for j in i:
                            j.insert(0, '')
                            table.insert('', 'end', values=(j), tags=str(method))

                table.insert('', 'end', values=(
                    seperator, seperator, seperator, seperator))
            except:
                pass

        exec_methods_acidic_wet = ['Wet_Halides',
                                'Wet_Chloride',
                                'Wet_Nitrate',
                                'Wet_Sulphate',
                                ]
        # These are the names of functions defined in
        # SaltAnalysisProcedure.py
        table.insert('', 'end', values=('WET TESTS', '', '', ''))

        for method in exec_methods_acidic_wet:
            try:
                a = getattr(test, method)()
                b = list(a.values())
                m = list(a.keys())[0]
                table.insert('', 'end', values=(m, '', '', ''))

                for i in b:
                    if type(i[0]) == str:
                        i.insert(0, '')
                        table.insert('', 'end', values=(i), tags=str(method))

                    if type(i[0]) == list:
                        for j in i:
                            j.insert(0, '')
                            table.insert('', 'end', values=(j), tags=str(method))

                table.insert('', 'end', values=(
                    seperator, seperator, seperator, seperator))
            except:

                pass

        exec_methods_basic = ['Ammonium',
                            'Lead',
                            'Copper',
                            'Arsenic',
                            'Ferric',
                            'Aluminium',
                            'Zinc',
                            'Cobalt',
                            'Nickel',
                            'Manganese',
                            'Barium',
                            'Strontium',
                            'Calcium',
                            'Magnesium']

        table.insert('', 'end', values=('TEST FOR BASIC RADICALS', '', '', ''))

        for method in exec_methods_basic:
            try:
                a = getattr(test, method)()
                b = list(a.values())
                m = list(a.keys())[0]
                table.insert('', 'end', values=(m, '', '', '',))

                for i in b:
                    if type(i[0]) == str:
                        i.insert(0, '')
                        table.insert('', 'end', values=(i), tags=str(method))
                    if type(i[0]) == list:
                        for j in i:
                            j.insert(0, '')
                            table.insert('', 'end', values=(j), tags=str(method))
                table.insert('', 'end', values=(
                    seperator, seperator, seperator, seperator))
            except:
                pass


    def youtube():

        while True:
            if checkInternetHttplib():

                time.sleep(2)
                a = chosen_basic.get()
                b = chosen_acidic.get()
                links = Youtubelink(a, b)
                webbrowser.open_new(links[0])
                webbrowser.open_new(links[1])
                break
            else:

                break


    def create_window():
        global Treeviewcolour, Treeviewfont
        '''This creates the required treeview on button click'''
        windows = tk.Toplevel(Master)
        style = ttk.Style()
        style.map('Treeview', foreground=fixed_map('foreground'),
        background=fixed_map('background'))
        table = ttk.Treeview(windows, selectmode='browse')

        windows.geometry('1280x720')
        windows.title("Salt Analysis")

        table.pack(expand=True, fill='both')

        table['columns'] = ('subheading', 'experiment',
                            'observation', 'conclusion')
        table['show'] = 'headings'

        table.heading('subheading', text='subheading')
        table.heading('experiment', text='experiment')
        table.heading('observation', text='observation')
        table.heading('conclusion', text='conclusion')

        style = ttk.Style(windows)
        style.configure('Treeview', rowheight=40)
        style.configure('Treeview', fieldbackground=Treeviewcolour,
                        background=Treeviewcolour, font=Treeviewfont)
        send(table)


    def acid_radical():
        """ This passes the acid radical to function
        acidradical( ) which helps generate the procedure for the chosen
        radical """

        a = chosen_acidic.get()
        acidradicals.acidradical(a, Master)


    def basic_radical():
        """ This passes the basic radical to function
        basicradical( ) which helps generate the procedure for the chosen
        radical """

        b = chosen_basic.get()

        basicradicals.basicradical(b, Master)

    def reccomendation():
        userrecommendation.starter()

    Master = tk.Tk()
    Master.geometry('300x400')
    Master.title("Salt Analysis")

    l_title = tk.Message(Master,
                        text="Salt Analysis",
                        relief="flat",
                        width=2000,
                        padx=600, pady=0,
                        fg="black",
                        bg="#ffb367",
                        justify="center",
                        anchor="center")

    l_title.config(font=("Lucida Grande", "30", "bold"))
    l_title.pack(side="top")
    Master['bg'] = '#ffe277'

    # All the basic radicals that the program can accept .
    # These lists are required for listbox .

    BasicRadicals = [
        'Ammonium',
        'Ammonium',
        'Lead',
        'Copper',
        'Arsenic',
        'Ferric',
        'Aluminium',
        'Zinc',
        'Cobalt',
        'Nickel',
        'Manganese',
        'Barium',
        'Strontium',
        'Calcium',
        'Magnesium'
    ]
    # All the acid radicals that the program can accept .

    AcidRadicals = [
        'Carbonate',
        'Carbonate',
        'Nitrate',
        'Sulphite',
        'Nitrite',
        'Sulphide',
        'Iodide',
        'Bromide',
        'Chloride',
        'Sulphate',
        'Phosphate',
        'Oxalate',
        'Acetate'
    ]

    chosen_basic = tk.StringVar(Master)
    chosen_basic.set(BasicRadicals[0])

    chosen_acidic = tk.StringVar(Master)
    chosen_acidic.set(AcidRadicals[0])

    basic_menu = ttk.OptionMenu(
        Master, chosen_basic, *BasicRadicals).place(x=40, y=190)
    acid_menu = ttk.OptionMenu(Master, chosen_acidic,
                            *AcidRadicals). place(x=40, y=220)


    buttonfont = ('Roboto', 10, 'bold')
    SystematicAnalysis = tk.Button(
        Master,
        text='RESULT',
        height=5,
        width=20,
        bg='#ffb367',
        relief='flat',
        anchor='center',
        font=buttonfont,
        command=create_window
    )

    YoutubeOpener = tk.Button(
        Master,
        text='Check YouTube',
        height=2,
        width=20,
        bg='#36b5b0',
        relief='flat',
        font=buttonfont,
        command=youtube
    )

    Test_AcidRadicals = tk.Button(
        Master,
        text='Check',
        width=15,
        bg='#36b5b0',
        relief='flat',
        font=buttonfont,
        command=acid_radical
    )

    Test_BasicRadicals = tk.Button(
        Master,
        text='Check',
        width=15,
        bg='#ffb367',
        relief='flat',
        font=buttonfont,
        command=basic_radical
    )

    User_Reccomendation = tk.Button(
        Master,
        text='Feedback',
        width=15,
        bg='#ffb367',
        relief='flat',
        font=buttonfont,
        command=reccomendation
    )

    SystematicAnalysis.place(x=70, y=290)
    YoutubeOpener.place(x=70, y=110)
    Test_AcidRadicals.place(x=150, y=220)
    Test_BasicRadicals.place(x=150, y=190)
    User_Reccomendation.place(x=90,y=50)
    Master.mainloop()
