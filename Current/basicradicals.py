import tkinter as tk
from tkinter import ttk
from SaltAnalysisProcedure import radicals


def basicradical(basicradical: str, root) -> None:
    """ This function helps create the table for
    the tests for all the various acid radicals .
    This function requires 2 arguments : \n
    `basic radical ` which is a `str` . Procedure to be found for this. \n
    `root` which is a `tk.Tk()` master root window.
    \n
    Result is a treeview table"""

    Master = root
    test = radicals(basicradical, 'carbonate')
    windows = tk.Toplevel(Master)
    style = ttk.Style(windows)

    style.configure('Treeview', rowheight=40)
    table = ttk.Treeview(windows, selectmode='browse')

    windows.geometry('1920x1080')

    table.pack(expand=True, fill='both')

    table['columns'] = ('experiment', 'observation', 'conclusion')
    table['show'] = 'headings'

    table.heading('experiment', text='experiment')
    table.heading('observation', text='observation')
    table.heading('conclusion', text='conclusion')

    exec_methods_basic = ['Ammonium', 'Lead', 'Copper',
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

    for radical in exec_methods_basic:
        if basicradical.lower() == radical.lower():
            exec_methods_basic = [radical]

    table.insert('', 'end', values=(
        'Test for '+basicradical + ' radical', '', ''))

    for method in exec_methods_basic:

        resultsdict = getattr(test, method)()
        Results = list(resultsdict.values())

        for Result in Results:

            if type(Result[0]) == str:

                Result.insert(0, '')
                table.insert('', 'end', values=(Result[1:]))

            if type(Result[0]) == list:

                for j in Result:
                    j.insert(0, '')
                    table.insert('', 'end', values=(j[1:]))
