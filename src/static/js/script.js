if ('webkitSpeechRecognition' in window) {
  var speechRecognition = new webkitSpeechRecognition();
  var startBtn = document.getElementById('start-btn');
  var stopVoiceOutputBtn = document.getElementById('stop-voice-output-btn'); // Reference to the new button
  var outputDiv = document.getElementById('output');
  var isListening = false; // Flag to toggle the listening state

  speechRecognition.continuous = false;
  speechRecognition.interimResults = false;
  speechRecognition.lang = 'en-US';

  speechRecognition.onresult = function(event) {
    var transcript = event.results[0][0].transcript;

    // Send the transcript to the API
    fetch('/api/v1/conversation', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ input: transcript }),
    })
    .then(response => response.json())
    .then(data => {
      console.log('Success:', data);
      // Handle the API response. For example, display a returned message:
      // Check if your API response contains a field for the response text you want to use.
      if(data.data) {
        outputDiv.textContent += data.data.answer;
        speechSynthesis.speak(new SpeechSynthesisUtterance(data.data.answer));
      }
    })
    .catch((error) => {
      console.error('Error:', error);
    });
  };

  speechRecognition.onstart = function() {
    isListening = true;
    startBtn.innerHTML = "Stop Voice Input"; // Update button text when recording starts
  };

  speechRecognition.onend = function() {
    isListening = false;
    startBtn.innerHTML = "Start Voice Input"; // Reset button text when recording stops
  };

  startBtn.onclick = function() {
    if (isListening) {
      speechRecognition.stop(); // Stop recording
    } else {
      speechRecognition.start(); // Start recording
    }
  };

  stopVoiceOutputBtn.onclick = function() {
    speechSynthesis.cancel(); // Stop speech synthesis (voice output)
  };
} else {
  alert('Your browser does not support the Web Speech API. Please use a compatible browser such as Google Chrome.');
}
