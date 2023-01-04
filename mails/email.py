import sys
IP=(sys.argv[1])
USR=(sys.argv[2])
PASS=(sys.argv[3])
OPC=(sys.argv[4])
LEV=(sys.argv[5])
ASM=(sys.argv[6])
FECHA=(sys.argv[7])
VERSION=(sys.argv[8])
EMAIL=(sys.argv[9])
COMMON=(sys.argv[10])
PINPAD=(sys.argv[11])
#pruebas  python email.py 12.12.12 master m1 1 12.ver12 accept 12712/12 Morty brian.cobian@toshibagcs.com
print(IP,USR,PASS,OPC,LEV,ASM,FECHA,VERSION,EMAIL,COMMON,PINPAD)
def createmail(message,path,boleano,msgs):
    # contenido = open("C:/Users/brian.cobian/Desktop/IMDesatendida/Correohtml/mail-node/email.txt").read().splitlines()
    contenido = open("/home/ebossteam/UnattendedInstallation/FULLSTACK/mails/email.txt").read().splitlines()
    contenido.insert(2,"    ip: '"+IP+"',")
    contenido.insert(2,"    usr: '"+USR+"',")
    contenido.insert(2,"    pass: '"+PASS+"',")
    contenido.insert(2,"    email: '"+EMAIL+"',")
    contenido.insert(2,"    nivel: '"+LEV+"',")
    contenido.insert(2,"    version: '"+VERSION+"',")
    contenido.insert(2,"    paquetes: 'ACE,EPS',")
    contenido.insert(2,"    ASM: '"+ASM+"',")
    contenido.insert(2,"    fecha: '"+FECHA+"',")
    contenido.insert(2,"    opc: '"+OPC+"',")
    contenido.insert(2,"    message: '"+message+"',")
    contenido.insert(2,"    path: '"+path+"',")
    contenido.insert(2,"    boleano: '"+str(boleano)+"',")
    contenido.insert(2,"    ACE: '"+msgs[0]+ "',")
    contenido.insert(2,"    EPS: '"+msgs[1]+"',")
    contenido.insert(2,"    Tcxpay: '"+msgs[2]+"',")
    contenido.insert(2,"    TcxpayPin: '"+msgs[3]+"',")
    contenido.insert(2,"    TcxpayCom: '"+msgs[4]+"',")
    contenido.insert(2,"    TcxpayComVer: '"+COMMON+"',")
    contenido.insert(2,"    TcxpayPinVer: '"+PINPAD+"',")
    f = open('/home/ebossteam/UnattendedInstallation/FULLSTACK/mails/mail.js', "w")
    # f = open('C:/Users/brian.cobian/Desktop/IMDesatendida/Correohtml/mail-node/mail.js', "w")

    f.writelines("\n".join(contenido))
    f.close

# def installationerror(linea):
#     iner=linea.find('RUNNING')
#     lineatemp=linea[iner:-1]
#     cut= lineatemp.find('u0')
#     Error1= lineatemp[80:cut-1]
#     return Error1

def changeBat(fileDirectory):
    with open(fileDirectory,'r') as archivo:
        ban = 0
        ban1 = 0
        i=0
        Error1=''
        Exito=0
        lineatemp=''
        reserva=[]
        resultados = [0] * 5
        msgs = ['Not installed'] * 5
        Error='The installation failed, the error message is: '
        Succes= 'The installation was successful, the current controller version is '+LEV+'\t\t\t'
        for linea in archivo:
            # print(linea)
            linea=linea.rstrip('\n')
            reserva.append(linea)
            if 'ADXCST0L Y 'in linea:
                if 'AG  BY' in linea: ##ACE3D
                    if 'SUCCESS' in linea:
                        print('ACE3D se instalo con exito')
                        resultados[0] = 1
                        msgs[0]='The installation was successful'
                    else :
                        print('Falló la instalación de ACE3D')
                        iner=linea.find('RUNNING')
                        lineatemp=linea[iner:-1]
                        cut= lineatemp.find('u0')
                        Error1= lineatemp[80:cut-1]
                        print(Error1)
                        if Error1 != '':
                            msgs[0]='Failed: ' +Error1
                if 'AI  BY' in linea: ##ACE4D
                    if 'SUCCESS' in linea:
                        resultados[1] = 1
                        msgs[1]='The installation was successful'
                        print('ACE4D se instalo con exito')
                    else :
                        print('Falló la instalación de ACE4D')
                        iner=linea.find('RUNNING')
                        lineatemp=linea[iner:-1]
                        cut= lineatemp.find('u0')
                        Error1= lineatemp[80:cut-1]
                        print(Error1)
                        if Error1 != '':
                            msgs[1]='Failed: ' +Error1
                if 'DA  BY' in linea: ##ACE6D
                    if 'SUCCESS' in linea:
                        resultados[2] = 1
                        msgs[2]='The installation was successful'
                        print('ACE6D se instalo con exito')
                    else :
                        print('Falló la instalación de ACE6D')
                        iner=linea.find('RUNNING')
                        lineatemp=linea[iner:-1]
                        cut= lineatemp.find('u0')

                        Error1= lineatemp[80:cut-1]
                        print(Error1)
                        if Error1 != '':
                            msgs[2]='Failed: ' +Error1
                if 'EC  BY' in linea: ##Common
                    if 'SUCCESS' in linea:
                        msgs[3]='The installation was successful'
                        resultados[3] = 1
                        print('Tcxpaycommon se instalo con exito')
                    else :
                        print('Falló la instalación de Tcxpaycommon')
                        iner=linea.find('RUNNING')
                        lineatemp=linea[iner:-1]
                        cut= lineatemp.find('u0')
                        Error1= lineatemp[80:cut-1]
                        print(Error1)
                        if Error1 != '':
                            msgs[3]='Failed: ' +Error1
                if 'FI  BY' in linea: #PinPad
                    if 'SUCCESS' in linea:
                        msgs[4]='The installation was successful'
                        resultados[4] = 1
                        print('TcxpayPinPad se instalo con exito')
                    else :
                        print('Falló la instalación de TcxpayPinPad')
                        iner=linea.find('RUNNING')
                        lineatemp=linea[iner:-1]
                        cut= lineatemp.find('u0')
                        Error1= lineatemp[80:cut-1]
                        print(Error1)
                        if Error1 != '':
                            msgs[4]='Failed: ' +Error1
            if 'SUCCES' in linea:
                 Exito=1
            if 'Print RML' in linea or ban==1:
                # Succes=Succes+linea
                ban=1
            i += 1
    print('Esta es la lista: ', resultados)
    print(msgs)
    if Exito ==1:
        print(Succes)
        createmail(Succes,fileDirectory,Exito,msgs)
    elif Exito==0:
        Error=Error+ Error1
        print(Error)
        createmail(Error,fileDirectory,Exito,msgs)
    else:
        print('No se sabe que sucedio revisar log')
        createmail('No se sabe que sucedio revisar log',fileDirectory,Nose=-1)

x= open("/home/ebossteam/temp/"+IP+"/date.txt",'r')
for x in x:
    date=x.rstrip('\n')
print(date)
# date = '20221230_1217'

changeBat("/var/log/logscontroladores/"+IP+"-"+date+".txt")

# changeBat("C:/Users/brian.cobian/Desktop/IMDesatendida/Correohtml/mail-node/log.txt")




