#libraries
from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

#setting the application window size and colour
root = Tk()
root.geometry('1000x320')
root.resizable(0,0)
root['bg']= 'grey90'

# Title for the Application window
root.title("Language translator Exposys Data Labs")
# Label for the heading
Label(root, text="Language Translator", font="Arial 20 bold", bg='skyblue').pack()          
# Label for the input text box
Label(root, text="Enter Text", font='arial 13 bold', bg='skyblue').place(x=165, y=90)       

# creating the input text box
Input_text=Entry(root, width= 60) 
Input_text.place(x=30, y = 130) 
Input_text.get()
# Label for the output text box
Label(root, text = "Output", font='arial 13 bold', bg='skyblue').place(x= 750, y= 90)       

# creating the output text box
output_text = Text(root, font='arial 10', height=5, wrap=WORD, padx= 5, pady= 5, width= 50)
output_text.place(x= 600, y = 130)

# list of languages to select for the translation from API
language = list(LANGUAGES.values())

# creating the combobox for the destination language to choose from
dest_lang= ttk.Combobox(root, values= language, width= 22) 
dest_lang.place(x=130, y=160)
dest_lang.set('choose language')

# defining the tranlate function
def Translate():
    translator = Translator()
    translated= translator.translate(text=Input_text.get(), dest= dest_lang.get())
    output_text.delete(1.0, END)
    output_text.insert(END, translated.text)

#creating the translate button
trans_btn= Button(root, text='Translate', font= 'arial 12 bold', pady = 5, command= Translate, bg= 'orange', activebackground='green')
trans_btn.place(x= 445, y=230)

root.mainloop()
