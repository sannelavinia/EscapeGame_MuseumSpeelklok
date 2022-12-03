// 03-12-2022
// Arduino code to receive information from python code 
// to turn lamps and machine on and off
// Riham Mushmush

String inBytes;
String gameNum;
String machineNum;

// the setup function runs once when you press reset or power the board
void setup() {

  Serial.begin(9600);

  // initialize pins as an output.
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(A0, OUTPUT);
  pinMode(A1, OUTPUT);
  pinMode(A2, OUTPUT);
  pinMode(A3, OUTPUT);
  pinMode(A4, OUTPUT);
  pinMode(A5, OUTPUT);
  //  ...  

}

// the loop function runs over and over again forever
void loop() {

  if (Serial.available()>0){
    inBytes = Serial.readStringUntil('\n');

    machineNum = inBytes.substring(14);

    // activeMachine 0,1,2,3,4,5
    // begin with 2 first instead of 0 to decrease number of comparisons because of that the games uses activeMachine=2 too
    if (machineNum == "2"){
      digitalWrite(LED_BUILTIN, HIGH);  // add orders for activeMachine=0
    }
    else if (machineNum == "1"){
      digitalWrite(LED_BUILTIN, HIGH);  // add orders for activeMachine=1
    }
    else if (machineNum == "0"){
      digitalWrite(LED_BUILTIN, HIGH);  // add orders for activeMachine=2
    }
    else if (machineNum == "3"){
      digitalWrite(LED_BUILTIN, HIGH);  // add orders for activeMachine=3
    }
    else if (machineNum == "4"){
      digitalWrite(LED_BUILTIN, HIGH);  // add orders for activeMachine=4
    }
    else if (machineNum == "5"){
      digitalWrite(LED_BUILTIN, HIGH);  // add orders for activeMachine=5
    }
    // delay(1000);                       // wait for a second

    // activeGame 0,1,2,3,4,5,6
    gameNum = inBytes.substring(27);

    if (gameNum == "0"){
      digitalWrite(LED_BUILTIN, LOW);  // add orders for activeGame=0
    }
    else if (gameNum == "1"){
      digitalWrite(A0, HIGH);  // add orders for activeGame=1
    }
    else if (gameNum == "2"){
      digitalWrite(A1, HIGH);  // add orders for activeGame=2
    }
    else if (gameNum == "3"){
      digitalWrite(A2, HIGH);  // add orders for activeGame=3
    }
    else if (gameNum == "4"){
      digitalWrite(A3, HIGH);  // add orders for activeGame=4
    }
    else if (gameNum == "5"){
      digitalWrite(A4, HIGH);  // add orders for activeGame=5
    }
    else if (gameNum == "6"){
      digitalWrite(A5, HIGH);  // add orders for activeGame=6
    }
    // delay(1000);                       // wait for a second

    Serial.write("stop");  // send a signal to python to stop the program when the signal is recived
  
  }

}
