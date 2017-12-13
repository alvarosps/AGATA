// Listen for click on toggle checkbox
	$('#select-all').click(function(event) {   
	    if(this.checked) {
	        // Iterate each checkbox
	        $(':checkbox').each(function() {
	            this.checked = true;                        
	        });
	    }
	});
	$('#select_all').click(function(event) {
		  if(this.checked) {
		      // Iterate each checkbox
		      $(':checkbox').each(function() {
		          this.checked = true;
		      });
		  }
		  else {
		    $(':checkbox').each(function() {
		          this.checked = false;
		      });
		  }
		});