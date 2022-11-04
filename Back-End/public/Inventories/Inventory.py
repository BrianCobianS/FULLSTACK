import sys
IP=(sys.argv[1])
USR=(sys.argv[2])
PASS=(sys.argv[3])
OPC=(sys.argv[4])
print(IP,USR,PASS)
def controller(host,user,password):
    # contenido = open("./Inventories/template.txt").read().splitlines()
    contenido = open("C:/Users/brian.cobian/Desktop/IMDesatendida/Fullstackpage/Back-End/public/Inventories/template.txt").read().splitlines()
    contenido.insert(6,"            "+host)
    contenido.remove("            host")
    contenido.insert(9,"        ansible_user: "+user)
    contenido.remove("        ansible_user: master")
    contenido.insert(10,"        ansible_ssh_pass: "+password)
    contenido.remove("        ansible_ssh_pass: m1")
    # f = open('./Inventories/import_inventory.yml', "w")
    f = open('C:/Users/brian.cobian/Desktop/IMDesatendida/Fullstackpage/Back-End/public/Inventories/import_inventory.yml', "w")
    f.writelines("\n".join(contenido))
controller(IP,USR,PASS)
def auto(opc):
    contenido = open('C:/Users/brian.cobian/Desktop/IMDesatendida/Fullstackpage/Back-End/public/Inventories/auto.txt').read().splitlines()
    contenido.insert(len(contenido),opc)
    print(contenido)
    f = open('C:/Users/brian.cobian/Desktop/IMDesatendida/Fullstackpage/Back-End/public/playbooks/os4690/roles/installation/files/AUTO.BAT', "w")
    f.writelines("\n".join(contenido))
auto(str(OPC))


