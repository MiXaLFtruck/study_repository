function isProp(str, obj){
    for (let prop in obj){
        if (prop === str)
            return 'true'
    }
    return 'false'
}

const person = {
    name: 'Piter',
    age: 35,
    country: 'Ireland'
}

console.log(isProp('country', person))
console.log(isProp('weight', person))