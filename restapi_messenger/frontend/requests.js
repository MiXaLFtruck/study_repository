// // GET-запрос
const getRequest = (url) => {
    const options = {
        method: 'GET',
        mode: 'cors',
        headers: { 
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Origin': 'http://127.0.0.1:8000'
        }
        }    
    return fetch(url, options)
        .then((response) => {
            return response.json();
        })
        .then((json) => { return json; })
        .catch((ev) => { alert('Ошибка запроса: ' + ev) });
}

// GET-запрос
// const getRequest = async (url) => {
//     const options = {
//         method: 'GET',
//         mode: 'cors',
//         headers: { 
//             'Content-Type': 'application/json',
//             'Accept': 'application/json',
//             'Origin': 'http://127.0.0.1:8000'
//         }
//         };  
//     let fetchedData = await fetch(url, options);
//     let fetchedDataJson = await fetchedData.json();
//     return fetchedDataJson
// }

// POST-запрос
const postRequest = (url, body) => {
    const options = {
        method: 'POST',
        mode: 'cors',
        headers: { 
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Origin': 'http://127.0.0.1:8000'
        },
        body: body
        }    
    return fetch(url, options)
        .then((response) => {
            return response.json();
        })
        // .then((json) => { return json; })
        .catch((ev) => { alert('Ошибка запроса: ' + ev) });
}
