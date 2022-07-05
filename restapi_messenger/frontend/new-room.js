// Ищем элементы
const form = document.getElementById("form");
const roomTitle = document.getElementById("title");
const roomUsers = document.getElementById("users");

// Заполняем значения селекта именами пользователей
(async () => {
    const requestResults = await getRequest(`${host}api/users/`);
    requestResults.forEach(obj => {
        if(obj.id == sessionStorage.getItem('currentUserID'))
            roomUsers.insertAdjacentHTML('beforeend', `<option selected="selected" value=${obj.id}>${obj.username}</option>`);
        else
            roomUsers.insertAdjacentHTML('beforeend', `<option value=${obj.id}>${obj.username}</option>`);
    })
}
)();

// Функция отправки данных формы на сервер
(function sendData() {
    // Валидация и автозаполнение полей формы



    form.addEventListener("submit", function (e) {
        e.preventDefault();

        // Извлекаем значения селектора в массив users
        let users = [];
        for (let i = 0; i < roomUsers.options.length; i++) {
            if (roomUsers.options[i].selected)
                users.push(Number(roomUsers.options[i].value))
        };

        // Формируем тело будущего запроса
        let body = `{"title": "${roomTitle.value}", "users": ${JSON.stringify(users)}`;
        if (roomUsers.options.length > 2)
            body = body + ', "is_direct": false';
        body += '}';

        postRequest(`${host}api/rooms/`, body)
            .then((response) => {
                console.log(response);
            })
            .catch((err) => console.error(err))
    });
})();