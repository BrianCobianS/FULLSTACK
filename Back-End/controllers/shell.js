import { exec } from 'child_process';
function shel(Controlador){
   let Tcxpay =0
   let EPS =0
   Controlador.Tcxpay != 0 ? Tcxpay = 1 : Tcxpay = 0
   Controlador.nivelEPS != 0 ? EPS = 1 : EPS = 0
   exec(`python3  /home/ebossteam/UnattendedInstallation/FULLSTACK/Back-End/public/Inventories/now.py ${Controlador.ip} ${Controlador.usr} ${Controlador.pass} ${Controlador.opc} ${Controlador.ACE3Dcomple} ${Controlador.nivel} ${Controlador.ASM} ${Controlador.fecha} ${Controlador.version} ${Controlador.email} ${EPS} ${Controlador.ACE4Dcomple} ${Tcxpay} ${Controlador.ACE6Dcomple}  ${Controlador.TCxpaycommon} ${Controlador.TCxpayPinPad} `, (error, stdout, stderr) => {
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
