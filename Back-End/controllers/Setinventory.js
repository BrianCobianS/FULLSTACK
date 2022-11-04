import { exec } from 'child_process';
function inventory(parametros){
    console.log(`python ${parametros.ip} ${parametros.usr} ${parametros.pass}`)
    exec(`python public/Inventories/inventory.py ${parametros.ip} ${parametros.usr} ${parametros.pass} ${parametros.opc}`, (error, stdout, stderr) => {
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
    console.log(`echo ${parametros.opc}`)
}
export default inventory;