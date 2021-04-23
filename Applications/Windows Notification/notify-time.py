#For begginers like me
#Remember to pip install win10toast first
import win10toast
#Import datetime library
import datetime 
#Cant get the icon to show on windows

filedir = "icono.ico" 
toaster = win10toast.ToastNotifier()
now = datetime.datetime.now()

#This is in spanish, change it
toaster.show_toast ("Son las",now.strftime("%I:%M %p"),
icon_path=filedir,duration=60)
