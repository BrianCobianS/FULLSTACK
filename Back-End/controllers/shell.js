import { exec } from 'child_process';
function shel(Controlador){
   exec(`python3  /home/ebossteam/UnattendedInstallation/FULLSTACK/Back-End/public/Inventories/now.py ${Controlador.ip} ${Controlador.usr} ${Controlador.pass} ${Controlador.opc} ${Controlador.complemento} ${Controlador.nivel} ${Controlador.ASM} ${Controlador.fecha} ${Controlador.version} ${Controlador.email}`, (error, stdout, stderr) => {
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
   exec(`echo "sh /home/ebossteam/UnattendedInstallation/FULLSTACK/Back-End/public/Inventories/controllers/${Controlador.ip}.sh"| at -t ${Controlador.fecha}`, (error, stdout, stderr) => {
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
export default shel;
