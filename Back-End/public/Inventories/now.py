import sys
IP=(sys.argv[1])
USR=(sys.argv[2])
PASS=(sys.argv[3])
OPC=(sys.argv[4])
COMP=(sys.argv[5])
LEV=(sys.argv[6])
ASM=(sys.argv[7])
FECHA=(sys.argv[8])
VERSION=(sys.argv[9])
EMAIL=(sys.argv[10])
EPS=(sys.argv[11])
EPSCOMPLE=(sys.argv[12])
TCXPAY=(sys.argv[13])
TCXPAYCOMPLE=(sys.argv[14])
COMMON=(sys.argv[15])
PINPAD=(sys.argv[16])
print(IP,USR,PASS,OPC,COMP,LEV,ASM,FECHA,VERSION,EMAIL,EPS,EPSCOMPLE,TCXPAY,TCXPAYCOMPLE,COMMON,PINPAD)
if COMMON != str(0):
    COMMONOPC='1'
else: 
    COMMONOPC='0'
if PINPAD != str(0):
    PINPADOPC='1'
else: 
    PINPADOPC='0'
# print(PINPADOPC,COMMONOPC)

# contenido = open("C:/Users/brian.cobian/Desktop/IMDesatendida/Fullstack-Linux/Back-End/public/Inventories/shceduled.sh").read().splitlines()
contenido = open("/home/ebossteam/UnattendedInstallation/FULLSTACK/Back-End/public/Inventories/shceduled.sh").read().splitlines()
print(contenido)
contenido.insert(1,"mkdir /home/ebossteam/temp/"+IP)
# print("mkdir /home/ebossteam/temp/"+IP)
contenido.insert(2,"cp -r /home/ebossteam/UnattendedInstallation/FULLSTACK/Back-End/ansible/* /home/ebossteam/temp/"+IP)
# print("cp -r /home/ebossteam/ansibletest/ansible/* /home/ebossteam/temp/"+IP)
contenido.insert(3,"python3 /home/ebossteam/UnattendedInstallation/FULLSTACK/Back-End/public/Inventories/Inventory.py "+IP+" "+USR+" "+PASS)
# print("python3 /home/ebossteam/UnattendedInstallation/FULLSTACK/Back-End/public/Inventories/Inventory.py "+IP+" "+USR+" "+PASS)
# contenido.insert(4,"cp /home/ebossteam/UnattendedInstallation/FULLSTACK/Back-End/public/Inventories/AUTO.BAT /home/ebossteam/temp/"+IP+"/playbooks/os4690/roles/installation/files/")
# print("cp /home/ebossteam/UnattendedInstallation/FULLSTACK/Back-End/public/Inventories/AUTO.BAT /home/ebossteam/temp/"+IP+"/playbooks/os4690/roles/installation/files/")
# contenido.insert(5,"echo "+OPC+" >> /home/ebossteam/temp/"+IP+"/playbooks/os4690/roles/installation/files/AUTO.BAT")
# print("echo "+OPC+" >> /home/ebossteam/temp/"+IP+"/playbooks/os4690/roles/installation/files/AUTO.BAT")
contenido.insert(4,"echo $(date +%Y%m%d_%H%M) > /home/ebossteam/temp/"+IP+"/date.txt")
# print("echo $(date +%Y%m%d_%H%M) > /home/ebossteam/temp/"+IP+"/date.txt")
contenido.insert(5,"ansible-playbook /home/ebossteam/temp/"+IP+"/playbooks/os4690/Install_Controller.yml -vv  -i /home/ebossteam/temp/"+IP+"/Inventories/import_inventory.yml -e 'level_complement="+COMP+" opc="+OPC+" ASM="+ASM+" level_name="+LEV+" level_complementEPS="+EPSCOMPLE+" Tcxpay="+TCXPAY+" level_complementTcxpay="+TCXPAYCOMPLE+" Common="+COMMONOPC+" level="+COMMON+" PinPad="+PINPADOPC+" levelPIN="+PINPAD+"' 2>&1 | tee /var/log/logscontroladores/"+IP+"-$(date +%Y%m%d_%H%M).txt")
# print("ansible-playbook /home/ebossteam/temp/"+IP+"/playbooks/os4690/Install_Controller.yml -vv  -i /home/ebossteam/temp/"+IP+"/Inventories/import_inventory.yml -e 'level_complement="+COMP+" opc="+OPC+" ASM="+ASM+" level_name="+LEV+"' 2>&1 | tee /var/log/logscontroladores/"+IP+"-$(date +%Y%m%d_%H%M).txt")

# print("rm -r /home/ebossteam/temp/"+IP)
contenido.insert(6,"python3 /home/ebossteam/UnattendedInstallation/FULLSTACK/mails/email.py "+IP+" "+USR+" "+PASS+" "+OPC+" "+LEV+" "+ASM+" "+FECHA+" "+VERSION+" "+EMAIL)
# print("python3 /home/ebossteam/UnattendedInstallation/FULLSTACK/mails/email.py "+IP+" "+USR+" "+PASS+" "+OPC+" "+LEV+" "+ASM+" "+FECHA+" "+VERSION+" "+EMAIL)
contenido.insert(7,"node /home/ebossteam/UnattendedInstallation/FULLSTACK/mails/mail.js")
contenido.insert(8,"rm -r /home/ebossteam/temp/"+IP)
# print("node /home/ebossteam/UnattendedInstallation/FULLSTACK/mails/mail.js")
# f = open('C:/Users/brian.cobian/Desktop/IMDesatendida/Fullstack-Linux/Back-End/public/Inventories/controllers/'+IP+'.sh', "w")
f = open('/home/ebossteam/UnattendedInstallation/FULLSTACK/Back-End/public/Inventories/controllers/'+IP+'.sh', "w")
f.writelines("\n".join(contenido))
