var rh = rh || {};
rh.eu = rh.eu || {};

rh.eu.enableButtons = function() {
  $("#attach-img-btn").click(function() {
	rh.eu.triggerImageFileInput();
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