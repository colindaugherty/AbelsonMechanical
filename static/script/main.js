var animationControler = (function(){
  var select = document.getElementById('careers_edit');

  select.addEventListener("change", function(e){
    var div = document.getElementById('edit_div');
    div.classList.add('fadein');
  });
})();

var newCareersPost = (function(){
  var newJobName = document.getElementById('new_job_name'),
      newJobLoc = document.getElementById('new_careers_loc'),
      newJobDes = document.getElementById('new_job_desiption');

  
})();
