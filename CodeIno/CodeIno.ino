#include <Servo.h>

Servo gate;
Servo lever;

const int midleAngle = 83;

const int pinBuzzer = 2;
const int trigPin = 7;
const int echoPin = 6;
const int trigPin1 = 13;
const int echoPin1 = 12;
const int trigPin2 = 11;
const int echoPin2 = 10;
const int trigPin3 = 9;
const int echoPin3 = 8;

long duration, duration1, duration2, duration3;
int distance, distance1, distance2, distance3;
int angel =0;
int mode = 0;
int gerak = 0;
int point, lever_position;

char data; 

void setup() {
  Serial.begin(9600);
  gate.attach(3);
  lever.attach(5);
  gate.write(10); //0-70
  lever.write(midleAngle);
  lever_position = midleAngle;
  
  pinMode(pinBuzzer, OUTPUT);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(trigPin1, OUTPUT);
  pinMode(echoPin1, INPUT);
  pinMode(trigPin2, OUTPUT);
  pinMode(echoPin2, INPUT);
  pinMode(trigPin3, OUTPUT);
  pinMode(echoPin3, INPUT);
  
  
  digitalWrite(pinBuzzer, HIGH);
  delay(500);
  digitalWrite(pinBuzzer, LOW);
  delay(1000);
}

void loop() {
  
  bacaUS();
  get_value(&angel);

  if(distance < 25 and mode == 0){mode = 1; digitalWrite(pinBuzzer, HIGH); delay(200); digitalWrite(pinBuzzer, LOW); delay(4000);}
  else if(mode == 1){gerak = angel; mode = 0;}

  if(gerak == 0){gate.write(8); point = midleAngle;}
  else if(gerak == 1){point = 0; delay(500);}
  else if(gerak == 2){point = midleAngle; delay(500);} 
  else if(gerak == 3){point = 170; delay(500);}

  if(lever_position > point)
  {
    for(int i = lever_position; i >= point; i--){lever.write(i); lever_position = i; /*Serial.println(lever_position);*/ delay(70);}
  }
  
  if(lever_position < point)
  {
    for(int i = lever_position; i <= point; i++){lever.write(i); lever_position = i; /*Serial.println(lever_position);*/ delay(70);}
  }
  
  if(gerak > 0 and gerak < 4){gate.write(70); delay(1000); gerak = 0;}

  if(distance1 + distance2 + distance3 < 80)
  {
    digitalWrite(pinBuzzer, HIGH); delay(50); 
    digitalWrite(pinBuzzer, LOW); delay(50);
    digitalWrite(pinBuzzer, HIGH); delay(50); 
    digitalWrite(pinBuzzer, LOW); delay(500);
  }

//  Serial.print(distance);
//  Serial.print(" , ");
//  Serial.print(distance1);
//  Serial.print(" , ");
//  Serial.print(distance2);
//  Serial.print(" , ");
//  Serial.print(distance3);
//  Serial.print(" , ");
//  Serial.print(gerak);
//  Serial.print(" , ");
//  Serial.println(angel);
}
