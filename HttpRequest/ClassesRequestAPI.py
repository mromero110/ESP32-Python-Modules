from HttpRequest.SIM800L import Modem
import json
#Starting SIM800L Connection:
print('Starting up...')
# Creamos un objeto modem para administrar SIM800L mediante el Módulo:
SIM800L = Modem(MODEM_TX_PIN= 22, MODEM_RX_PIN= 21)
# Inicializamos el Modem SIM800L:
SIM800L.initialize()
# Conectamos SIM800L al AP de la operadora  e imprimimos en pantalla:
SIM800L.connect(apn='internet.comcel.com.co', user='comcelweb', pwd='comcelweb') #leave username and password empty if your network don't require them
print('\nModem IP address: "{}"'.format(SIM800L.get_ip_addr()))

class ConnectionsAPI():
    def Get_AuthenticationRequest():
    # Inicializar Conexión Token GET:
        print('HTTP GET Start it, obtaining code device for supply:')
        url = 'http://isvaiot-001-site1.ftempurl.com/api/security/device/25645141414'
        response = SIM800L.http_request(url, 'GET')
        print('Response status code:', response.status_code)
        ID_Device_Request=response.content
        Decodificate=(json.loads(ID_Device_Request))
        global Code
        Code=(Decodificate["Code"])
        print(Code)
    # Enviar datos actuales Geolocalización GPS:
    def Post_Position_GPS_State(CodeDevice, Lat, Long, Presition):
        print('HTTP POST Position Actually GPS:')
        url  = 'http://isvaiot-001-site1.ftempurl.com/api/gps'
        data = json.dumps({"IdDispositivo": CodeDevice,"Id": 2,"Latitud": Lat,
                           "Longitud": Long,"Prescicion": Presition,
                           "Genera": "2022-01-24T23:30:29.6222346-08:00"})
        response = SIM800L.http_request(url, 'POST', data, 'application/json')
        #print('Response status code:', response.status_code)
        #print('Response content:', response.content)
    # Obtener configuración establecida Zona Wifi:
    def Get_Wifi_Zone_Dates():
        print('HTTP GET Wifi Zone Dates:')
        url = 'http://isvaiot-001-site1.ftempurl.com/api/zona/wifi/' + Code
        response = SIM800L.http_request(url, 'GET')
        print('Response status code:', response.status_code)
        print('Response content:', response.content)

    # Obtener parametros conexion Wifi Zona Segura:
    def Get_Secure_Zones_Wifi():
        print('HTTP GET Secure Zone Wifi Dates:')
        url = 'http://isvaiot-001-site1.ftempurl.com/api/zona/segura/' + Code
        response = SIM800L.http_request(url, 'GET')
        print('Response status code:', response.status_code)
        print('Response content:', response.content)
     # Obtener configuración Dispositivo:
    def Get_Configurations_Device():
        print('HTTP GET Configurations Device:')
        url = 'http://isvaiot-001-site1.ftempurl.com/api/dispositivo/' + Code + '/serial/' + Code
        response = SIM800L.http_request(url, 'GET')
        print('Response status code:', response.status_code)
        print('Response content:', response.content)

        
#1:   APIConnection= ConnectionsAPI
#2 :  APIConnection.Get_AuthenticationRequest()
#3 :   APIConnection.Post_Position_GPS_State(1, 4545474, 463778, 2)
APIConnection= ConnectionsAPI
APIConnection.Get_AuthenticationRequest()
APIConnection.Get_Configurations_Device()