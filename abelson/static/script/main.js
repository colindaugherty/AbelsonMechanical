function ready(fn) {
  if (document.readyState != 'loading') {
    fn();
  } else {
    document.addEventListener('DOMContentLoaded', fn);
  }
}

var ABELSONMECHANICAL = (function() {
  var select, div;
  //var AdminForm = document.getElementById('adminform'),
  //careerNewForm = document.getElementById('careerNewForm');
  //careerEditForm = document.getElementById('careerNewForm');

  //  var Evt = new EventEmitter2();

  function animationController() {
    select = $('#loc_edit');

    select.on("change", function(e) {
      div = $('#edit_div');
      div.addClass('fadein');
    });
  }


  

  return {
    init: init
  };
})();

$(document).on('ready', function () { ABELSONMECHANICAL.init(); });
