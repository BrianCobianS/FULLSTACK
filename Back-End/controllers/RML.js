
import { exec } from 'child_process';

const RML = (req,res) =>{
    const {checkcontroller} = req.body
    console.log(checkcontroller)
    console.log(checkcontroller.ip)
    exec(`python3 /home/ebossteam/RML/ojjo/Inventories/Inventory.py ${checkcontroller.ip} ${checkcontroller.usr} ${checkcontroller.pass}`, (error, stdout, stderr) => {
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
     setTimeout(() => {

        exec(`sh /home/ebossteam/RML/ojjo/excecuteme.sh 2>&1 | tee salidadelnode.txt`, (error, stdout, stderr) => {
            if (error) {
            console.error(`error: ${error.message}`);
            res.json({msg:`The controller information is: ${error.message}`})
            return error.message;
            }
            if (stderr) {
            console.error(`stderr: ${stderr}`);
            res.json({msg:`The controller information is: ${stderr}`})
            return stderr; 
            }
            const versiones = {

            }
            
            const Current = {
                ACE3D:'-',
                EPS:'-',
                Txcpay:'-',
                TxcpayPINPAD:'-',
                ACE3DCommon:'-'
            }
            const Maintenance = {
                type: 'Maintenance',
                ACE3D:'-',
                EPS:'-',
                Txcpay:'-',
                TxcpayPINPAD:'-',
                ACE3DCommon:'-'
            }
            const Backup = {
                type: 'Backup',
                ACE3D:'-',
                EPS:'-',
                Txcpay:'-',
                TxcpayPINPAD:'-',
                ACE3DCommon:'-'
            }
            console.log(`stdout: \n${stdout}`);
            stdout.indexOf('TYPE1') != -1 ? Current.ACE3D=stdout.substring(stdout.indexOf('TYPE1')+6,stdout.indexOf('TYPE1')+16):  Current.ACE3D='None'; 
            stdout.indexOf('TYPE2') != -1 ? Maintenance.ACE3D=stdout.substring(stdout.indexOf('TYPE2')+6,stdout.indexOf('TYPE2')+16): Maintenance.ACE3D='None'; 
            stdout.indexOf('TYPE3') != -1 ? Backup.ACE3D=stdout.substring(stdout.indexOf('TYPE3')+6,stdout.indexOf('TYPE3')+16): Backup.ACE3D='None'; 
            versiones.Current=Current
            versiones.Maintenance=Maintenance
            versiones.Backup=Backup
            // console.log(versiones)
            res.json({stdout})
            return stdout; 
        });
        
    }, 5000);

}
export default RML;