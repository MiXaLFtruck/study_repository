// Ищем элементы
const username = document.querySelector('#username');
const avatar = document.querySelector('#avatar');
const avatarButton = document.querySelector('#avatar-button');
const sb = document.querySelector('#submit-button');

let usernameValue = '';

// Добавляем в форму данные текущего пользователя
(async () => {
    const data = await getRequest(`${host}api/users/${sessionStorage.getItem('currentUserID')}`);
    username.value = data.username;
    usernameValue = username.value;
    avatar.parentElement.insertAdjacentHTML('afterbegin', `<div><img src="${data.avatar}" class="circle-image" alt="avatar" width="300px"></div>`);
})()

// // Подменяем некрасивый input на красивую кнопку
// avatarButton.addEventListener("click", function (e) {
//       avatar.click();
//   }, false);

// Функция отправки данных на сервер
const patchRequest = async function () {
    let data = new FormData();
    if (username.value != usernameValue) {
        data.append('username', username.value);
    }
    if (avatar.value) {
        data.append('avatar', avatar.files[0]);
    }
    if (data.has('username') || data.has('avatar')) {
        return await fetch(`${host}api/users/${sessionStorage.getItem('currentUserID')}/`, {
            method: 'PATCH',
            body: data,
            headers: {
            }
        })
        .then(response => {
            return response.json()
        })
        .catch(ev=>console.log(`Error: ${ev}`))
    } else {
        alert('Вы ничего не изменили');
    }
}

// Отправляем данные формы на сервер
sb.addEventListener('click', ()=> patchRequest())