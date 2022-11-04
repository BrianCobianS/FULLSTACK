import { exec } from 'child_process';
function ansible(Controlador){
    console.log(`ansible-playbook playbooks/os4690/Install_Controller.yml -vv  -i Inventories/import_inventory.yml -e 'level_complement=${Controlador.complemento} opc=${Controlador.opc} ASM=${Controlador.ASM} level_name=${Controlador.nivel}'`)
    exec(`ansible-playbook /public/playbooks/os4690/Install_Controller.yml -vv  -i Inventories/import_inventory.yml -e 'level_complement=${Controlador.complemento} opc=${Controlador.opc} ASM=${Controlador.ASM} level_name=${Controlador.nivel} >> salida.txt'`, (error, stdout, stderr) => {
        if (error) {
        console.error(`error: ${error.message}`);
        return;
        }
        if (stderr) {
        console.error(`stderr: ${stderr}`);
        return;
        }
        console.log(`stdout:\n${stdout}`);
    });
}
export default ansible;