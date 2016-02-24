var mouseX = 0;
var mouseY = 0;

var image = new Image();
var myInterval;
image.src = "sprites/losange.png";

var objectList = [];
var canvas;

//window.onload = function() {
function LaunchGame(){
	canvas = document.getElementById("canvas");
    var context = canvas.getContext("2d");

	canvas.addEventListener('mousemove', function(evt) {
		var position = getMousePos(canvas, evt);
		mouseX = position.x;
		mouseY = position.y;
	}, false);

	myInterval = setInterval(animate, 500/50);
	
	function animate(){
		context.save(); 
		context.clearRect(0, 0, canvas.width, canvas.height);
		drawObjects();
		doSend("globalView")
	}

	function drawObjects(){
		for (i=0; i<objectList.length; i++){
			object = objectList[i];
			if (object.type == "rectangle"){
				context.save(); 
				if (object.angle != 0){
					context.translate(object.position[0] + object.params[0]/2, object.position[1] + object.params[1]/2);
					context.rotate(object.angle * Math.PI / 180);
					context.rect(0 - object.params[0]/2,0 - object.params[1]/2,object.params[0],object.params[1]);
				} else {
					context.rect(object.position[0],object.position[1],object.params[0],object.params[1]);
				}
				context.restore();
				context.stroke();
			}
			if (object.type == "ellipse"){
				var r = object.params[0];
				var wX = object.params[1];
				var wY = object.params[2];
				var angle = object.angle;
				context.beginPath();
				context.ellipse(object.position[0],object.position[1],r*wX,r*wY,angle * Math.PI / 180,0,2 * Math.PI);
				context.stroke();
			}
			if (object.type == "complexe"){
				context.beginPath();
				context.moveTo(object.params[0][0],object.params[0][1]);
				for(i=1; i<object.params.length; i++){
					context.lineTo(object.params[i][0],object.params[i][1]);
				}
				context.lineTo(object.params[0][0],object.params[0][1]);
			}
		}
	}
}

function setMapSize(x , y){
	canvas.width = x;
	canvas.height = y;
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
