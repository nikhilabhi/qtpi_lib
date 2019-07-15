from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants
from pymata_aio.pymata_core import PymataCore
from pymata_aio.private_constants import PrivateConstants
import asyncio
from time import sleep
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import ttk

import serial.tools.list_ports
global pin
val = 0

def bluetooth_connect():
    while 1:
        port = input("Enter COM port number:")
        if port != "":
            break
    board = PymataCore(com_port='COM'+port)
    board.start()
   


class connect():
    global cp, ComPort, board

    def enter():
        global cp, ComPort, board
        cp = cb.get()
        print(cp)
        comport = cp[:6]
        print(comport)
        #print("Enter ComPort No:")
        # cp=input()
        #cp = InOutResult.get()
        cp = comport
        while 1:
            if cp == "":
                print("Enter ComPort No:")
                cp = input()
                ui.notifier("Not connected")
            else:
                ComPort =cp
                break

        #Creating Board Instance
        #board = PyMata3(com_port=ComPort)
        board = PymataCore(com_port=ComPort)
        board.start()
        root.destroy()
        ui.notifier("connected")
        #root.wait_window(new)

def dig_port2pin(port):
    if len(board.digital_pins) == 70:
        #print("veda digital")
        if port == 1:
            pin = 3
        elif port == 2:
            pin = 9
        elif port == 3:
            pin = 10
        elif port == 4:
            pin = 11
        elif port == 5:
            pin = 52
        elif port == 6:
            pin = 8
        return pin
    elif len(board.digital_pins) == 22:
        print("rio")
        if port == 1:
            pin = 3
        elif port == 2:
            pin = 9
        elif port == 3:
            pin = 10
        elif port == 4:
            pin = 11
        elif port == 5:
            pin = 2
        elif port == 6:
            pin = 8
        return pin
def ana_port2pin(port):
    if port == 1:
        pin = 0
    elif port == 2:
        pin = 1
    elif port == 3:
        pin = 2
    elif port == 4:
        pin = 6
    return pin

async def ver():
    await board.get_firmware_version()
  
async def send_argb(port,index, pixel, r, g, b):
    pin = dig_port2pin(port)
    await board._send_sysex(0x12, [0x01, pin, pixel])
    await (board._send_sysex(0x13,[pin,index, r,g, b]))

async def send_us(pin):
    await board._send_sysex(0x10, [pin])

async def send_temp(pin):
    await board._send_sysex(0x09, [pin])

async def dc_motor(port, speed, dire):
    if port == 1:
        await board.set_pin_mode(4, Constants.OUTPUT)
        await board.set_pin_mode(5, Constants.PWM)
        if (dire == True):
            await board.digital_write(4, 1)
            await board.analog_write(5, speed)
        elif dire == False:
            await board.digital_write(4, 0)
            await board.analog_write(5, speed)
    elif port == 2:
        await board.set_pin_mode(7, Constants.OUTPUT)
        await board.set_pin_mode(6, Constants.PWM)
        if dire == True:
            await board.digital_write(7, 1)
            await board.analog_write(6, speed)
        if dire == False:
            await board.digital_write(7, 0)
            await board.analog_write(6, speed)

async def dig_led(port, state):
    if state == True:
        pin = dig_port2pin(port)
        await board.set_pin_mode(pin, Constants.OUTPUT)
        await board.digital_write(pin,1)
    elif state == False:
        pin = dig_port2pin(port)
        await board.set_pin_mode(pin, Constants.OUTPUT)
        await board.digital_write(pin,0)

async def servo(port, angle):
    if port == 1:
        pin = 3
    elif port == 2:
        pin = 9
    elif port == 3:
        pin = 10
    elif port == 4:
        pin = 11
    elif port == 5:
        pin = 2
    elif port == 6:
        pin = 8
    await board.servo_config(pin)
    await board.analog_write(pin,angle)
    

