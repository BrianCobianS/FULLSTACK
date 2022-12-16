#!/bin/bash
mkdir /home/ebossteam/temp/10.89.105.98
cp -r /home/ebossteam/UnattendedInstallation/FULLSTACK/Back-End/ansible/* /home/ebossteam/temp/10.89.105.98
python3 /home/ebossteam/UnattendedInstallation/FULLSTACK/Back-End/public/Inventories/Inventory.py 10.89.105.98 master m1
echo $(date +%Y%m%d_%H%M) > /home/ebossteam/temp/10.89.105.98/date.txt
ansible-playbook /home/ebossteam/temp/10.89.105.98/playbooks/os4690/Install_Controller.yml -vv  -i /home/ebossteam/temp/10.89.105.98/Inventories/import_inventory.yml -e 'level_complement=V8R1SP2.j305-20221208.173413-1 opc=1 ASM=Accept level_name=V8R1SP2.j305 level_complementEPS=V8R1SP2.j305-20221208.173431-1 Tcxpay=1 level_complementTcxpay=V8R1SP2.j305-20221208.173440-1 Common=1 level=1.2.11--19 PinPad=1 levelPIN=1.2.7--7' 2>&1 | tee /var/log/logscontroladores/10.89.105.98-$(date +%Y%m%d_%H%M).txt
rm -r /home/ebossteam/temp/10.89.105.98
python3 /home/ebossteam/UnattendedInstallation/FULLSTACK/mails/email.py 10.89.105.98 master m1 1 V8R1SP2.j305 Accept Now Jedi brian.cobian@alumnos.udg.mx
node /home/ebossteam/UnattendedInstallation/FULLSTACK/mails/mail.js