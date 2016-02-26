$(function() {
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


  $('#id_description').hide();
  $('#id_description_label').hide();

  $('#add-photo').submit(function() {
    $('#tag :checked').each(function() {
      $('<input />')
        .attr('id', 'id_description')
        .attr('name', 'description')
        .attr('value', $(this).val())
        .hide()
        .appendTo('#add-photo');
    });
    return true;
  });
});