async def async_rgb(port,colour,value):
    colour = colour.casefold()
    if value == 255:
        value = 1
    if port == 3:
        if len(board.digital_pins) == 70:
            if colour == 'r':
                pin = 56
            elif colour == 'b':
                pin = 10
            elif colour == 'g':
                pin = 59
            await board.set_pin_mode(pin, Constants.OUTPUT)
            await board.digital_write(pin, value)
        if len(board.digital_pins) == 22:
            if colour == 'r':
                pin = 16
            elif colour == 'b':
                pin = 10
            elif colour == 'g':
                pin = 19
            await board.set_pin_mode(pin, Constants.OUTPUT)
            await board.digital_write(pin, value)
    if port == 2:
        if len(board.digital_pins) == 70:
            if colour == 'r':
                pin = 55
            elif colour == 'b':
                pin = 9
            elif colour == 'g':
                pin = 21
            await board.set_pin_mode(pin, Constants.OUTPUT)
            await board.digital_write(pin, value)
        if len(board.digital_pins) == 22:
            if colour == 'r':
                pin = 15
            elif colour == 'b':
                pin = 9
            elif colour == 'g':
                pin = 19
            await board.set_pin_mode(pin, Constants.OUTPUT)
            await board.digital_write(pin, value)
    if port == 1:
        if len(board.digital_pins) == 70:
            if colour == 'r':
                pin = 54
            elif colour == 'b':
                pin = 3
            elif colour == 'g':
                pin = 26
            await board.set_pin_mode(pin, Constants.OUTPUT)
            await board.digital_write(pin, value)
        if len(board.digital_pins) == 22:
            if colour == 'r':
                pin = 14
            elif colour == 'b':
                pin = 3
            elif colour == 'g':
                pin = 26
            await board.set_pin_mode(pin, Constants.OUTPUT)
            await board.digital_write(pin, value)
    if port == 4:
        if len(board.digital_pins) == 70:
            if colour == 'r':
                pin = 60
            elif colour == 'b':
                pin = 11
            elif colour == 'g':
                pin = 19
            await board.set_pin_mode(pin, Constants.OUTPUT)
            await board.digital_write(pin, value)
        if len(board.digital_pins) == 22:
            if colour == 'r':
                pin = 20
            elif colour == 'b':
                pin = 11
            elif colour == 'g':
                pin = 19
            await board.set_pin_mode(pin, Constants.OUTPUT)
            await board.digital_write(pin, value)
    if port == 5:
        if len(board.digital_pins) == 70:
            if colour == 'r':
                pin = 12
            elif colour == 'b':
                pin = 52
            elif colour == 'g':
                pin = 51
            await board.set_pin_mode(pin, Constants.OUTPUT)
            await board.digital_write(pin, value)
        if len(board.digital_pins) == 22:
            if colour == 'r':
                pin = 12
            elif colour == 'b':
                pin = 2
            await board.set_pin_mode(pin, Constants.OUTPUT)
            await board.digital_write(pin, value)

    
            
async def dig_read(port):
    pin = dig_port2pin(port)
    await board.set_pin_mode(pin, Constants.INPUT)
    value = await board.digital_read(pin)
    return value
    
async def dig_write(port, value):
    pin = dig_port2pin(port)
    await board.set_pin_mode(pin, Constants.OUTPUT)
    await board.digital_write(pin, value)
    print(1)
        
async def ana_read(port):
    pin = ana_port2pin(port)
    await board.set_pin_mode(pin, Constants.ANALOG)
    value = await board.analog_read(pin)
    return value

async def ana_write(port, value):
    pin = ana_port2pin(port)
    await board.set_pin_mode(pin, Constants.OUTPUT)
    await board.analog_write(pin, value)

def get_ver():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(ver)

def serial_ports():    
    return serial.tools.list_ports.comports()

def on_select(event=None):
    #print(cb.get())
    #print("comboboxes: ", cb.get())
    #cp = cb.get()
    #print(cp)
    #comport = cp[:5]
    #print(comport)
    connect.enter()
    #board = PymataCore(com_port=comport())
    #board = PymataCore(com_port=cb.get())
    #board.start()
    
def delay(time):
    sleep(time)

def motor_run(port, speed, dire):
    #asyncio.run(motor(port, speed, dire))
    #motor(port, speed, dire)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(dc_motor(port, speed, dire))

def pump_motor_run(port, speed, dire):
    #asyncio.run(motor(port, speed, dire))
    #motor(port, speed, dire)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(dc_motor(port, speed, dire))


def rgb(port, color, value):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_rgb(port, color, value))

