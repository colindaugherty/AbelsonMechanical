var select, div, newJobName, newJobLoc, newJobDesc, newJobNameValue, newJobLocValue, newJobDescValue, newJob;

var animationControler = (function(){
  select = document.getElementById('careers_edit');

  select.addEventListener("change", function(e){
  div = document.getElementById('edit_div');
    div.classList.add('fadein');
  });
})();

var newCareersPost = (function(){
  newJobName = document.getElementById('new_job_name');
  newJobLoc = document.getElementById('new_careers_loc');
  newJobDesc = document.getElementById('new_job_desiption');

  newJobNameValue = newJobName.value;
  newJobLocValue = newJobLoc.value;
  newJobDescValue = newJobDesc.value;

  newJob = [newJobNameValue, newJobLocValue, newJobDesValue];

  function PostRequest(){

      e.preventDefault();
      fetch(newJob, {
        method: "POST",
        body: data
      }).then(fetchHandler).then(responseHandler);
    }

    function fetchHandler(r) {
      return r.json();
    }

    function responseHandler(r) {
        window.alert("It worked!");
    }

})();
