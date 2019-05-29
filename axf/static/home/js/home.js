$(function(){
    
    setTimeout(function () {
        initTopSwiper();
        initMenuSwiper();
    },100)

})


function initTopSwiper(){

    var swiper = new Swiper("#topSwiper", {
        direction: 'horizontal',
        loop: true,
        speed: 500,
        autoplay: 2000,
        pagination:".swiper-pagination",
        control: true,
    });
}


function initMenuSwiper(){

    var swiper = new Swiper("#swiperMenu", {
        slidesPerView: 3,
        paginationClickable: true,
        spaceBetween: 2,
        loop: false,
    })
}