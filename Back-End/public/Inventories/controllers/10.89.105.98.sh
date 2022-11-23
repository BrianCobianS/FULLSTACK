#!/bin/bash
mkdir /home/ebossteam/temp/10.89.105.98
cp -r /home/ebossteam/ansibletest/ansible/* /home/ebossteam/temp/10.89.105.98
python3 /home/ebossteam/UnattendedInstallation/FULLSTACK/Back-End/public/Inventories/Inventory.py 10.89.105.98 master m1
cp /home/ebossteam/UnattendedInstallation/FULLSTACK/Back-End/public/Inventories/AUTO.BAT /home/ebossteam/temp/10.89.105.98/playbooks/os4690/roles/installation/files/
echo 2 >> /home/ebossteam/temp/10.89.105.98/playbooks/os4690/roles/installation/files/AUTO.BAT
echo $(date +%Y%m%d_%H%M) > /home/ebossteam/temp/10.89.105.98/date.txt
ansible-playbook /home/ebossteam/temp/10.89.105.98/playbooks/os4690/Install_Controller.yml -vv  -i /home/ebossteam/temp/10.89.105.98/Inventories/import_inventory.yml -e 'level_complement=V8R2.l125.7-20221107.200831-1 opc=2 ASM=Test level_name=V8R2.l125.7' 2>&1 | tee /var/log/logscontroladores/10.89.105.98-$(date +%Y%m%d_%H%M).txt
python3 /home/ebossteam/UnattendedInstallation/FULLSTACK/mails/email.py 10.89.105.98 master m1 2 V8R2.l125.7 Test Now Leia brian.cobian@toshibagcs.com
node /home/ebossteam/UnattendedInstallation/FULLSTACK/mails/mail.js
rm -r /home/ebossteam/temp/10.89.105.98