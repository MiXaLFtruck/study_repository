const usersBlock = document.querySelector('#users_block');

// async/await функция, которая добавляет на страницу ссылки на юзеров
const fillBlock = async () => {
    const requestResult = await getRequest(`${host}api/users/`);
    requestResult.forEach((user) => {
        usersBlock.insertAdjacentHTML('beforeend', `<h4><a href="messenger.html?user=${user.id}">${user.username}</a></h4>`)
    })

}

fillBlock()