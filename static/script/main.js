var animationControler = (function(){
  var select = document.getElementById('careers_edit');

  select.addEventListener("change", function(e){
    var div = document.getElementById('edit_div');
    div.classList.add('fadein');
  });
})();
