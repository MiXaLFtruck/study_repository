let input = prompt('Введите число');
let num = +input

if (num === num){
    if (num % 2 === 0)
        console.log('Вы ввели четное число')
    else
        console.log('Вы ввели нечетное число')
}else{
    console.log('Упс, кажется, вы ошиблись')
}