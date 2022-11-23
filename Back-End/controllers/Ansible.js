import { exec } from 'child_process';
function ansible(Controlador){
    exec(`sh /home/ebossteam/UnattendedInstallation/FULLSTACK/Back-End/public/Inventories/controllers/${Controlador.ip}.sh`, (error, stdout, stderr) => {
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