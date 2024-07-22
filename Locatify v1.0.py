from customtkinter import *
from PIL import Image
import tkintermapview

def det():
    map.delete_all_marker()
def search():
    global remove
    contry=entry.get()
    map.set_address(contry,marker=True)
    remove= CTkButton(frame2,command=det,text="remove all markers" ,height=20,width=160,hover_color="#333333",border_color="#008170",corner_radius=12,border_width=2,fg_color="#005B41")
    remove.place(x=220,y=510)
def usa():
    global remove
    map.set_address("united state of america",marker=True) 
    map.set_zoom(2)
    remove= CTkButton(frame2,command=det,text="remove all markers" ,height=20,width=160,hover_color="#333333",border_color="#008170",corner_radius=12,border_width=2,fg_color="#005B41")
    remove.place(x=220,y=510)
def iraq():
    global remove
    map.set_address("iraq",marker=True) 
    map.set_zoom(6)
    remove= CTkButton(frame2,command=det,text="remove all markers" ,height=20,width=160,hover_color="#333333",border_color="#008170",corner_radius=12,border_width=2,fg_color="#005B41")
    remove.place(x=220,y=510)
def saudi():
    global remove
    map.set_address("المملكة العربية السعودية",marker=True) 
    map.set_position(23.559175877765366, 45.140001313992066) 
    map.set_zoom(5)
    remove= CTkButton(frame2,command=det,text="remove all markers" ,height=20,width=160,hover_color="#333333",border_color="#008170",corner_radius=12,border_width=2,fg_color="#005B41")
    remove.place(x=220,y=510)
def Iran():
    global remove
    map.set_address("iran",marker=True) 
    map.set_zoom(5)
    remove= CTkButton(frame2,command=det,text="remove all markers" ,height=20,width=160,hover_color="#333333",border_color="#008170",corner_radius=12,border_width=2,fg_color="#005B41")
    remove.place(x=220,y=510)
def Jordan():
    global remove
    map.set_address("الأردن",marker=True) 
    map.set_zoom(7)
    remove= CTkButton(frame2,command=det,text="remove all markers" ,height=20,width=160,hover_color="#333333",border_color="#008170",corner_radius=12,border_width=2,fg_color="#005B41")
    remove.place(x=220,y=510)
def russia():
    global remove
    map.set_address("روسيا",marker=True) 
    map.set_zoom(2)
    remove= CTkButton(frame2,command=det,text="remove all markers" ,height=20,width=160,hover_color="#333333",border_color="#008170",corner_radius=12,border_width=2,fg_color="#005B41")
    remove.place(x=220,y=510)
def turkey():
    global remove
    map.set_address("Turkey",marker=True) 
    map.set_zoom(5)
    remove= CTkButton(frame2,command=det,text="remove all markers" ,height=20,width=160,hover_color="#333333",border_color="#008170",corner_radius=12,border_width=2,fg_color="#005B41")
    remove.place(x=220,y=510)
def japan():
    global remove
    map.set_address("japan",marker=True) 
    map.set_zoom(5)
    remove= CTkButton(frame2,command=det,text="remove all markers" ,height=20,width=160,hover_color="#333333",border_color="#008170",corner_radius=12,border_width=2,fg_color="#005B41")
    remove.place(x=220,y=510)

#logo
logo   = CTkImage(light_image=Image.open("mainlogo.png"),size=(288, 82))

window = CTk()
window.geometry   ('1503x705+0+0'),window.title('locatify v1.0'),window.configure(fg_color="#333333"),window.iconbitmap('assets\\Locatify.ico')
frame  = CTkFrame (window,fg_color="#333333",bg_color="#333333",border_color="#008170",height=425,width=500,border_width=3,corner_radius=12)
LOGO   = CTkLabel (frame,text=" ",image=logo)
entry  = CTkEntry (frame,placeholder_text_color="white",placeholder_text="france..",border_color="#008170",fg_color="#005B41",width=130,height=30,border_width=3,font=(("Segoe"),15))
button = CTkButton(frame,command=search,text="Search",hover_color="#333333",border_width=0,corner_radius=0,border_color="#008170",width=40,height=20,bg_color="#008170",fg_color="#005B41")
frame2 = CTkFrame (frame,corner_radius=12,border_width=2,border_color="#008170",fg_color="#232D3F",width=400,height=550)
frame3 =CTkFrame  (frame,width=500,border_width=3,corner_radius=12,height=50,border_color="#008170",bg_color="#008170",fg_color="#333333")
label  = CTkLabel (frame3,text="stormtools\nlocatify-2024 simple map veiwer",font=(("Segoe"),10),text_color="#008170")

