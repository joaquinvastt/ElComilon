const btn = document.querySelector('#menu-btn');
const menu = document.querySelector('#sidemenu');

btn.addEventListener('click', function(){
    document.getElementById('sidemenu').classList.toggle('menu-expanded');
    
    document.getElementById('sidemenu').classList.toggle('menu-collapsed');
});