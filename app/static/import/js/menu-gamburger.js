var item = document.querySelector('.helpMenu');

var box = document.querySelector('.buttonBlockFirst');
var boxStyle = box.style;

// var vvv = document.querySelector('.buttonBlockFirst');

var blockInfo = document.querySelector('.blockInfo');
var blockInfoStyle = blockInfo.style;

var menudrop = document.querySelector('.menu-drop-first');
var menudropStyle = menudrop.style;

item.addEventListener('click', function(){
    this.classList.toggle('activeHelpMenu');

    menudrop.classList.toggle('menu-drop-first-active');
});



item.addEventListener('mouseover', function(){
  blockInfoStyle.transform = "translateX(0px)";
});

item.addEventListener('mouseout', function(){


  var result = menudrop.getAttribute('class');
  var massivResult = result.split(' ');
  console.log(massivResult);

  if (massivResult.indexOf('menu-drop-first-active') == -1){
    blockInfoStyle.transform = "translateX(-400px)";
  } else blockInfoStyle.transform = "translateX(0px)";


});


item.addEventListener('click', function(){
  blockInfoStyle.opacity = "1";
});

$(function(){
  $(document).mouseup(function (e){ // событие клика по веб-документу
    var div = $("#blockNav"); // тут указываем ID элемента
    if (!div.is(e.target) // если клик был не по нашему блоку
        && div.has(e.target).length === 0) { // и не по его дочерним элементам
      $('.helpMenu').removeClass('activeHelpMenu');
      blockInfoStyle.transform = "translateX(-400px)";
      menudrop.classList.remove('menu-drop-first-active');
    }
  });
});