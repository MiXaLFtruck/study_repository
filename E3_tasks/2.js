function isSimpleNum(x){
    if(x > 3 && x < 1001){
        for(let i = 2; i <= Math.sqrt(x); ++i){
            if (x % i === 0){
                return `Число ${x} - непростое`
            }
        }
        return `Число ${x} - простое`
    }
    else if(x === 0 || x === 1)
        return `Числа 0 и 1 не могут считаться простыми`
    else if(x === 2 || x === 3)
        return `Число ${x} - простое`
    else
        return 'Вы ввели неверное число'
}

num = prompt('Введите целое число от 0 до 1000')
console.log(isSimpleNum(+num))