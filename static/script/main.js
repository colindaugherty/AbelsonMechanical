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

var updateloc = (function(){
  var locName = $("#careers_edit"),
      locAddress = $("#edit_loc_address"),
      locEmail = $("#edit_loc_email"),
      locFax = $("#edit_loc_fax"),
      locPhone = $("#edit_loc_phone");

})();

var updatejob = (function(){

})();
