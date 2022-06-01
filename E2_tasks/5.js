let arr = [11, true, '333', 556.24, 'hello', null];

console.log(`Длина массива ${arr.length} элементов`);

let result = arr.map(function(item, index, array) {
    console.log(item)
});