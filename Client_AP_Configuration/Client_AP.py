import network
import utime
#Configuración inicial de WiFi
wlan = network.WLAN(network.STA_IF) #Inializamos modo de conexión cliente Wifi.
wlan.active(True) #Activa el Wifi
wlan.disconnect()
utime.sleep(2)
 
class Connection_Wifi():
    def Config_Parameter_Wifi(Name, Pass):
        global ssid
        ssid = Name  #Nombre de la Red
        global password
        password = Pass #Contraseña de la red
        #wlan.connect(ssid, password) #Hacemos la conexión
        utime.sleep(3)
class Connection_Wifi_State():
    def Validate_Connection_Client():
            if (wlan.isconnected() == True):
                print('Conexion con el WiFi %s establecida' % ssid)
                print(wlan.ifconfig()) #Muestra la IP y otros datos del Wi-Fi
                global Client_Connected
                Client_Connected=True
                utime.sleep(3)
            elif (wlan.isconnected() == False):
                print('Wifi desconectado')
                Client_Connected=False
                wlan.active(True)
                utime.sleep(3)
                wlan.disconnect()
                utime.sleep(3)
                wlan.connect(ssid, password)
                utime.sleep(3)
#while True:
#    Wifi=Connection_Wifi
#    Wifi.Config_Parameter_Wifi('Animathionware','Lunes*123')
#    Validate=Connection_Wifi_State
#    Validate.Validate_Connection_Client()
#    print(Client_Connected)


 