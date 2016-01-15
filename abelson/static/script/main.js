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
        $.ajax({type: 'POST',url: '/admin/careers/add',data: data});
        return;
    }

    function locEdit(){
      var data = new FormData(form);
      $.ajax({type: 'POST',url: '/admin/loc',data: data});
      return;
    }

    function get_job(){
      var jobs;
      jobs = $.ajax({type: 'GET', utl: '/job/get'});
      return jobs;
    }

    function get_loc(){
      var loc;
      loc = $.ajax({type: 'GET', url: '/loc/get'});
      return loc;
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
