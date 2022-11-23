from tkinter import *
import random

root = Tk()

root.title("Display the Country and City`")
root.geometry("600x600")

entry_country = Entry(root, font=("courier, 15"))
entry_city = Entry(root, font=("courier, 15"))

label_country_list =  Label(root, font=("courier, 15"), fg="green", bg="yellow", padx ="10", pady="5")
label_city_list =  Label(root, font=("courier, 15"), fg="green", bg="yellow", padx ="10", pady="5")
country_list = []
city_list = []

def addToList():
  country = entry_country.get()
  country_list.append(country)
  city = entry_city.get()
  city_list.append(city)
  label_country_list['text'] = "Country list = "+str(country_list)
  label_city_list['text'] = "City List = "+str(city_list)
label_random_country =  Label(root, font=("courier, 15"), fg="green", bg="yellow", padx ="10", pady="5")

label_random_city =  Label(root, font=("courier, 15"), fg="green", bg="yellow", padx ="10", pady="5")

def randomCombo():
  length = len(country_list)
  random_no = random.randint(0,length-1)
  random_country = country_list[random_no]
  random_city = city_list[random_no]
  label_random_country['text'] = "Country = " + random_country

  label_random_city['text'] = "City = " + random_city


btn =  Button(root, text= "Display Country And City Name", command=addToList , font=("courier, 15"), bg="orange", padx ="15", pady="25")
btn2 =  Button(root, text= "Display Country And City Name Randomly", command=randomCombo , font=("courier, 15"), bg="orange", padx ="15", pady="25")

entry_country.place(relx=0.5, rely=0.2, anchor=CENTER)
entry_city.place(relx=0.5, rely=0.3, anchor=CENTER)
btn.place(relx=0.5, rely=0.4, anchor=CENTER)
label_country_list.place(relx=0.5, rely=0.5, anchor=CENTER)
label_city_list.place(relx=0.5, rely=0.6, anchor=CENTER)
btn2.place(relx=0.5, rely=0.7, anchor=CENTER)
label_random_country.place(relx=0.5, rely=0.8, anchor=CENTER)
label_random_city.place(relx=0.5, rely=0.9, anchor=CENTER)
root.mainloop()
