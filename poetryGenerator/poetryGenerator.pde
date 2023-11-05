import oscP5.*;
import netP5.*; // networking 

OscP5 oscP5;
NetAddress destination;

String userInput = "";
String generatedPoetry = "";

void setup() {
  size(800,600);
  background(255);
  
  oscP5 = new OscP5(this, 12000);
  destination = new NetAddress("127.0.0.1", 57120);
  
  textSize(18);
  textAlign(LEFT);
}

void draw() {
  background(255);

  fill(0);
  text("User Input: " + userInput, 20, 50);

  fill(50, 150, 200);
  text("Generated Poetry:", 20, 100);
  text(generatedPoetry, 20, 140, width - 40, height - 140);
}

void keyPressed() {
  if (key == '\n') {
    // When Enter/Return key is pressed, send user input via OSC
    OscMessage msg = new OscMessage("/prompt");
    msg.add(userInput);
    oscP5.send(msg, destination);
  } else if (key == BACKSPACE) {
    // Handle backspace to delete characters
    if (userInput.length() > 0) {
      userInput = userInput.substring(0, userInput.length() - 1);
    }
  } else {
    // Append typed characters to user input
    userInput += key;
  }
}

void oscEvent(OscMessage message) {
  if (message.checkAddrPattern("/response")) {
    generatedPoetry = message.get(0).stringValue();
  }
}
