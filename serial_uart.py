from tkinter import *

import serial

uart = serial.Serial('/dev/ttyUSB0', 115200, 8, 'N', 1)

root=Tk()
root.title("UART_controller") 

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

frame = Frame(root)
frame.grid(row=0, column=0)

frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

def move(event):
    
    evnt_obj = str(event.widget)[-1]

    if evnt_obj == '2':
        uart.write('DOWN'.encode())
    elif evnt_obj == 'n' :
        uart.write('UP'.encode())  
    elif evnt_obj == '3' :
        uart.write('LEFT'.encode())       
    elif evnt_obj == '4' :
        uart.write('RIGHT'.encode())   
    
btm1 = Button(frame,
              padx=30,
              pady=30,
              font=('Arial', 24, 'bold'),
              text='🡅'
)
btm1.grid(column=1, row=0, padx=10, pady=10, sticky=(N))

btm1.bind('<Button-1>', move)

btm2 = Button(frame,
              padx=30,
              pady=30,
              font=('Arial', 24, 'bold'),
              text='🡇'
              
)
btm2.grid(column=1, row=2, padx=10, pady=10)
btm2.bind('<Button-1>', move)

btm3 = Button(frame,
              padx=30,
              pady=30,
              font=('Arial', 24, 'bold'),
              text='🡄'
)
btm3.grid(column=0, row=1, padx=10, pady=10, sticky=(N))
btm3.bind('<Button-1>', move)

btm4 = Button(frame,
              padx=30,
              pady=30,
              font=('Arial', 24, 'bold'),
              text='🡆'
)
btm4.grid(column=2, row=1, padx=10, pady=10)
btm4.bind('<Button-1>', move)



root.mainloop()
