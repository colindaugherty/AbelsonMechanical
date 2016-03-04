/* eslint-env es6 */

'use strict';

{
  const formHandler = function formHandler (e) {
    let form = $(e.target),
      username = document.getElementById("InUser").value,
      password = document.getElementById("InPass").value,
      auth = btoa(username + ":" + password);

    e.preventDefault();

    $.ajax({
      type: "POST",
      url: form.attr('action'),
      headers: {
        'Authorization': 'Basic ' + auth
      },

      success: (data) => {
        console.log(data);
        if(data.includes("login")){
        var a = document.getElementById("no");
        a.innerHTML = "Username and Password do not mach" 
        }
        else if(data.includes("admin")){
          window.location.href = data;
        }
      },

      error: (xhr, errorType, error) => {
        console.log(error)
      }
    })
  };
  const init = function init () {
    $('form').on('submit', formHandler);
  };

  $(document).on('ready', init);  
}
