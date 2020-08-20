from tkinter import*
root=Tk()
root.title("Tanjib's Super Store_Version.1.2")
root.geometry('650x500')

#Company Title area
name=Frame(root, bd=5, relief=GROOVE)
name.place(x=0,y=0, width=600, height=60)
name_tile=Label(name,bg='black',fg='white', text="Tanjib's Super Store", font=('times new roman',30,'bold')).pack(fill=X)

#Products details area
f_product=Frame(root, bd=4, relief=GROOVE)
f_product.place(x=0, y=60, width=400, height=300)

bil_title=Label(f_product, text='Products', font=('times new roman',15,'bold'),width=35)
bil_title.grid(row=0, column=0, columnspan=7)
#products name
product_1=Label(f_product, text='Rice',font=('times new roman',9, 'bold'))
product_2=Label(f_product, text='Oil',font=('times new roman',9, 'bold'))
product_3=Label(f_product, text='Potato', font=('times new roman',9, 'bold'))
product_4=Label(f_product, text='Meat', font=('times new roman',9, 'bold'))
product_5=Label(f_product, text='Ilish', font=('times new roman',9, 'bold'))
product_6=Label(f_product, text='Egg', font=('times new roman',9, 'bold'))
product_7=Label(f_product, text='Apple', font=('times new roman',9, 'bold'))
product_8=Label(f_product, text='Banana', font=('times new roman',9, 'bold'))
product_9=Label(f_product, text='Mango', font=('times new roman',9, 'bold'))
product_10=Label(f_product, text='Lichi', font=('times new roman',9, 'bold'))
product_11=Label(f_product, text='Lemon', font=('times new roman',9, 'bold'))
product_12=Label(f_product, text='Coconut', font=('times new roman',9, 'bold'))
product_13=Label(f_product, text='Pen', font=('times new roman',9, 'bold'))
product_14=Label(f_product, text='Pencil', font=('times new roman',9, 'bold'))
product_15=Label(f_product, text='Eraser', font=('times new roman',9, 'bold'))
product_16=Label(f_product, text='Marker', font=('times new roman',9, 'bold'))
product_17=Label(f_product, text='Scale', font=('times new roman',9, 'bold'))
product_18=Label(f_product, text='Compas', font=('times new roman',9, 'bold'))



#==============================
product_1.grid(row=1, column=0)
product_2.grid(row=2, column=0)
product_3.grid(row=3, column=0)
product_4.grid(row=4, column=0)
product_5.grid(row=5, column=0)
product_6.grid(row=6, column=0)
product_7.grid(row=7, column=0)
product_8.grid(row=8, column=0)
product_9.grid(row=9, column=0)
product_10.grid(row=1, column=2)
product_11.grid(row=2, column=2)
product_12.grid(row=3, column=2)
product_13.grid(row=4, column=2)
product_14.grid(row=5, column=2)
product_15.grid(row=6, column=2)
product_16.grid(row=7, column=2)
product_17.grid(row=8, column=2)
product_18.grid(row=9, column=2)

#Products Quantity
entry_1=Entry(f_product)
entry_2=Entry(f_product)
entry_3=Entry(f_product)
entry_4=Entry(f_product)
entry_5=Entry(f_product)
entry_6=Entry(f_product)
entry_7=Entry(f_product)
entry_8=Entry(f_product)
entry_9=Entry(f_product)
entry_10=Entry(f_product)
entry_11=Entry(f_product)
entry_12=Entry(f_product)
entry_13=Entry(f_product)
entry_14=Entry(f_product)
entry_15=Entry(f_product)
entry_16=Entry(f_product)
entry_17=Entry(f_product)
entry_18=Entry(f_product)


entry_1.grid(row=1, column=1)
entry_2.grid(row=2, column=1)
entry_3.grid(row=3, column=1)
entry_4.grid(row=4, column=1)
entry_5.grid(row=5, column=1)
entry_6.grid(row=6, column=1)
entry_7.grid(row=7, column=1)
entry_8.grid(row=8, column=1)
entry_9.grid(row=9, column=1)
entry_10.grid(row=1, column=3)
entry_11.grid(row=2, column=3)
entry_12.grid(row=3, column=3)
entry_13.grid(row=4, column=3)
entry_14.grid(row=5, column=3)
entry_15.grid(row=6, column=3)
entry_16.grid(row=7, column=3)
entry_17.grid(row=8, column=3)
entry_18.grid(row=9, column=3)
#**********************************************************

