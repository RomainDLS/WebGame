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
function sendMessage(){
  websocket.send(getAngle()*90/Math.PI);
}
function onOpen(evt)
{
  writeToScreen("connected\n");
  document.myform.connectButton.disabled = true;
  document.myform.disconnectButton.disabled = false;
}
function onClose(evt)
{
  writeToScreen("disconnected\n");
  StopGame();
  document.myform.connectButton.disabled = false;
  document.myform.disconnectButton.disabled = true;
}
function onMessage(evt)
{
  writeToScreen("response: " + evt.data + '\n');
}
function onError(evt)
{
  writeToScreen('error: ' + evt.data + '\n');
  websocket.close();
  document.myform.connectButton.disabled = false;
  document.myform.disconnectButton.disabled = true;
}
function doSend(message)
{ 
  websocket.send(message);
}
function writeToScreen(message)
{
  console.log(message);
}
window.addEventListener("load", init, false );
function doDisconnect() {
  websocket.close();
}