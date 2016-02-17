var mouseX = 0;
var mouseY = 0;

var image = new Image();
var myInterval;
image.src = "sprites/losange.png";

var objectList = []

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
		drawObjects();
		sendAngle();
	}

	function drawObjects(){
		for (i=0; i<objectList.length; i++){
			object = objectList[i];
			var x = object.position[0];
			var y = object.position[1];
			if (object.type == "rectangle"){
				context.rect(x,y,object.params[0],object.params[1]);
				context.stroke();
			}
			if (object.type == "ellipse"){
				var r = object.params[0];
				var wX = object.params[1];
				var wY = object.params[2];
				var angle = object.angle;
				context.beginPath();
				context.ellipse(x,y,r*wX,r*wY,angle * Math.PI / 180,0,2 * Math.PI);
				context.stroke();
			}
			if (object.type == "complexe"){

			}
		}
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
