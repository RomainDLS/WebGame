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
function sendAngle(angle){
  websocket.send("angle//" + angle*180/Math.PI);
}
function onOpen(evt)
{
  console.log("connected\n");
  document.myform.connectButton.disabled = true;
  document.myform.disconnectButton.disabled = false;
  doSend("connected");
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