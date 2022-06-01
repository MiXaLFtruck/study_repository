let input = prompt('Введите переменную X');

if (+input === +input && input != '')
    console.log('X - число')
else if(input === 'true' || input === 'false')
    console.log('X - булевый тип')
else if(Boolean(input))
    console.log('X - строка')
else
    console.log('Тип X не определен')