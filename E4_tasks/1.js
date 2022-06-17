function getOwnProp(obj){
    for (let prop in obj){
        if (obj.hasOwnProperty(prop)){
            console.log(`${prop}: ${obj[prop]}`)
            debugger
        }
    }
}

const parentObj = {
    prop1: 1
}

const childObj = Object.create(parentObj)
childObj.prop2 = 2

getOwnProp(childObj)