first = prompt('Введите первое число')
last = prompt('Введите второе число')

let intervalID = setInterval(function (){
    console.log(first)
    if (first == last){
        clearInterval(intervalID)
    }
    first++
}, 1000)