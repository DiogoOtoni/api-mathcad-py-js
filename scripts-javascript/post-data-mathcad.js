import { PythonShell } from "python-shell";

try{
    PythonShell.run('./scripts-python/post-data-mathcad.py', null).then(results => {
        
        const dataResult = JSON.stringify(results);
        
        console.log("CONSOLE LOG DA AWAIT PYTHON",results);
        console.log("CONSOLE LOG DA DATARESULT JSON PARSE", dataResult);
    })
}catch(error){
    console.error(error);
}

