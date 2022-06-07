function outer(x){
    return function (y = 5){
        return y + x
    }
}

result = outer(7)
console.log(result())