allAppliances = []

class Appliance{
    constructor() {
        this.name = 'appliance';
        this.pluggedIn = false;
        this.powerConsuption = 0;
    }

    switch(){
        this.pluggedIn = !this.pluggedIn
        if (this.pluggedIn === true)
            console.log(`${this.name} включен`)
        else
            console.log(`${this.name} выключен`)
    }
}

class KettleAppliance extends Appliance{
    constructor() {
        super()
        this.color = 'white'
    }

    boil(){
        console.log('Вода закипела')
    }

    input(){
        this.name = prompt('Введите название модели чайника')
        this.color = prompt('Введите цвет чайника')
        do {
            let pc = +prompt('Введите потребляемую мощность чайника в кВт')
            if (typeof pc === 'number' && pc > 0)
                this.powerConsuption = pc
            else
                alert('Введите число')
        }
        while (this.powerConsuption === 0)
        let pluggedIn = prompt('Включить чайник? y/n')
        if (pluggedIn === 'y')
            this.switch()
    }
}

class ComputerAppliance extends Appliance{
    constructor() {
        super()
        this.processorFrequency = 0
    }

    programCompleted(){
        console.log('Программа закончила свою работу')
    }

    input(){
        this.name = prompt('Введите название модели компьютера')
        this.processorFrequency = prompt('Введите тактовую частоту процессора')
        do {
            let pc = +prompt('Введите потребляемую мощность компьютера в кВт')
            if (typeof pc === 'number' && pc > 0)
                this.powerConsuption = pc
            else
                alert('Введите число')
        }
        while (this.powerConsuption === 0)
        let pluggedIn = prompt('Включить компьютер? y/n')
        if (pluggedIn === 'y')
            this.switch()
    }
}

function powerConsumptionTotal(appliancesArr){
    let pcTotal = 0
    appliancesArr.forEach(function (item, i, arr){
        if (item.pluggedIn)
            pcTotal += item.powerConsuption
    })
    return pcTotal
}

let kettlesNum = 0
while (true){
    let kettlesNumString = prompt('Сколько у нас будет чайников? Введите число')
    if (Number.isInteger(+kettlesNumString)){
        kettlesNum = +kettlesNumString
        break
    }
}

for (let i = 0; i < kettlesNum; i++){
    const kettle = new KettleAppliance()
    kettle.input()
    allAppliances.push(kettle)
}

let computersNum = 0
while (true){
    let computersNumString = prompt('Сколько у нас будет компьютеров? Введите число')
    if (Number.isInteger(+computersNumString)){
        computersNum = +computersNumString
        break
    }
}

for (let i = 0; i < computersNum; i++){
    const computer = new ComputerAppliance()
    computer.input()
    allAppliances.push(computer)
}

console.log(`Общая потребляемая мощность всех включенных электроприборов составляет ${powerConsumptionTotal(allAppliances)} кВт`)