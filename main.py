from  tkinter import *
import ipaddress
window = Tk()
window.title("IP Converter to binary")
window.minsize(height= 200, width=300)




header = Label(window, text="IP Address Converter")
header.grid(row=1, column=2)


Label(window, text="Enter IP Address").grid(row=4, column=1)
ipaddressinput = Entry(window).grid(row=4, column=2)


def OnClick():
    value = str(ipaddressinput)
    ip = ipaddress.ip_address(ipaddressinput)
    binaryIP = bin(int(ip))

    Label(window, text=str(binaryIP)).grid(row=8, column=1)

Button(window, text="Convert Now", command=OnClick).grid(row=6, column=2)



#Label(window, text="IP Address Converter").grid(row=3, column=3)


window.mainloop()