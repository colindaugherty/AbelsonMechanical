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

  var newJobNameValue = newJobName.value,
      newJobLocValue = newJobLoc.value,
      newJobDesValue = newJobDes.value;

  var newJob = [newJobNameValue, newJobLocValue, newJobDesValue];

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

var updateloc = (function(){
  var locName = $("#careers_edit"),
      locAddress = $("#edit_loc_address"),
      locEmail = $("#edit_loc_email"),
      locFax = $("#edit_loc_fax"),
      locPhone = $("#edit_loc_phone");

})();

var updatejob = (function(){

})();
