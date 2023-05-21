String int_inString1 = "";
uint16_t integer1;
void get_value(int* value)
{
  while(Serial.available())
  {
    int inchar = Serial.read();
    if(isDigit(inchar)){int_inString1+=(char)inchar;}
  
    if(inchar == '\n')
    {
      *value = int_inString1.toInt();
      int_inString1 = "";
    }
  }
}

void bacaUS()
{

//  digitalWrite(trigPin, LOW);
//  digitalWrite(trigPin1, LOW);
//  digitalWrite(trigPin2, LOW);
//  digitalWrite(trigPin3, LOW);
//  delayMicroseconds(2);
//  digitalWrite(trigPin, HIGH);
//  digitalWrite(trigPin1, HIGH);
//  digitalWrite(trigPin2, HIGH);
//  digitalWrite(trigPin3, HIGH);
//  delayMicroseconds(10);
//  digitalWrite(trigPin, LOW);
//  duration = pulseIn(echoPin, HIGH);
//  duration1 = pulseIn(echoPin1, HIGH);
//  duration2 = pulseIn(echoPin2, HIGH);
//  duration3 = pulseIn(echoPin3, HIGH);
//  distance= duration*0.034/2;
//  distance1= duration1*0.034/2;
//  distance2= duration2*0.034/2;
//  distance3= duration3*0.034/2;

  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance= duration*0.034/2;
  
  digitalWrite(trigPin1, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin1, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin1, LOW);
  duration = pulseIn(echoPin1, HIGH);
  distance1= duration*0.034/2;

  digitalWrite(trigPin2, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin2, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin2, LOW);
  duration = pulseIn(echoPin2, HIGH);
  distance2= duration*0.034/2;

  digitalWrite(trigPin3, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin3, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin3, LOW);
  duration = pulseIn(echoPin3, HIGH);
  distance3= duration*0.034/2;
  
}
