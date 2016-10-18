var rh = rh || {};
rh.eu = rh.eu || {};

rh.eu.enableButtons = function() {
	
	
}

rh.eu.mapUpdate = function(){
//	think about removing and re-creating
}


$(document).ready(function() {
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