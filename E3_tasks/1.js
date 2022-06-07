function getEvenOdd(arr){
    let calculates = {
        even: 0,
        odd: 0,
        zero: 0
    };

    for (let i of arr){
        if (typeof(i) === "number"){
            switch (i % 2){
                case 0:
                    if (i !== 0)
                        calculates['even'] += 1;
                    else
                        calculates['zero'] += 1;
                    break;
                case 1:
                    calculates['odd'] += 1;
                    break;
            }
        }
    }
    console.log(`Четных чисел ${calculates['even']}`);
    console.log(`Нечетных чисел ${calculates['odd']}`);
    console.log(`Нулевых элементов ${calculates['zero']}`);
}

const arr = [5, 67, 94, '33', 0, 12548, NaN, '+', 5487, null, 0, 79, false, 'string', 23, 48, 67];
getEvenOdd(arr);