// Сохраняем id текущего пользователя
window.sessionStorage.setItem('currentUserID', getParam('user'));

//Ищем элементы
const pList = document.querySelector('#plist');
const chatList = document.querySelector('.chat-list');

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
        `<li class="clearfix">
            <div class="about">
                <div class="name">${obj.title}</div>
            </div>
        </li>`)        
    })
})();