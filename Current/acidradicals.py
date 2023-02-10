import tkinter as tk
from tkinter import ttk
from SaltAnalysisProcedure import radicals


def acidradical(acidradical: str, root) -> None:
    """ This function helps create the table for
    the tests for all the various acid radicals .
    This function requires 2 arguments : \n
    `acid radical ` which is a `str` . Procedure to be found for this. \n
    `root` which is a `tk.Tk()` master root window.
    \n
    Result is a treeview table"""

    Master = root
    test = radicals('ammonium', acidradical)
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

    # Execution methods for various acid radicals.

    if acidradical.lower() == 'carbonate':
        exec_methods_acidic = ['Dry_Testtube_Heating', 'Dil_HCl']

    elif acidradical.lower() == 'sulphate':
        exec_methods_acidic = ['Sulphate', 'Wet_Sulphate']

    elif acidradical.lower() == 'nitrate':
        exec_methods_acidic = ['Dry_Testtube_Heating',
                               'Conc_Sulphuric', 'Wet_Nitrate']

    elif acidradical.lower() == 'sulphite':
        exec_methods_acidic = ['Dil_HCl']

    elif acidradical.lower() == 'nitrite':
        # Nitrite and nitrate have same wet tests
        exec_methods_acidic = ['Dil_HCl', 'Wet_Nitrate']

    elif acidradical.lower() == 'sulphide':
        exec_methods_acidic = ['Dil_HCl', 'Special_Sulphide']

    elif acidradical.lower() in ['iodide', 'bromide']:
        exec_methods_acidic = ['Conc_Sulphuric', 'Wet_Halides']

    elif acidradical.lower() == 'phosphate':
        exec_methods_acidic = ['Phosphate']

    elif acidradical.lower() == 'oxalate':
        exec_methods_acidic = ['Oxalate']

    elif acidradical.lower() == 'acetate':
        exec_methods_acidic = ['Dil_HCl', 'Acetate', 'Special_Acetate']

    elif acidradical.lower() == 'chloride':
        exec_methods_acidic = ['Conc_Sulphuric', 'Wet_Halides', 'Wet_Chloride']

    else:
        exec_methods_acidic = []

    table.insert('', 'end', values=(
        'Test for ' + acidradical + ' radical', '', ''))

    seperator = '_' * 200

    for method in exec_methods_acidic:

        resultsdict = getattr(test, method)()
        Results = list(resultsdict.values())
        Reagentheading = list(resultsdict.keys())[0]

        table.insert('', 'end', values=(seperator, seperator, seperator))
        table.insert('', 'end', values=(Reagentheading, '', ''))

        for Result in Results:

            if type(Result[0]) == str:

                Result.insert(0, '')
                table.insert('', 'end', values=(Result[1:]))

            if type(Result[0]) == list:

                for j in Result:

                    j.insert(0, '')
                    table.insert('', 'end', values=(j[1:]))
