#Name:- Karthik D
from tkinter import*
import sys
import requests
###################


#########################
root=Tk()
y='#ffc13b'
b='#1e3d59'
o='#ff6e40'
w='#f5f5f5'
fg='courier 15 '
######################
global text, st,link
tet =StringVar()#to get city name using tkinter

tet.set('Enter the City Name')#setting value


#######################################################
def ex():
    sys.exit()
def check():
    global l11, st,tet,link
    API_KEY='User api key from openweathermap.org'
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    URL = BASE_URL + "q=" + tet.get()+ "&appid=" + API_KEY
    # HTTP request
    response = requests.get(URL)
    sm=tet.get().center(20,'-')+'\n'
    if response.status_code == 200:
        # getting data in the json format
        data = response.json()
        # getting the main dict block
        main = data['main']
        # getting temperature
        temperature = main['temp']
        # getting the humidity
        humidity = main['humidity']
        # getting the pressure
        pressure = main['pressure']
        # weather report
        report = data['weather']
        sm+='Temperature: '+str(round(temperature-273.15,2))+' Degree C\nHumidity: '+str(humidity)+'%\nPressure: '+str(pressure)+'\nWeather Report'+str(report[0]['description'])
        sm+='\n'+''.center(20,'-')
        l11.config(text=sm)

    else:
        l11.config(text="Error in the HTTP request")





root.config(bg=w)
root.geometry('600x600')
l1=Label(root,text='Weather Checking Using Python',fg=o,relief='flat',font=fg,justify='center')
l1.pack(pady=5)
l1=Label(root,bg=b,text=' ',fg=b, width =200,relief='flat',font=fg,justify='center')
l1.pack(pady=5)

l1=Entry(root,bg=y,text=tet,fg=b,relief=FLAT,font=fg,justify='center')
l1.pack(pady=5)
l1=Button(root,bg=y,text='search',fg=b,relief='ridge',font=fg,justify='center',command=check)
l1.pack(pady=5)
frame=Frame(root)
frame.pack()
l11=Label(frame,bg=w,text='',fg=b,relief='flat',font='courier 15',justify='center')
l11.pack(pady=5)

l1=Button(root,bg=y,text='Quit',fg=b,relief=FLAT,font=fg,justify='center',command=ex)
l1.pack(pady=5)
l1=Label(root,bg=b,text=' ',fg=y, width =200,relief=FLAT,font=fg,justify='center')
l1.pack(pady=5)





root.mainloop()
