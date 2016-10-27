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
  
  $(".edit-trip-btn").click(function() {
	     var entityKey = $(this).find(".entity-key").html();
	     var state = $(this).find(".state").html();
	     var city = $(this).find(".city").html();
	     var description = $(this).find(".description").html();
	     var startDate = $(this).find(".start-date").html();
	     var endDate = $(this).find(".end-date").html();
	     
	     if($(this).prev().children('div').children(".trip-image").length){
	    	 $("#insert-trip-modal #attach-img-btn").text("Update image")
	     }else{
	    	 $("#insert-trip-modal #attach-img-btn").text("Add image")
	     }

	     $("#insert-trip-modal input[name=trip_entity_key]").val(entityKey);
	     $("#delete-trip-modal input[name=entity_key_for_delete]").val(entityKey);

	     $("#insert-trip-modal .modal-title").html("Update Trip!");
	     $("#insert-trip-modal #state-input").val(state);
	     $("#insert-trip-modal #city-input").val(city);
	     $("#insert-trip-modal #arrival-date").val(startDate);
	     $("#insert-trip-modal #departure-date").val(endDate);
	     $("#insert-trip-modal #description").val(description);
	     $("#insert-trip-modal .delete-trip-btn").show();
	     $("#insert-trip-modal button[type=submit]").html("Update");
	     $("#insert-trip-modal").modal("show");
	  });
  
  $("#add-trip").click(function(){
	 rh.eu.resetAddTripModal(); 
  });

  $(".cancel-delete-trip-button").click(function() {
	 $("#delete-trip-modal").modal('toggle');
  });
  
}

rh.eu.resetAddTripModal = function() {
	$("#insert-trip-modal .modal-title").html("Add trip!");
	$("#insert-trip-modal #state-input").val("");
    $("#insert-trip-modal #city-input").val("");
    $("#insert-trip-modal #arrival-date").val("");
    $("#insert-trip-modal #departure-date").val("");
    $("#insert-trip-modal #description").val("");
    $("#insert-trip-modal .delete-trip-btn").hide();
    $("#insert-trip-modal button[type=submit]").html("Add");
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