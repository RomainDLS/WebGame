var mouseX = 0;
var mouseY = 0;

var image = new Image();
var myInterval;
var objectList = [];
var offsetY = 0;
var offsetX = 0;
var playerId;
var mapSize = {x:0, y:0};
var packet = {};
packet.isClicked = false;

image.src = "sprites/losange.png";

//window.onload = function() {
function LaunchGame(){
	var canvas = document.getElementById("canvas");
    var context = canvas.getContext("2d");
    var playerPosition = {x:canvas.width, y:canvas.height}
	canvas.addEventListener('mousemove', function(evt) {
		var position = getMousePos(canvas, evt);
		mouseX = position.x;
		mouseY = position.y;
	}, false);
	canvas.addEventListener('click',function(evt){
		packet.isClicked = true;
	},false);


	myInterval = setInterval(step, 10);
	
	function step(){
		if (typeof(objectList[1]) !== 'undefined'){
			if (objectList[1].statut == 'alive'){
				animate();
			} else if (objectList[1].statut == 'dead') {
				context.clearRect(0, 0, canvas.width, canvas.height);
				StopGame();
			}
		} else {
			animate();
		}
	}

	function animate(){
		var angle = getAngle();
		context.save(); 
		context.clearRect(0, 0, canvas.width, canvas.height);
		context.translate(canvas.width/2, canvas.height/2);
		context.rotate(angle);
		context.drawImage(image, 0 - 60/2, 0 - 100/2, 60, 100);
		context.restore();
		drawObjects();
		drawMapBound();
		packet.angle = angle*180/Math.PI;
		sendPacket();
	}

	function drawMapBound(){
		if(playerPosition.x <= canvas.width/2){
			context.fillStyle="#D1CACA";
			context.fillRect(0,0,canvas.width/2 - playerPosition.x,canvas.height);
		}
		if(playerPosition.y <= canvas.height/2){
			context.fillStyle="#D1CACA";
			context.fillRect(0,0,canvas.width,canvas.height/2 - playerPosition.y)
		}
		if(mapSize != 0 && (mapSize.x - playerPosition) <= canvas.width/2){
			context.fillStyle="#D1CACA";
			context.fillRect(canvas.width/2 + (mapSize.x - playerPosition),0,canvas.width/2,canvas.height)
		}
		if(mapSize != 0 && (mapSize.x - playerPosition) <= canvas.width/2){
			context.fillStyle="#D1CACA";
			context.fillRect(0,canvas.height/2 + (mapSize.x - playerPosition),canvas.width,canvas.height/2)
		}
	}

	function drawObjects(){
		playerPosition.x = objectList[0].positionX
		playerPosition.y = objectList[0].positionY
		for (i=1; i<objectList.length; i++){
			object = objectList[i];
			var x = object.position[0];
			var y = object.position[1];
			if (object.type == "rectangle"){
				context.save(); 
				context.beginPath();
				if (object.angle != 0){
					context.translate(object.position[0] + object.params[0]/2, object.position[1] + object.params[1]/2);
					context.rotate(object.angle * Math.PI / 180);
					context.rect(0 - object.params[0]/2,0 - object.params[1]/2,object.params[0],object.params[1]);
				} else {
					context.rect(object.position[0],object.position[1],object.params[0],object.params[1]);
				}
				context.restore();
			}
			if (object.type == "ellipse"){
				var r = object.params[0];
				var wX = object.params[1];
				var wY = object.params[2];
				var angle = object.angle;
				context.beginPath();
				context.ellipse(x,y,r*wX,r*wY,angle * Math.PI / 180,0,2 * Math.PI);
			}
			if (object.type == "complexe"){
				context.beginPath();
				context.moveTo(object.params[0][0],object.params[0][1]);
				for(j=1; j<object.params.length; j++){
					context.lineTo(object.params[j][0],object.params[j][1]);
				}
				context.lineTo(object.params[0][0],object.params[0][1]);
			}
			context.stroke();
		}
	}
}

function StopGame(){
	clearInterval(myInterval);
	doDisconnect();
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
