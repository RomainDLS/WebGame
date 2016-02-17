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
function sendAngle(){
  websocket.send("angle//" + getAngle()*90/Math.PI);
}
function onOpen(evt)
{
  console.log("connected\n");
  document.myform.connectButton.disabled = true;
  document.myform.disconnectButton.disabled = false;
}
function onClose(evt)
{
  console.log("disconnected\n");
  StopGame();
  document.myform.connectButton.disabled = false;
  document.myform.disconnectButton.disabled = true;
}
function onMessage(evt)
{
  objectList = []
  for (i=0; i< evt.data.split("//").length; i++){
    objectList.push(JSON.parse(evt.data.split("//")[i]));
  }
  console.log(objectList);
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