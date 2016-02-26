/* eslint-env es6 */

{
  'use strict';

  const ABELSON = (function() {
    let select, div;

    const toggleClass = function toggleClass (classname, el) {
      $(el).toggleClass(classname);
    };

    const animationController = function animationController (e) {
      let t = e.target;

      e.preventDefault();

      if ($(t.options[t.selectedIndex].value).hasClass(e.data)) {
        $("form").forEach((x) => {
          toggleClass(e.data, x);
        });
      }
    };

    const menuChanger1 = function menuChanger1 () {
      toggleClass('hidden', '#menu1');
      toggleClass('hidden', '#menu2');
    }

    const deleat1 = function deleat1 (e) {
      console.log("hi");
      e.target.src="/static/images/deletehighlighted.png";
    }

    const deleat2 = function deleat2 (e) {
      console.log(e.target);
      e.target.src="/static/images/delete.png";
    }

    const init = function init () {
      $("body").on("change", "#loc_edit", 'hidden', animationController);
      $("#lines").on("click", menuChanger1);
      $("#menu2pic").on("click", menuChanger1);
      $(".DeleatA").on("mouseenter", deleat1);
      $(".DeleatA").on("mouseleave", deleat2);
    };

    return {
      init: init
    };

  }());

  $(document).on('ready', function () { ABELSON.init(); });
}