def servo_move(port,angle):
    print(angle)
    asyncio.run(servo(port, angle))
    #loop = asyncio.get_event_loop()
    #loop.run_until_complete(servo(port,angle))

def led(port, state):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(dig_led(port,state))

def ir_read(port):
    loop = asyncio.get_event_loop()
    val = loop.run_until_complete(dig_read(port))
    print(val)
    return val

def ldr_read(port):
    loop = asyncio.get_event_loop()
    val = loop.run_until_complete(ana_read(port))
    print(val)
    return(val)

def gas_read(port):
    loop = asyncio.get_event_loop()
    val = loop.run_until_complete(ana_read(port))
    print(val)
    return (val)

def buzzer(port, value):
    if value == 255:
        value = 1
    loop = asyncio.get_event_loop()
    loop.run_until_complete(dig_write(port, value))

def argb(pin,index, pixel, r, g, b):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_argb(pin, index, pixel, r, g, b))

def us(pin):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_us(pin))

def temp(pin):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_temp(pin))

def my_callback(data):
    print(data[1])

def bluetooth_connect_UI():
    global cb, root, TopFrame, MidFrame, BottomFrame
    root=tk.Tk()
    root.title("QTPI ROBOTICS")
    root.geometry('600x600+10+30')
    TopFrame = tk.Frame(root)
    TopFrame.pack()

    MidFrame = tk.Frame(root)
    MidFrame.pack()

    BottomFrame = tk.Frame(root)
    BottomFrame.pack()

    #InOutResult = tk.Entry(TopFrame, bd=5, width=40)
    #cp = InOutResult.grid(row=2, column=0)
    label = tk.Label(TopFrame, text = " Select comport", font=("Gentium Book Basic",15,"bold"), fg = 'white',bg='green').grid(row = 1, column = 0)
    cb = ttk.Combobox(TopFrame, values=serial_ports(), width=60)
    cb.grid(row = 2, column = 0)
    try:
        cb.bind('<<ComboboxSelected>>', on_select)
    except:
        delay(1)
    #root.mainloop()

    #label = tk.Label(TopFrame, text="Enter Port Number", font=('Gentium Book Basic', 15, 'bold'), fg='white',bg='green')
    #label.grid(row=1, column=0)

    #EnterButton = tk.Button(TopFrame, text="CONNECT", font=('Gentium Book Basic', 15, 'bold'), fg='white', bg='green',command=connect.enter)
    #EnterButton.grid(row=3, column=0, padx=5, pady=5)
    #root.mainloop()



class ui():
    global cb, root, TopFrame, MidFrame, BottomFrame
    root = tk.Tk()
    #window = tk.Toplevel(root)
    root.title("QtPi")
    root.geometry('600x600+10+30')
    TopFrame = tk.Frame(root)
    TopFrame.pack()
    MidFrame = tk.Frame(root)
    MidFrame.pack()
    BottomFrame = tk.Frame(root)
    BottomFrame.pack()
    def title(name):
        label=tk.Label(MidFrame, text = name,font = ('Gentium Book Basic',15,'bold'),fg='white',bg='blue4')
        label.grid(row=0,column=0)
    def button(name, command,row,column):
        button= tk.Button(MidFrame, text = name,font = ('Gentium Book Basic',15,'bold'),fg='white',bg='blue4',command=command) #Forwardbutton.pack( side = LEFT )
        button.grid(row=row, column=column,padx=5,pady=5)
    def print_value(val):
        val = int(val)
        print(val)
    def slider(min, max,ti,command):
        #scale = Scale(orient='horizontal', from_=min, to=max, tickinterval=ti ,command=command)
        #scale.pack()
        Scale(from_ = min, to=max, orient=HORIZONTAL,length=500,width=20, sliderlength=10,tickinterval=ti, command = command).pack()
    def notifier(content):
        messagebox.showinfo(content)
    def c_status():
        print(var1.get())
    def checkbox(name, row):
        #master = Tk()
        var1 = IntVar()
        Checkbutton(BottomFrame, text=name, variable=var1).grid(row=row, sticky=W)
        return var1
    def textbox(name, row, column):
        InOutResult = tk.Entry(MidFrame, bd=5, width=40)
        in_text = InOutResult.grid(row=row, column=column)
        return in_text
    #root.mainloop()

#get_ver()

