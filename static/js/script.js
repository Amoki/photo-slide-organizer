$(document).ready(function() {
  $("#tags-list li").click(function(e) {
    var cb = $(this).find(":checkbox")[0];
    //if the click wasn't from the checkbox already, toggle it
    if(e.target != cb) {
      cb.checked = !cb.checked;
    }
    $(this).toggleClass("selected", cb.checked);
    if(cb.checked) {
      $(this).addClass("checked");
      $(this).removeClass("unchecked");
    }
    else {
      $(this).addClass("unchecked");
      $(this).removeClass("checked");
    }
  });

  $("#groupes-list li").click(function(e) {
    $('.tags-groups').each(function() {
      $(this).hide();
    });
    $('#tags-' + $(this).text()).show();
  });

  // Hide groups expect first
  $('.tags-groups:gt(0)').hide();

  // Hide tags
  $('#id_description').hide();
  $('#id_description_label').hide();

  $('select#id_description option').removeAttr("selected");

  $('#tags-form').submit(function() {
    $('#tag :checked').each(function() {
      $('<input />')
        .attr('id', 'id_description')
        .attr('name', 'description')
        .attr('value', $(this).val())
        .hide()
        .appendTo('#tags-form');
    });
    return true;
  });
});
