const arr = [5, 67, 94, '33', 0, 12548, NaN, '+', 5487, null, 0, 79, false, 'string', 23, 48, 67];
let even = 0;
let odd = 0;
let zero = 0;

for (let i of arr){
    if (typeof(i) === "number"){
        switch (i % 2){
            case 0:
                if (i !== 0)
                    even += 1;
                else
                    zero += 1;
                break;
            case 1:
                odd += 1;
                break;
        }
    }
}

// for (let i = 0; i < arr.length; ++i){
//     if (typeof(arr[i]) === "number"){
//         switch (arr[i] % 2){
//             case 0:
//                 if (arr[i] !== 0)
//                     even += 1;
//                 else
//                     zero += 1;
//                 break;
//             case 1:
//                 odd += 1;
//                 break;
//         }
//     }
// }

console.log(`Четных чисел ${even}`);
console.log(`Нечетных чисел ${odd}`);
console.log(`Нулевых элементов ${zero}`);