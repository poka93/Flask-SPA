$(document).ready(function() {
  console.log("ready!");

  $('#try-again').hide();

  // on form submission ...
  $('form').on('submit', function() {

    console.log("the form has beeen submitted");

    // grab values
    valueOne = $('select[name="variables"]').val();
    console.log(valueOne)

    $.ajax({
      type: "POST",
      url: "/",
      data : { 'column': valueOne },
      success: function(results) {
        if (1 > 0) {
          $('#try-again').show();
          console.log(results.items);
          $('#results').html('<h1>GOOOD</h1')
          // $('input').val('')
        } else {
          $('#results').html('Something went terribly wrong! Please try again.')
        }
      },
      error: function(error) {
        console.log(error)
      }
    });

  });

  $('#try-again').on('click', function(){
    $('input').val('').show();
    $('#try-again').hide();
    $('#results').html('');
  });

});
