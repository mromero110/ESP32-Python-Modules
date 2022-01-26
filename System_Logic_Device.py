from machine import UART, Pin #Uart para SIM800L y Pin para administrar Relé
#uart = UART(1, 115200, timeout=2000, rx=22, tx=21) #Creamos una variable para indicarle las entradas de la SIM800L mediante UART
import utime
import Client_AP_Configuration.Client_AP as AP
import HttpRequest.ClassesRequestAPI as API
import GPS.GPS_Position as GPS
############################### Start Principal Variables definition ######################################
#Definición de variables:
Electric_System=Pin(18, Pin.OUT)
TurnOff_Emergency_App=False #Apagado de emergencia.
TurnOff_Wifi_Zone=False     #Apagado por desconexión zona Wifi.  ---Esp32 Camara --- Exitosa--- 
TurnOff_Facial_Recognition=False    #Mantener apagado si no logra reconocimiento facial.
#Opción App, activar o desactivar Zona Wifi Segura, Zona GPS Segura y reconocimiento facial:
WebSock_Disable_Wifi_Zone=False  #Activar o desactivar Zona Wifi segura desde App.
WebSock_Disable_Facial_Recognition=False  #Activar o desactivar Reconocimiento Facial desde App.
#WebSock_Disable_GPS_Zone=False  #Activar o desactivar Zona GPS segura desde App.
############################### End Principal Variables definition ######################################
############################### Start Json Import Configurations Instances ######################################
APIConnection= API.ConnectionsAPI
Connect_Wifi=AP.Connection_Wifi
Geolocalization=GPS.GetLocation
############################### End Json Import Configurations Instances ######################################

#Definición de funciones: 
def Emergency_Blocker(Order):  #  1  Significa que esta apagado el sistema electrico.
    Emergency_Block=Electric_System.value(Order)  # 0 Significa que el sistema electrico está encendido.
#Inicio bucle infinito:    
while True:
#Start Authentication API and Obtain ID_Device:
    APIConnection.Get_AuthenticationRequest()
#Validations Wifi:
    Connect_Wifi.Config_Parameter_Wifi('Animathionware','Lunes*123')
    Check_State=AP.Connection_Wifi_State       #Assing Class to Object
    Check_State.Validate_Connection_Client()   #Check connection Wifi function
#Start Traker GPS and Send API Paramethers:
    Geolocalization.Tracking_GPS()
    APIConnection.Post_Position_GPS_State(API.Code, GPS.lat, GPS.long, 0)  

#Si el cliente ESP32 está conectado en el server, entonces el apagado de emergencia por Wifi será
#deshabilitado, pero si esta desconectado el ciente, entonces el apagado de emergencia se activará:
    #print(AP.Client_Connected)  Funciona OK
    if (AP.Client_Connected==True):
        TurnOff_Wifi_Zone=False
        print('Cliente Conectado, no hay necesidad de apagar automotor.')
    elif(AP.Client_Connected==False):
        TurnOff_Wifi_Zone=True
        print('No existe cliente conectado.')
    print(TurnOff_Wifi_Zone,WebSock_Disable_Wifi_Zone)
#Protección:
    if (TurnOff_Wifi_Zone==True and WebSock_Disable_Wifi_Zone==False):
        Emergency_Blocker(1)
    elif (TurnOff_Facial_Recognition==True and WebSock_Disable_Facial_Recognition==False):
        Emergency_Blocker(1)
    elif (TurnOff_Emergency_App==True):
        Emergency_Blocker(1)
    else:
        Emergency_Blocker(0)
    utime.sleep(1)

 

