var mouseX = 0;
var mouseY = 0;

var image = new Image();
var myInterval;
image.src = "sprites/losange.png";

//window.onload = function() {
function LaunchGame(){
	var canvas = document.getElementById("canvas");
    var context = canvas.getContext("2d");
	
	canvas.addEventListener('mousemove', function(evt) {
		var position = getMousePos(canvas, evt);
		mouseX = position.x;
		mouseY = position.y;
	}, false);
	
	myInterval = setInterval(animate, 500/50);
	
	function animate(){
		var angle = getAngle();
		context.save(); 
		context.clearRect(0, 0, canvas.width, canvas.height);
		context.translate(canvas.width/2, canvas.height/2);
		context.rotate(angle);
		context.drawImage(image, 0 - 60/2, 0 - 100/2, 60, 100);
		context.restore();
	}
}

function StopGame(){
	clearInterval(myInterval);
}

function getAngle() {
	var mouseXFromCenter = 0;
	var mouseYFromCenter = 0;
	var angle = 0;
	if(mouseY < canvas.height/2){ 
		mouseYFromCenter = canvas.height/2 - mouseY;
	}
	else{ 
		mouseYFromCenter = - mouseY + canvas.height/2;
	}
	if(mouseX > canvas.width/2){ 
		mouseXFromCenter = mouseX - canvas.width/2;
		angle = Math.atan(mouseXFromCenter/mouseYFromCenter);
		if (angle < 0){
			angle += Math.PI;
		}
	}
	else{ 
		mouseXFromCenter = mouseX - canvas.width/2;
		angle = Math.atan(mouseXFromCenter/mouseYFromCenter);
		if(angle >= 0){
			angle += Math.PI;
		}
		else{
			angle += 2*Math.PI;
		}
	}
	
	return angle;
}

function getMousePos(canvas, evt) {
    var rect = canvas.getBoundingClientRect();
    return {
      x: evt.clientX - rect.left,
      y: evt.clientY - rect.top
    };
  }
