#Importar la liberria de notificacionde windows
import win10toast
#Importar la libreria del tiempo
import datetime 
#Vamos a ver si arreglamos esto de pathing

filedir = "icono.ico" #Padre ayudame a identificar como es que se busca el pathing aqui
toaster = win10toast.ToastNotifier()
now = datetime.datetime.now()

#Esta vaina jala la libreria y la ponte a mostrarse. Cuidado con los parentesis
toaster.show_toast ("Son las",now.strftime("%I:%M %p"),
icon_path=filedir,duration=60)