#places
frame .pack(fill=Y,side=LEFT)
LOGO  .place(x=50,y=5)
entry .place(x=350,y=55)
button.place(x=430,y=60)
frame2.place(x=50,y=95)
frame3.pack(side=BOTTOM,fill=X)
label .place(x=160,y=10)
#flags and lands ============================
IRAN = CTkImage(light_image=Image.open("assets\\iran.png")  ,size=(60, 60))
USA  = CTkImage(light_image=Image.open("assets\\usa.png")   ,size=(60, 60))
IRAQ = CTkImage(light_image=Image.open("assets\\iraq.png")  ,size=(60, 60))
KSA  = CTkImage(light_image=Image.open("assets\\ksa.png")   ,size=(60, 60))
JOR  = CTkImage(light_image=Image.open("assets\\jordan.png"),size=(60, 60))
RUS  = CTkImage(light_image=Image.open("assets\\russia.png"),size=(60, 60))
TRK  = CTkImage(light_image=Image.open("assets\\Turkey.png"),size=(60, 60))
jpn  = CTkImage(light_image=Image.open("assets\\japan.png") ,size=(60, 60))
#contury        master  compound     flag      command       name#               
usa = CTkButton(frame2,compound=TOP,image=USA ,command=usa,text="United State\nof america"            ,height=50,width=160,hover_color="#333333",border_color="#008170",corner_radius=12,border_width=2,fg_color="#005B41")
iqd = CTkButton(frame2,compound=TOP,image=IRAQ,command=iraq,text="The republic \nof iraq"             ,height=50,width=160,hover_color="#333333",border_color="#008170",corner_radius=12,border_width=2,fg_color="#005B41")
ksa = CTkButton(frame2,compound=TOP,image=KSA,command=saudi,text="the kingdom \nof saudi arabia"      ,height=50,width=160,hover_color="#333333",border_color="#008170",corner_radius=12,border_width=2,fg_color="#005B41")
irn = CTkButton(frame2,command=Iran,compound=TOP,image=IRAN,text="The Islamic Republic\n of Iran"     ,height=50,width=160,hover_color="#333333",border_color="#008170",corner_radius=12,border_width=2,fg_color="#005B41")
jrdn= CTkButton(frame2,compound=TOP,image=JOR,command=Jordan,text="Hashemite Kingdom \nof Jordan"     ,height=50,width=160,hover_color="#333333",border_color="#008170",corner_radius=12,border_width=2,fg_color="#005B41")
rus = CTkButton(frame2,compound=TOP,image=RUS,command=russia,text="the Russian\n Federation"          ,height=50,width=160,hover_color="#333333",border_color="#008170",corner_radius=12,border_width=2,fg_color="#005B41")
trk = CTkButton(frame2,compound=TOP,image=TRK,command=turkey,text="the Republic \nof Turkey "         ,height=50,width=160,hover_color="#333333",border_color="#008170",corner_radius=12,border_width=2,fg_color="#005B41")
jpan= CTkButton(frame2,compound=TOP,image=jpn,command=japan,text="Nippon-koku 日本国\n State of Japan" ,height=50,width=160,hover_color="#333333",border_color="#008170",corner_radius=12,border_width=2,fg_color="#005B41")
#main-map
map = tkintermapview.TkinterMapView(window, width=1503, height=300, corner_radius=12)

map.set_zoom(1)

#places
usa.place(x=25,y=10)
iqd.place(x=220,y=10)
ksa.place(x=25,y=130)
irn.place(x=220,y=130)
jrdn.place(x=25,y=250)
rus.place(x=220,y=250)
trk.place(x=25,y=370)
jpan.place(x=220,y=370)

map.pack(side=RIGHT,fill=Y)
window.mainloop()