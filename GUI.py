from Tkinter import *
app = Tk()
app.title("New Entry")
app.geometry('450x300+200+200')

sum_labstr = StringVar(None)
sum_labstr.set("Summary")
summary_lab = Label(app, textvariable=sum_labstr)
summary_lab.pack(side="left")

summary_str = StringVar(None)
summary = Entry(app, textvariable=summary_str)
summary.pack(side="left")

aut_labstr = StringVar(None)
aut_labstr.set("Author")
author_lab = Label(app, textvariable=aut_labstr)
author_lab.pack(side="left")

author_str = StringVar(None)
author = Entry(app, textvariable=author_str)
author.pack(side="left")

body_labstr = StringVar(None)
body_labstr.set("Body")

body_str = StringVar(None)
body = Entry(app, textvariable=body_str)
body.pack()

tags_str = StringVar(None)
tags = Entry(app, textvariable=tags_str)
tags.pack()

source_str = StringVar(None)
source = Entry(app, textvariable=source_str)

text = Text(app)
text.pack()

app.mainloop()
