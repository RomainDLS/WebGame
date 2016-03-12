var mouseX = 0;
var mouseY = 0;
var image = new Image();
var myInterval;
var objectList = [];
var canvas;
var playerId;
var mapToScreen = 1
image.src = "sprites/losange.png";


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
		// context.save(); 
		context.clearRect(0, 0, canvas.width, canvas.height);
		drawObjects();
		doSend("globalView")
	}

	function drawObjects(){
		for (i=0; i<objectList.length; i++){
			var zoom = mapToScreen;
			object = objectList[i];
			var x = object.position[0]/zoom;
			var y = object.position[1]/zoom;
			if (object.type == "rectangle"){
				context.save(); 
				context.beginPath();
				if (object.angle != 0){
					context.translate((object.position[0] + object.params[0]/2)/zoom, (object.position[1] + object.params[1]/2)/zoom);
					context.rotate(object.angle * Math.PI / 180);
					context.rect((0 - object.params[0]/2)/zoom,(0 - object.params[1]/2)/zoom,object.params[0]/zoom,object.params[1]/zoom);
				} else {
					context.rect(x,y,object.params[0]/zoom,object.params[1]/zoom);
				}
				context.restore();
			}
			if (object.type == "ellipse"){
				var r = object.params[0]/zoom;
				var wX = object.params[1]/zoom;
				var wY = object.params[2]/zoom;
				var angle = object.angle;
				context.beginPath();
				context.ellipse(x,y,r*wX,r*wY,angle * Math.PI / 180,0,2 * Math.PI);
			}
			if (object.type == "complexe"){
				context.beginPath();
				context.moveTo(object.params[0][0]/zoom,object.params[0][1]/zoom);
				for(j=1; j<object.params.length; j++){
					context.lineTo(object.params[j][0]/zoom,object.params[j][1]/zoom);
				}
				context.lineTo(object.params[0][0]/zoom,object.params[0][1]/zoom);
			}
			context.stroke();
		}
	}
}

function setMapSize(x , y){
	var tmpMapToScreen = x / canvas.width;
	if (tmpMapToScreen > y / canvas.height){
		mapToScreen = y / canvas.height;
	} else {
		mapToScreen = tmpMapToScreen;
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
