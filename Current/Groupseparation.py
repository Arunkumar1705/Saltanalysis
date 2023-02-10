import tkinter as tk


def chart(basicradical:str, root:tk.Tk):

    """ This is a function to draw the group separation chart.
    Inputs. \n
    basicradical --> Name of basic radical
    root --> tkinter master """
    
    Master = root
    chart = tk.Toplevel(Master,bg='#ffe277')
    width, height = root.winfo_screenwidth(), root.winfo_screenheight()
    chart.geometry(f'{width}x{height}')
   
    test1 = 'To the Salt Solution dil.Hcl is added and is heated'
    test2 = 'H2S gas passed in Acidic Medium'
    test3 = 'H2S is boiled off and NH4Cl and NH4OH  is added to medium alkaline  . Check alkalinity with litmus paper'
    test4 = 'H2S is passed in Alkaline Medium'
    test5 = 'H2S is boiled off and  Ammonium Carbonate is added'
    test6 = 'To the filterate of group V  Sodium hydrogen phosphate is added'

    result1 = 'No \n Precipitate'
    result2 = 'No \n Precipitate'
    result3 = 'No \n Precipitate'
    result4 = 'No \n Precipitate'
    result5 = 'No \n Precipitate'
    result6 = 'No \n Precipitate'

    if basicradical.lower() == 'lead':
        result1 = 'White \n Precipitate \n of PbCl2'
        
    elif basicradical.lower() == 'copper':
        result2 = 'Black \n Precipitate \n of \n CuS'
        
    elif basicradical.lower() == 'arsenic':
        result2 = 'Yellow \n Precipitate \n of \n As2S3'
        
    elif basicradical.lower() == 'aluminium':
        result3 = 'Gelatenous \n White \n Precipitate \n of \n Al(OH)3'
        
    elif basicradical.lower() == 'iron':
        result3 = 'Brown \n Precipitate \n of \n Fe(OH)3'
        
    elif basicradical.lower() == 'manganese':
        result4 = 'Flesh \n Precipitate \n of \n MnS'
       
    elif basicradical.lower() in ['cobalt', 'nickel']:
        result4 = 'Black \n Precipitate \n of \n' + basicradical.lower()
        
    elif basicradical.lower() == 'zinc':
        result4 = 'White \n Precipitate \n of \n NiS'
        
    elif basicradical.lower() in ['barium', 'strontium', 'calcium']:
        result5 = 'White \n Precipitate \n of \n '+basicradical.lower()
        
    elif basicradical.lower() == 'magnesium':
        result6 = 'White \n Precipitate \n of \n MgHPO4'
        
    else:
        pass
    
    BUTTON_HEIGHT = height//10
    SPACE_FACTOR = 10
    pixel = tk.PhotoImage(width=1, height=1)
    
    a = tk.Button(
        chart ,
        text=test1 ,
        image=pixel ,
        height = BUTTON_HEIGHT , 
        width=width ,
        bg='#ffb367', 
        relief='flat',
        anchor='w',
        compound='c'
        )
    b = tk.Button(
        chart, 
        text=test2,
        image=pixel, 
        height =BUTTON_HEIGHT, 
        width=width,
        bg='#ffb367', 
        relief='flat',
        anchor='w',
        compound='c'
        )
    c = tk.Button(
        chart, 
        text=test3,
        image=pixel, 
        height = BUTTON_HEIGHT, 
        width=width,
        bg='#ffb367', 
        relief='flat',
        anchor='w',
        compound='c'
        )
    d = tk.Button(
        chart, 
        text=test4,
        image=pixel, 
        height =BUTTON_HEIGHT, 
        width=width,
        bg='#ffb367', 
        relief='flat',
        anchor='w',
        compound='c'
        )
    e = tk.Button(
        chart,
        text=test5,
        image=pixel, 
        height = BUTTON_HEIGHT, 
        width=width,
        bg='#ffb367', 
        relief='flat',
        anchor='w',
        compound='c'
        )
    f = tk.Button(
        chart, 
        text=test6, 
        image=pixel,
        height = BUTTON_HEIGHT, 
        width=width,
        bg='#ffb367', 
        relief='flat',
        anchor='w',
        compound='c'
        )
    nb = tk.Button(
        chart,
        height = height//2.5, 
        image=pixel,
        width=width,
        bg='#36b5b0', 
        relief='flat' ,
        justify="center",
        anchor='w',
        compound='c'
        )
                     
    g = tk.Button(
        chart, 
        text=result1,
        image=pixel, 
        height=8*(BUTTON_HEIGHT),
        width = width//13, 
        bg= '#ffe277', 
        relief='flat',
        anchor='c',
        compound='c'
        )
    h = tk.Button(
        chart, 
        text=result2, 
        image=pixel,
        height=7*(BUTTON_HEIGHT),
        width = width//13, 
        bg= '#ffe277', 
        relief='flat',
        anchor='c',
        compound='c'
        )
    i = tk.Button(
        chart, 
        text=result3,
        image=pixel ,
        height=6*(BUTTON_HEIGHT),
        width = width//13, 
        bg='#ffe277', 
        relief='flat',
        anchor='c',
        compound='c'
        )
    j = tk.Button(
        chart, 
        text=result4,
        image=pixel,
        height=5*(BUTTON_HEIGHT),
        width = width//13, 
        bg='#ffe277', 
        relief='flat',
        anchor='c',
        compound='c'
        )
    k = tk.Button(
        chart, 
        text=result5,
        image=pixel,
        height=4*(BUTTON_HEIGHT),
        width = width//13, 
        bg='#ffe277', 
        relief='flat',
        anchor='c',
        compound='c'
        )
    l = tk.Button(
        chart,
        text=result6,
        image=pixel,
        height=3*(BUTTON_HEIGHT),
        width = width//13, 
        bg='#ffe277', 
        relief='flat',
        anchor='c',
        compound='c'
        )


    a.place(y=0, x=0)
    b.place(y=(BUTTON_HEIGHT), x=(width//13)+SPACE_FACTOR)
    c.place(y=(BUTTON_HEIGHT)*2, x=((width//13)*2)+(2*SPACE_FACTOR))
    d.place(y=(BUTTON_HEIGHT)*3, x=((width//13)*3)+(3*SPACE_FACTOR))
    e.place(y=(BUTTON_HEIGHT)*4, x=((width//13)*4)+(4*SPACE_FACTOR))
    f.place(y=(BUTTON_HEIGHT)*5, x=((width//13)*5)+(5*SPACE_FACTOR))
    nb.place(y=((BUTTON_HEIGHT)*6)+SPACE_FACTOR,x=((width//13)*6)+(6*SPACE_FACTOR))
    

    g.place(x=0, y=(BUTTON_HEIGHT)+SPACE_FACTOR)
    h.place(y=((BUTTON_HEIGHT)*2)+SPACE_FACTOR, x=((width//13)*1)+10)
    i.place(y=((BUTTON_HEIGHT)*3)+SPACE_FACTOR, x=((width//13)*2)+(2*SPACE_FACTOR))
    j.place(y=((BUTTON_HEIGHT)*4)+SPACE_FACTOR, x=((width//13)*3)+(3*SPACE_FACTOR))
    k.place(y=((BUTTON_HEIGHT)*5)+SPACE_FACTOR, x=((width//13)*4)+(4*SPACE_FACTOR))
    l.place(y=((BUTTON_HEIGHT)*6)+SPACE_FACTOR, x=((width//13)*5)+(5*SPACE_FACTOR))
