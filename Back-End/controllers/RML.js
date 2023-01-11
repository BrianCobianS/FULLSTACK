
import { exec } from 'child_process';

const RML = (req,res) =>{
    const {checkcontroller} = req.body
    console.log(checkcontroller)
    console.log(checkcontroller.ip)
    exec(`python3 /home/ebossteam/RML/ojjo/Inventories/Inventory.py ${checkcontroller.ip} ${checkcontroller.usr} ${checkcontroller.pass} ${checkcontroller.type}`, (error, stdout, stderr) => {
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

            console.log(`stdout: \n${stdout}`);
            // console.log(stdout.indexOf('UNREACHABLE!'))
            if (stdout.indexOf('UNREACHABLE!') == -1){

                const versiones = []
                const current = {
                    Product: stdout.substring(stdout.indexOf("CProduct")+11,stdout.indexOf("8C")),
                    PID: stdout.substring(stdout.indexOf("CPID")+7,stdout.indexOf("1C")),
                    SP_Build: stdout.substring(stdout.indexOf("CSP/Build ")+12,stdout.indexOf("2C")),
                    Base_level: stdout.substring(stdout.indexOf("CBase level")+14,stdout.indexOf("3C")),
                    DateApplied: stdout.substring(stdout.indexOf("CDate applied")+16,stdout.indexOf("4C")),
                    PTF: stdout.substring(stdout.indexOf("CPTF")+7,stdout.indexOf("5C")),
                    Release: stdout.substring(stdout.indexOf("CRelease")+11,stdout.indexOf("7C")),
                    Emergencyfix: stdout.substring(stdout.indexOf("CEmergency Fix")+17,stdout.indexOf("9C"))
                }
                versiones.push(current)
                const maintenance = {
                    PID: "-" ,
                    SP_Build: "-" ,
                    Base_level: "-" ,
                    DateApplied: "-" ,
                    PTF: "-" ,
                    Release: "-" ,
                    Emergencyfix: "-" 
                }
        
                if(stdout.indexOf('No hay mantenimineto') == -1){
                maintenance.Product= stdout.substring(stdout.indexOf("MProduct")+11,stdout.indexOf("8M")),
                maintenance.PID = stdout.substring(stdout.indexOf("MPID")+7,stdout.indexOf("1M")),
                maintenance.SP_Build = stdout.substring(stdout.indexOf("MSP/Build ")+12,stdout.indexOf("2M")),
                maintenance.Base_level = stdout.substring(stdout.indexOf("MBase level")+14,stdout.indexOf("3M")),
                maintenance.DateApplied = stdout.substring(stdout.indexOf("MDate applied")+16,stdout.indexOf("4M")),
                maintenance.PTF = stdout.substring(stdout.indexOf("MPTF")+7,stdout.indexOf("5M")),
                maintenance.Release = stdout.substring(stdout.indexOf("MRelease")+11,stdout.indexOf("7M")),
                maintenance.Emergencyfix = stdout.substring(stdout.indexOf("MEmergency Fix")+17,stdout.indexOf("9M"))
                }

                versiones.push(maintenance)
                console.log(current)
                console.log(maintenance)
                
                res.json({versiones})
            }else{
                res.json({error:`The controller ${checkcontroller.ip} can't be reach`})
            }

            return stdout; 
        });
        
    }, 1000);

}
export default RML;