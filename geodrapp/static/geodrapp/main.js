const hamburger = document.querySelector('.header .nav-bar .nav-list .hamburger');
const mobile_menu = document.querySelector('.header .nav-bar .nav-list ul');
const menu_item = document.querySelectorAll('.header .nav-list ul li a');


// Toogle

const menuCenter = document.querySelector('#mainMenuCenter');
const closebars = document.querySelector('.close');
const opebBars = document.querySelector('#open')

function humbergh() {
    console.log('clicked')
    opebBars.style.display = block;
}

opebBars.addEventListener('click', ()=>{
    console.log('clicked')
    // hamburger.classList.toggle('active');
    // mobile_menu.classList.toggle('active')
})

opebBars.addEventListener('click', ()=>{
    console.log('clicked')
    // hamburger.classList.toggle('active');
    // mobile_menu.classList.toggle('active')
})












const header = document.querySelector('header');
const sectionOne = document.querySelector('#home-intro');
const siteHeader = document.querySelector('.site-header')

const sectionOneObserver = new IntersectionObserver
    (function(
        entries,
    sectionOneObserver
        ) {
    entries.forEach(entry => {
     if (!entry.isIntersecting) {
     header.classList.add('siteHeader');
     } else {
     header.classList.remove('siteHeader')
     }
    });
    }
    sectionOneOptions);

    sectionOneObserver.observe(sectionOne);


const nav = document.querySelector('.navbar');
const nav_link = document.querySelectorAll('.navbar .navbar-container ul li a');


hamburger.addEventListener('click', ()=>{
    hamburger.classList.toggle('active');
    mobile_menu.classList.toggle('active')
})

document.addEventListener('scroll', ()=>{
    var scroll_position = window.scrollY;
    if(scroll_position > 70){
       navbar.style.backgroundColor = '#29323c';
    } else{
        nav.style.backgroundColor = 'red';
    }
});

menu_item.forEach((item) => {
    item.addEventListener('click', ()=>{
        hamburger.classList.toggle('active');
        mobile_menu.classList.toggle('active');
    })
})

// '#29323c'

window.addEventListener('scroll', event =>{
    let fromTop = window.scrollY;

   nav_link.forEach(link => {
    let section = document.querySelector(link.hash);

    if (section.offsetTop <= fromTop + 70 && section.offsetTop + section.offsetHeight > fromTop + 70){
        link.style.color = 'crimson';
        link.style.borderBottom = '2px solid crimson';
        console.log(fromTop +30)
    } else {
        link.style.color = 'white';
        link.style.borderBottom = 'none';
    }
   })
});

document.getElementById('login').addEventListener('click',  ()=>{
    document.querySelector('.login-modal').style.display='flex';
    });

    document.querySelector('.close').addEventListener('click', ()=> {
        document.querySelector('.login-modal').style.display='none';

    });