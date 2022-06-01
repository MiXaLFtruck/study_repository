let input = prompt('Введите строку любых символов');

const arr = input.split('');
const arrL = arr.length;
let i = 1;
for (; i < arrL; ++i){
    if (arr[0] !== arr[i]){
        console.log('false');
        break;
    }
}
if (i === arrL){
    console.log('true');
}