"use strict"
new Swiper('.image-slider',{
    breakpoints: {
        '@0.75': {
          slidesPerView: 1,
          spaceBetween: 20,
        },
        '@1.00': {
          slidesPerView: 2,
          spaceBetween: 40,
        },
        '@1.50': {
          slidesPerView: 3,
          spaceBetween: 50,
        },
    },
    navigation:{
        nextEl:'.swiper-button-next',
        prevEl:'.swiper-button-prev'
    },
    simulateTouch:false,
    
    loop:true,
    
    
});

function validateFormm() {
    let login = document.forms["registrationFormm"]["Login"].value;
    let password = document.forms["registrationFormm"]["Password"].value;

    if (login == "admin" & password == "admin" ) {
        alert("Вы авторизовались");
        return true;
    }
    alert("Неверный логин или пароль");
    return false;
}

function validateForm() {
    let surname = document.forms["registrationForm"]["Secondname"].value;
    let name = document.forms["registrationForm"]["Firstname"].value;
    let patronymic = document.forms["registrationForm"]["Patronymic"].value;
    let email = document.forms["registrationForm"]["Number_email"].value;
    let agree =document.forms["registrationForm"]["Agreement"].value;

    if (!/^[а-яА-ЯёЁ]+$/.test(surname)) {
        alert("Введите фамилию на кириллице");
        return false;
    }
    
    if (!/^[а-яА-ЯёЁ]+$/.test(name)) {
        alert("Введите имя на кириллице");
        return false;
    }
    
    if (!agree){
        if (!/^[а-яА-ЯёЁ]+$/.test(patronymic)) {
            alert("Введите отчество на кириллице");
            return false;
        }
    }
    if(!/^[0-9]+$/.test(email)){
        if (!/^\S+@\S+.+\S$/.test(email)) {
            alert("Введите корректную почту или номер телефона");
            return false;
        }
    }

    alert("Вы отправили запись на прием");
    return true;
}

function agreeForm(f) {
    if (f.Agreement.checked) f.Patronymic.disabled = 1 
    else 
    f.Patronymic.disabled = 0
    Patronymic=""
}
var today = new Date().toISOString().split('T')[0];
document.getElementsByName("date")[0].setAttribute('min', today);