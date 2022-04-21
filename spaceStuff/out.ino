long randNumber1, randNumber2, randNumber3, randNumber4, randNumber5, randNumber6;



void setup(){
  Serial.begin(9600);

  // if analog input pin 0 is unconnected, random analog
  // noise will cause the call to randomSeed() to generate
  // different seed numbers each time the sketch runs.
  // randomSeed() will then shuffle the random function.
  randomSeed(analogRead(0));
}

void loop() {
  // print a random number from 0 to 299
  randNumber1 = random(60000);
  randNumber2 = random(60000);
  randNumber3 = random(60000);
  randNumber4 = random(60000);
  randNumber5 = random(60000);
  randNumber6 = random(60000);
  
  Serial.print(",");
  Serial.print(randNumber1);
  Serial.print(",");
  Serial.print(randNumber2);
  Serial.print(",");
  Serial.print(randNumber3);
  Serial.print(",");
  Serial.print(randNumber4);
  Serial.print(",");
  Serial.print(randNumber5);
  Serial.print(",");
  Serial.print(randNumber6);
  Serial.println(",");

  delay(50);
}

