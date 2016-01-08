function ready(fn) {
  if (document.readyState != 'loading'){
    fn();
  } else {
    document.addEventListener('DOMContentLoaded', fn);
  }
}

var ABELSONMECHANICAL = (function(){
    var select, div;

  function animationController() {
    select = $('#loc_edit');

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

    function locEdit(){
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
