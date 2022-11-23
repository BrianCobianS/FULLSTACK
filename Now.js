import { exec } from 'child_process';
function now(Controlador){

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

}
export default now;