ansible-playbook playbooks/os4690/Install_Controller.yml -vv  -i Inventories/import_inventory.yml -e 'level_complement=V8R1SP2.j302-20221117.173637-1 opc=1 Tcxpay=1 ASM=Accept level_name=V8R1SP2.j302 level_complementEPS=V8R1SP2.j302-20221117.173651-1 	level_complementTcxpay=V8R1SP2.j302-20221117.173701-1 Common=1 level=1.2.10--32 PinPad=1 levelPIN=1.2.7--1' 2>&1 | tee temp.txt