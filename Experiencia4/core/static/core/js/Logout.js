$(document).ready(function (){
  $( "#logout" ).click(function() {
    var cookies_dict = [];
    var cookies_array = document.cookie.split(';');
    var csrftoken;
    cookies_array.forEach(elem => {
      var temp = elem.split('=');
      cookies_dict.push({
          key: temp[0],
          value: temp[1]
      });
    });
    cookies_dict.forEach(elem => {
      if(elem.key == 'csrftoken') {
        csrftoken = elem.value;
      }
  })
    $.ajax({
      url:'/api/v1/logout',
      type: 'POST',
      data: {csrfmiddlewaretoken: csrftoken},
      success: function(){
        location.reload();        
      } 
    })
 });
});