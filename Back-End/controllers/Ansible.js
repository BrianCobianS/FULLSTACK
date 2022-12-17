import { exec } from 'child_process';
function ansible(Controlador){
    exec(`sh /home/ebossteam/UnattendedInstallation/FULLSTACK/Back-End/public/Inventories/controllers/${Controlador.ip}.sh 2>&1 | tee /home/ebossteam/UnattendedInstallation/FULLSTACK/Back-End/logs/${Controlador.ip}-log-$(date +%Y%m%d_%H%M).txt`, (error, stdout, stderr) => {
        if (error) {
        console.error(`error: ${error.message}`);
        return;
        }
        if (stderr) {
        console.error(`stderr: ${stderr}`);
        return;
        }
        console.log(`stdout: \n${stdout}`);
   });
}
export default ansible;