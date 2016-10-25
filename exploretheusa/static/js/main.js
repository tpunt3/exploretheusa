var rh = rh || {};
rh.eu = rh.eu || {};

rh.eu.enableButtons = function() {
  $("#attach-img-btn").click(function() {
	rh.eu.triggerImageFileInput();
  });
  
  
  $(".trip-card .header").click(function() {
    var $header = $(this)
    var $content = $header.next();
    $content.slideToggle(250, function() {
      if ($content.is(":visible")) {
        $header.find(".edit-trip-btn").show();
      } else {
        $header.find(".edit-trip-btn").hide();
      }
    });
  });
  
  
  
  $(".trip-card .edit-trip-btn").click(function(){
	  console.log("woo");
  });
  
}

rh.eu.mainPageInit = function() {
  $("#img-input").change(function(event) {
    $("#attach-img-btn").text("Update image");
  });
}

rh.eu.triggerImageFileInput = function() {
  document.getElementById("img-input").click();
}

rh.eu.mapUpdate = function(){
//	think about removing and re-creating
}


$(document).ready(function() {
	rh.eu.enableButtons();
	rh.eu.mainPageInit();

	$('#map').usmap({
	  // The click action
	  click: function(event, data) {
	    console.log(data.name);
	    rh.eu.mapUpdate();
	  },
	
	stateSpecificStyles: {
	    'MD': {fill: 'yellow'},
	    'VA': {fill: 'teal'}
	  }
	});
});