let cars = new Map([
    ["Ferrari", "red"],
    ["Mercedes", "black"],
    ["Porsche", "blue"]
]);

for (let car of cars.entries()){
    console.log(`Ключ - ${car[0]}, значение - ${car[1]}`)
}