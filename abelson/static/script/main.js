function ready(fn) {
  if (document.readyState != 'loading'){
    fn();
  } else {
    document.addEventListener('DOMContentLoaded', fn);
  }
}

var ABELSONMECHANICAL = (function(){
    var select, div;
    var AdminForm = document.getElementById('adminform'),
        careerNewForm = document.getElementById('careerNewForm');
        //careerEditForm = document.getElementById('careerNewForm');

  //  var Evt = new EventEmitter2();

  function animationController() {
    select = $('#loc_edit');

    select.on("change", function(e){
      div = $('#edit_div');
      div.addClass('fadein');
    });
  }


    function careerEdit(){
      var data = new FormData(form);
      $.ajax({type: 'POST',url: '/admin/careers/update',data: data});
    }

    function careerNew(){
      var data = new FormData(form);
      if (data.name !== null && data.description !== null){
        $.ajax({type: 'POST',url: '/admin/careers/add',data: data});
        return;
      }
      alert("Please enter a name and/or description.");
      return;
    }

    function locEdit(){
      var data = new FormData(form);
      $.ajax({type: 'POST',url: '/admin/loc',data: data});
    }

  function init() {
      animationController();
      AdminForm.addEventListener("submit", locEdit);
      careerNewForm.addEventListener("submit", careerNew);
  }

  return {
    init: init
  };
})();

ready(ABELSONMECHANICAL.init());
