var select, div, newJobName, newJobLoc, newJobDesc, newJobNameValue, newJobLocValue, newJobDescValue, newJob;

var animationControler = (function(){
  select = $('#careers_edit');

  select.on("change", function(e){
  div = $('#edit_div');
    div.addClass('fadein');
  });
})();

var newCareersPost = (function(){
  newJobName = $('#new_job_name');
  newJobLoc = $('#new_careers_loc');
  newJobDesc = $('#new_job_desiption');
  
  newJobNameValue = newJobName.value;
  newJobLocValue = newJobLoc.value;
  newJobDescValue = newJobDesc.value;

  newJob = [newJobNameValue, newJobLocValue, newJobDescValue];

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
