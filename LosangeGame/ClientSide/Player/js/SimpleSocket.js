function init()
{
	document.myform.url.value = "ws://localhost:5627/"
	document.myform.disconnectButton.disabled = true;
}
function doConnect()
{
  websocket = new WebSocket(document.myform.url.value);
  websocket.onopen = function(evt) { onOpen(evt) };
  websocket.onclose = function(evt) { onClose(evt) };
  websocket.onmessage = function(evt) { onMessage(evt) };
  websocket.onerror = function(evt) { onError(evt) };
  LaunchGame();
}
function sendPacket(){
  var jsonPacket = JSON.stringify(packet);
  websocket.send("packet//" + jsonPacket);
  packet.isClicked = false
  ;
}
function onOpen(evt)
{
  console.log("connected\n");
  document.myform.connectButton.disabled = true;
  document.myform.disconnectButton.disabled = false;
  doSend("connected//screenSize//" + document.getElementById("canvas").width + "//" + document.getElementById("canvas").height + "//player");
}
function onClose(evt)
{
  console.log("disconnected\n");
  document.myform.connectButton.disabled = false;
  document.myform.disconnectButton.disabled = true;
  StopGame();
}
function onMessage(evt)
{
  objectList = JSON.parse(evt.data);
  if (objectList.type == "clientInfo"){
    playerId = objectList.clientId;
    mapSize.x = objectList.mapX
    mapSize.y = objectList.mapY
  }
}
function onError(evt)
{
  console.log('error: ' + evt.data + '\n');
  websocket.close();
  document.myform.connectButton.disabled = false;
  document.myform.disconnectButton.disabled = true;
}
function doSend(message)
{ 
  websocket.send(message);
}
window.addEventListener("load", init, false );
function doDisconnect() {
  websocket.close();
}