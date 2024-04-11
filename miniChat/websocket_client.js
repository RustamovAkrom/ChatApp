document.addEventListener('DOMContentLoaded', function(){

    const messagesContainsers = document.documentElement.querySelector("#messages_container");
    const messageinput = document.querySelector("[name=message_input]")
    const sendMessageButton = document.querySelector("[name=send_message_button]")

    let websocketClient = new WebSocket('ws://localhost:8000');

    websocketClient.onopen = () => {
        console.log("client connected!")
        // websocketClient.send('what ser name')

        sendMessageButton.onclick = () => {
            websocketClient.send(messageinput.value)
            messageinput.value = "";
        };
    };
  
}, false)
