// Сохраняем id текущего пользователя
window.sessionStorage.setItem('currentUserID', getParam('user'));
// "подчищаем" от предыдущего сеанса
window.sessionStorage.removeItem('currentRoomID')

//Ищем элементы
const pList = document.querySelector('#plist');
const chatList = document.querySelector('.chat-list');
const btns = document.querySelectorAll('.btn-block');
const btnEdit = document.querySelector('#btn-edit');
const btnDel = document.querySelector('#btn-del');

// Рендерим данные текущего пользователя
(async () => {
    const data = await getRequest(`${host}api/users/${sessionStorage.getItem('currentUserID')}`);
    pList.insertAdjacentHTML('afterbegin', 
    `<div style="margin-bottom: 18px;">
        <a href="#" data-toggle="modal" data-target="#view_info">
            <img src="${data.avatar}" alt="avatar">
        </a>
        <div class="chat-about">
            <h6 class="m-b-0" style="margin-bottom: 0px;">${data.username}</h6>
            <small><a href="profile.html?user=${data.id}">Мой профиль</a></small>
        </div>
    </div>`);
})();

// Рендерим все комнаты текущего пользователя
(async () => {
    const data = await getRequest(`${host}api/users/${sessionStorage.getItem('currentUserID')}/rooms/`);
    data.forEach(obj => {
        chatList.insertAdjacentHTML('beforeend', 
        `<li id="chat" class="clearfix">
            <div class="about">
                <div class="name">${obj.title}</div>
            </div>
        </li>`);
        sessionStorage.setItem(obj.title, obj.id);
    })
})();

// Вешаем обработчики клика на перечень комнат
chatList.onclick = function(event) {
    let li = event.target.closest('li'); // где был клик?  
    if (!li)
        return;
    // очищаем подсветку со всех комнат
    const chats = document.querySelectorAll('#chat');
    chats.forEach(obj => {
        obj.classList.remove('selected')
    });
    // подсвечиваем кликнутую комнату
    li.classList.add('selected');
    // добавляем кнопки Редактировать и Удалить
    if (sessionStorage.getItem('currentRoomID') == null) {
        btns.forEach(obj => {
            obj.classList.remove('invisible');
        });
    }
    // сохраняем "на всякий" id выбранной комнаты
    sessionStorage.setItem('currentRoomID', sessionStorage.getItem(li.innerText));
  };

  // Удаление комнаты
  btnDel.addEventListener('click', () => {
    delRequest(`${host}api/rooms/${sessionStorage.getItem('currentRoomID')}/`)
        .then((response) => {
            console.log(response);
        })
        .then(() => {
            location.reload();
        })    
  })