#Clear Button in the product frame
def clean():
    entry_1.delete(0, END)
    entry_2.delete(0, END)
    entry_3.delete(0, END)
    entry_4.delete(0, END)
    entry_5.delete(0, END)
    entry_6.delete(0, END)
    entry_7.delete(0, END)
    entry_8.delete(0, END)
    entry_9.delete(0, END)
    entry_10.delete(0, END)
    entry_11.delete(0, END)
    entry_12.delete(0, END)
    entry_13.delete(0, END)
    entry_14.delete(0, END)
    entry_15.delete(0, END)
    entry_16.delete(0, END)
    entry_17.delete(0, END)
    entry_18.delete(0, END)
    e_vat.delete(0, END)
    e_reduced.delete(0, END)
    e_biller.delete(0, END)
    text_box.delete('1.0', END)

clear_button=Button(f_product, text='Clear',borderwidth=3, padx=176, pady=22, bg='#3ee4db', font=('times new roman',15, 'bold'), command=clean)
clear_button.grid(row=10, column=0, columnspan=4)
#******************************************************************************************************************************************

#bill area
f_bil=Frame(root, bd=4, relief=GROOVE)
f_bil.place(x=400, y=60, width=200, height=300)
text_box=Text(f_bil, width=25, height=21)
text_box.config(state='disabled')
out=Label(f_bil, text='Bill Area', font=('times new roman', 15)).pack()

