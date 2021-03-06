from functions import Calculation
import tkinter

CalcNumber = []

Fenster = tkinter.Tk()

Fenster.title("Calculator")
Fenster.geometry("375x400")


InputLine = tkinter.Entry(
    text="Relative placement"
)
InputLine.place(relx=1, y=2, relwidth=1, relheight=0.09, anchor='ne')
InputLine.config(state='readonly')

Button1 = tkinter.Button(
    text="1",
    command=lambda: Calculation(1, InputLine, CalcNumber)
)
Button1.place(relx=0.2, rely=0.09, relwidth=0.2, relheight=0.18, anchor='nw')
Fenster.bind("1", lambda event: Calculation(1, InputLine, CalcNumber))

Button2 = tkinter.Button(
    text="2",
    command=lambda: Calculation(2, InputLine, CalcNumber)
)
Button2.place(relx=0.4, rely=0.09, relwidth=0.2, relheight=0.18, anchor='nw')
Fenster.bind("2", lambda event: Calculation(2, InputLine, CalcNumber))

Button3 = tkinter.Button(
    text="3",
    command=lambda: Calculation(3, InputLine, CalcNumber)
)
Button3.place(relx=0.6, rely=0.09, relwidth=0.2, relheight=0.18, anchor='nw')
Fenster.bind("3", lambda event: Calculation(3, InputLine, CalcNumber))

# ButtonKlammerAuf = tkinter.Button(
#    text="(",
#    command=lambda: Calculation("(", InputLine, CalcNumber)
# )
# ButtonKlammerAuf.place(relx=0.8, rely=0.09, relwidth=0.2,
#                       relheight=0.18, anchor='nw')
#Fenster.bind("(", lambda event: Calculation("(", InputLine, CalcNumber))

Button4 = tkinter.Button(
    text="4",
    command=lambda: Calculation(4, InputLine, CalcNumber)
)
Button4.place(relx=0.2, rely=0.27, relwidth=0.2,
              relheight=0.18, anchor='nw')
Fenster.bind("4", lambda event: Calculation(4, InputLine, CalcNumber))

Button5 = tkinter.Button(
    text="5",
    command=lambda: Calculation(5, InputLine, CalcNumber)
)
Button5.place(relx=0.4, rely=0.27, relwidth=0.2,
              relheight=0.18, anchor='nw')
Fenster.bind("5", lambda event: Calculation(5, InputLine, CalcNumber))

Button6 = tkinter.Button(
    text="6",
    command=lambda: Calculation(6, InputLine, CalcNumber)
)
Button6.place(relx=0.6, rely=0.27, relwidth=0.2,
              relheight=0.18, anchor='nw')
Fenster.bind("6", lambda event: Calculation(6, InputLine, CalcNumber))

# ButtonKlammerZu = tkinter.Button(
#    text=")",
#    command=lambda: Calculation(")", InputLine, CalcNumber)
# )
# ButtonKlammerZu.place(relx=0.8, rely=0.27, relwidth=0.2,
#                      relheight=0.18, anchor='nw')
#Fenster.bind(")", lambda event: Calculation(")", InputLine, CalcNumber))

Button7 = tkinter.Button(
    text="7",
    command=lambda: Calculation(7, InputLine, CalcNumber)
)
Button7.place(relx=0.2, rely=0.45, relwidth=0.2,
              relheight=0.18, anchor='nw')
Fenster.bind("7", lambda event: Calculation(7, InputLine, CalcNumber))

Button8 = tkinter.Button(
    text="8",
    command=lambda: Calculation(8, InputLine, CalcNumber)
)
Button8.place(relx=0.4, rely=0.45, relwidth=0.2, relheight=0.18, anchor='nw')
Fenster.bind("8", lambda event: Calculation(8, InputLine, CalcNumber))

Button9 = tkinter.Button(
    text="9",
    command=lambda: Calculation(9, InputLine, CalcNumber)
)
Button9.place(relx=0.6, rely=0.45, relwidth=0.2,
              relheight=0.18, anchor='nw')
Fenster.bind("9", lambda event: Calculation(9, InputLine, CalcNumber))

Button0 = tkinter.Button(
    text="0",
    command=lambda: Calculation(0, InputLine, CalcNumber)
)
Button0.place(relx=0.2, rely=0.63, relwidth=0.4,
              relheight=0.18, anchor='nw')
Fenster.bind("0", lambda event: Calculation(0, InputLine, CalcNumber))

ButtonComma = tkinter.Button(
    text=",",
    command=lambda: Calculation(",", InputLine, CalcNumber)
)
ButtonComma.place(relx=0.6, rely=0.63, relwidth=0.2,
                  relheight=0.18, anchor='nw')
Fenster.bind(",", lambda event: Calculation(",", InputLine, CalcNumber))

ButtonEqual = tkinter.Button(
    text="=",
    command=lambda: Calculation("=", InputLine, CalcNumber)
)
ButtonEqual.place(relx=0.6, rely=0.81, relwidth=0.4,
                  relheight=0.18, anchor='nw')
Fenster.bind("=", lambda event: Calculation("=", InputLine, CalcNumber))
Fenster.bind("<Return>", lambda event: Calculation("=", InputLine, CalcNumber))


ButtonPlus = tkinter.Button(
    text="+",
    command=lambda: Calculation("+", InputLine, CalcNumber)
)
ButtonPlus.place(relx=0, rely=0.09, relwidth=0.2,
                 relheight=0.18, anchor='nw')
Fenster.bind("+", lambda event: Calculation("+", InputLine, CalcNumber))

ButtonMinus = tkinter.Button(
    text="-",
    command=lambda: Calculation("-", InputLine, CalcNumber)
)
ButtonMinus.place(relx=0, rely=0.27, relwidth=0.2,
                  relheight=0.18, anchor='nw')
Fenster.bind("-", lambda event: Calculation("-", InputLine, CalcNumber))

ButtonMultiply = tkinter.Button(
    text="*",
    command=lambda: Calculation("*", InputLine, CalcNumber)
)
ButtonMultiply.place(relx=0, rely=0.45, relwidth=0.2,
                     relheight=0.18, anchor='nw')
Fenster.bind("*", lambda event: Calculation("*", InputLine, CalcNumber))

ButtonDivide = tkinter.Button(
    text="/",
    command=lambda: Calculation("/", InputLine, CalcNumber)
)
ButtonDivide.place(relx=0, rely=0.63, relwidth=0.2,
                   relheight=0.18, anchor='nw')
Fenster.bind("/", lambda event: Calculation("/", InputLine, CalcNumber))

ButtonClear = tkinter.Button(
    text="C",
    command=lambda: Calculation("C", InputLine, CalcNumber)
)
ButtonClear.place(relx=0, rely=0.81, relwidth=0.4,
                  relheight=0.18, anchor='nw')
Fenster.bind("c", lambda event: Calculation("C", InputLine, CalcNumber))

ButtonStepBack = tkinter.Button(
    text="<-",
    command=lambda: Calculation("<-", InputLine, CalcNumber)
)
ButtonStepBack.place(relx=0.4, rely=0.81, relwidth=0.2,
                     relheight=0.18, anchor='nw')
Fenster.bind("<BackSpace>", lambda event: Calculation(
    "<-", InputLine, CalcNumber))


Fenster.mainloop()
