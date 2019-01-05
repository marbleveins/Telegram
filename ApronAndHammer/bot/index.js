var express = require('express');
var app = express();
var bodyParser = require('body-parser');
const axios = require('axios');

var TELEGRAM_API_TOKEN = "717624899:AAHwsfG_weAuTn8asirPRQKGIA34bBySGro";
var TELEGRAM_URL = "https://api.telegram.org/bot" + TELEGRAM_API_TOKEN + "/sendMessage";


app.use(bodyParser.json()) // for parsing application/json
app.use(
  bodyParser.urlencoded({
    extended: true
  })
); // for parsing application/x-www-form-urlencoded

//This is the route the API will call
app.post('/new-message', function(req, res) {
  const { message } = req.body.message;

  //Each message contains "text" and a "chat" object, which has an "id" which is the chat id

  if (!message || message.text.toLowerCase().indexOf('marco') < 0) {
    // In case a message is not present, or if our message does not have the word marco in it, do nothing and return an empty response
    return res.end();
  }

  // If we've gotten this far, it means that we have received a message containing the word "marco".
  // Respond by hitting the telegram bot API and responding to the approprite chat_id with the word "Polo!!"
  // Remember to use your own API toked instead of the one below  "https://api.telegram.org/bot<your_api_token>/sendMessage"
  var reply = "pollo!";
  sendMessage(TELEGRAM_URL,message,reply,res);
  
});

app.post("/start_bot", function(req, res) {
	const { message } = req.body.message;
	var reply = "Welcome to Apron & Hammer bot. bot started";
	if(message.text.toLowerCase().indexOf("hi") !== -1){
		sendMessage(TELEGRAM_URL,message,reply,res);
	}
});

// Finally, start our server
app.listen(3000, function() {
  console.log('Telegram app listening on port 3000!')
});

function sendMessage(url, message,reply,res){
	axios.post(url, {chat_id: message.chat.id,
		text: reply
	}).then(response => {
		console.log("Message posted");
		res.end("ok");
	}).catch(error =>{
		console.log(error);
		res.end('Error :' + err);
	});
}