#Bill generate button area
def enter():
    #text_box.delete(0, END)                            #(Looking for the command to delete the text screen first)
    text_box.config(state='normal')
    text_box.insert(INSERT,'==========Bill=========')
    #Product price
    if entry_1.get()=='':
        rice=0
    else:
        rice=50*float(entry_1.get())
        text_box.insert(INSERT,'\nRice=50x'+entry_1.get()+'kg='+str(rice)+'tk')
    if entry_2.get()=='':
        oil=0
    else:
        oil=100*float(entry_2.get())
        text_box.insert(INSERT,'\nOil=100x'+entry_2.get()+'Litre='+str(oil)+'tk')

    if entry_3.get()=='':
        potato=0
    else:
        potato=30*float(entry_3.get())
        text_box.insert(INSERT,'\nPotato=30x'+entry_3.get()+'kg='+str(potato)+'tk')
    if entry_4.get()=='':
        meat=0
    else:
        meat=570*float(entry_4.get())
        text_box.insert(INSERT,'\nMeat=570x'+entry_4.get()+'kg='+str(meat)+'tk')

    if entry_5.get()=='':
        ilish=0
    else:
        ilish=1100*float(entry_5.get())
        text_box.insert(INSERT,'\nIlish=1100x'+entry_5.get()+'kg='+str(ilish)+'tk')

    if entry_6.get()=='':
        egg=0
    else:
        egg=9*float(entry_6.get())
        text_box.insert(INSERT,'\nEgg=9x'+entry_6.get()+'piece='+str(egg)+'tk')
    
    if entry_7.get()=='':
        apple=0
    else:
        apple=160*float(entry_7.get())
        text_box.insert(INSERT,'\nApple=160x'+entry_7.get()+'kg='+str(apple)+'tk')

    if entry_8.get()=='':
        banana=0
    else:
        banana=7*float(entry_8.get())
        text_box.insert(INSERT,'\nBanana=7x'+entry_8.get()+'piece='+str(banana)+'tk')

    if entry_9.get()=='':
        mango=0
    else:
        mango=110*float(entry_9.get())
        text_box.insert(INSERT,'\nMango=110x'+entry_9.get()+'kg='+str(mango)+'tk')

    if entry_10.get()=='':
        lichi=0
    else:
        lichi=6*float(entry_10.get())
        text_box.insert(INSERT,'\nLichi=6x'+entry_10.get()+'piece='+str(lichi)+'tk')

    if entry_11.get()=='':
        lemon=0
    else:
        lemon=6*float(entry_11.get())
        text_box.insert(INSERT,'\nLemon=6x'+entry_11.get()+'piece='+str(lemon)+'tk')

    if entry_12.get()=='':
        coconut=0
    else:
        coconut=45*float(entry_12.get())
        text_box.insert(INSERT,'\nCoconut=45x'+entry_12.get()+'piece='+str(coconut)+'tk')

    if entry_13.get()=='':
        pen=0
    else:
        pen=5*float(entry_13.get())
        text_box.insert(INSERT,'\nPen=5x'+entry_13.get()+'piece='+str(pen)+'tk')

    if entry_14.get()=='':
        pencil=0
    else:
        pencil=10*float(entry_14.get())
        text_box.insert(INSERT,'\nPencil=10x'+entry_14.get()+'piece='+str(pencil)+'tk')

    if entry_15.get()=='':
        eraser=0
    else:
        eraser=10*float(entry_15.get())
        text_box.insert(INSERT,'\nEraser=10x'+entry_15.get()+'piece='+str(eraser)+'tk')

    if entry_16.get()=='':
        marker=0
    else:
        marker=45*float(entry_16.get())
        text_box.insert(INSERT,'\nMarker=45x'+entry_16.get()+'piece='+str(marker)+'tk')

    if entry_17.get()=='':
        scale=0
    else:
        scale=30*float(entry_17.get())
        text_box.insert(INSERT,'\nScale=30x'+entry_17.get()+'pice='+str(scale)+'tk')

    if entry_18.get()=='':
        compas=0
    else:
        compas=60*float(entry_18.get())
        text_box.insert(INSERT,'\nCompas=60x'+entry_18.get()+'piece='+str(compas)+'tk')
  


    #*******************************
    billi=rice+oil+potato+meat+ilish+egg+apple+banana+mango+lichi+lemon+coconut+pen+pencil+eraser+marker+scale+compas
    total_bill=str(billi) 
    
    vatti=billi*.15
    total_vat=str(vatti)

    reduction=billi*.02
    e_reduced.insert(INSERT, str(reduction)+' Tk')

    final_bill=billi+vatti-reduction
    #text_box.config(state='normal')
    text_box.insert(INSERT, '\n\nTotal bill = '+total_bill+' TK')
    text_box.insert(INSERT, '\n15% Vat= '+total_vat+' Tk')
    e_vat.insert(INSERT, total_vat+' Tk')
    text_box.insert(INSERT, '\nReduced Tk = '+str(reduction)+' Tk')
    text_box.insert(INSERT, '\n\nFinal bill= '+str(final_bill)+' Tk')
    text_box.insert(INSERT,'\n\nPrepared by- '+str(e_biller.get()))
    #text_box.config(state='disabled')
    #e_vat.config(state='disabled')
    #e_reduced.config(state='disabled')
text_box.pack()

#Bottom area (tax, reduced price, bill generate button, saler name)
botom=Frame(root, bd=4, relief=GROOVE)
botom.place(x=0, y=360, width=600, height=60)

l_vat=Label(botom, text='Vat →', bg='#5be4d0', width=20)
e_vat=Entry(botom, width=15, bg='#5be4d0')
l_reduced=Label(botom, text='Reduced Price →',bg='#57d1e6',width=20)
e_reduced=Entry(botom, width=15,bg='#57d1e6')
l_generate=Button(botom, text="Generate Bill",bg='#57d1e6', borderwidth=2, padx=47, pady=15, command=enter)
l_biller=Label(botom, text='Biller Name ↓↓↓', bg='#ea64e5', width=25)
e_biller=Entry(botom, width=30, bg='#ea64e5')

l_vat.grid(row=0, column=0)
e_vat.grid(row=0, column=1)
l_reduced.grid(row=1, column=0)
e_reduced.grid(row=1, column=1)
l_generate.grid(row=0, column=3, rowspan=2)
l_biller.grid(row=0, column=2)
e_biller.grid(row=1, column=2)


root.mainloop()