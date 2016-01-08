function ready(fn) {
  if (document.readyState != 'loading'){
    fn();
  } else {
    document.addEventListener('DOMContentLoaded', fn);
  }
}

var ABELSONMECHANICAL = (function(){

  function animationController() {
    select = $('#careers_edit');

    select.on("change", function(e){
    div = $('#edit_div');
      div.addClass('fadein');
    });
  }

  function careerEdit(){
    var data = new FormData(form);
    $.ajax({type: 'POST',url: '/my/url',data: data});
  }

  function careerNew(){
    var data = new FormData(form);
    $.ajax({type: 'POST',url: '/my/url',data: data});
  }

  function LocEdit(){
    var data = new FormData(form);
    $.ajax({type: 'POST',url: '/my/url',data: data});
  }

  function init() {
      animationController();
  }

  return {
    init: init
  };
})();

ready(ABELSONMECHANICAL.init());
