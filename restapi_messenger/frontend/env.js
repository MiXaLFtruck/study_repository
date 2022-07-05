const host = 'http://127.0.0.1:8000/'

// Функция для получения get-параметра key из url
function getParam(key) {
    var p = window.location.search;
    p = p.match(new RegExp(key + '=([^&=]+)'));
    return p ? p[1] : false;
}