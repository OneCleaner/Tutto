
#include <ComponentObject.h>
#include <RangeSensor.h>
#include <SparkFun_VL53L1X.h>
//#include <vl53l1x_class.h>
//#include <vl53l1_error_codes.h>

#include "Wire.h"
#define BAUD 115200

extern "C" {
#include "utility/twi.h"  // from Wire library, so we can do bus scanning
}

bool direzione = true;

#define TCAADDR 0x70
#define VL53L1X_ADDR 0x29

SFEVL53L1X distanceSensor(Wire, -1, -1);

#define pwm_a 6  //PWM control
#define pwm_b 9
#define pwm_c 5
#define pwm_d 3

#define BUZZER 2

bool isMoving = false;

#define led_freni A0
#define led_fari 4

#define dir_a 7  //Motore posteriore destro
#define dir_b 8  //Motore anteriore destro
#define dir_c 11 //Motore posteriore sinistro
#define dir_d 10 //Motore anteriore sinistro

#define DESTRA 0
#define SINISTRA 1
#define AVANTI_SINISTRA 2
#define AVANTI_DESTRA 3
#define DIETRO_DESTRA 4
#define DIETRO_SINISTRA 5
#define SOTTO 6
#define AVANTI 7

/* CANALI TCASELECT
 * 0 -> DESTRA
 * 1 -> SINISTRA
 * 2 -> AVANTI-SINISTRA
 * 3 -> AVANTI-DESTRA
 * 4 -> DIETRO-DESTRA
 * 5 -> DIETRO-SINISTRA
 * 6 -> SOTTO #70 -> buzzer
 * 7 -> AVANTI
 */



int distance[8] = {0};

int tc = 0;

unsigned velocity = 230;

void setup (void) {

  Serial.begin(BAUD);
  while(!Serial);

  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(BUZZER, OUTPUT);

  //pwm motori output
  pinMode(pwm_a, OUTPUT);  //Set control pins to be outputs
  pinMode(pwm_b, OUTPUT);
  pinMode(pwm_c, OUTPUT);
  pinMode(pwm_d, OUTPUT);

  //driver motori output
  pinMode(dir_a, OUTPUT);
  pinMode(dir_b, OUTPUT);
  pinMode(dir_c, OUTPUT);
  pinMode(dir_d, OUTPUT);

  //luci freni output
  pinMode(led_freni, OUTPUT);
  pinMode(led_fari, OUTPUT);

  //mettiamo così che parta in avanti alla prima
  digitalWrite(dir_a, HIGH);
  digitalWrite(dir_b, HIGH);
  digitalWrite(dir_c, HIGH);
  digitalWrite(dir_d, HIGH);
  digitalWrite(led_fari, HIGH);
  digitalWrite(led_freni, HIGH);

  setVelocity(velocity);
  spegni();

  Wire.begin();
  delay(1000);

  Serial.print("\nTCA ADDR: 0x"); Serial.println(TCAADDR, HEX);
  delay(1000);
  for (uint8_t i = 0; i < 8; i++) {
    tcaselect(i);
    Serial.print("TCA Port #"); Serial.println(i);
    if (distanceSensor.begin() == 0) //Begin returns 0 on a good init
      Serial.println(" Sensor online!");
    delay(333);
  }
}

int getDistance(int sensor){
  tcaselect(sensor);
  distanceSensor.startRanging();
  int distance = distanceSensor.getDistance();
  distanceSensor.stopRanging();
  return distance;
}

void loop(void){

  String data = "";
  /*for (uint8_t i = 0; i < 8; i++) {
    tcaselect(i);
    distanceSensor.startRanging();
      distance[i] = distanceSensor.getDistance();
    distanceSensor.stopRanging();

  }*/

  /*if(distance[2] < 250 || distance[3] < 250 || distance[7] < 250) {
    setVelocity(0);

    tone(BUZZER, 1000, 100);
  } else {
    
    tone(BUZZER, 0, 100);
    
    if(isMoving) setVelocity(velocity); //setVelocity(255);
  }*/

  /*distanceSensor.startRanging();
  Serial.print("Distance: ");
  Serial.println(distanceSensor.getDistance());
  distanceSensor.stopRanging();
  delay(200);*/

  /*int dis = getDistance(SOTTO);
  if (dis > 70){
    tone(BUZZER, 2000, 300);
    delay(300);
    tone(BUZZER, 1000, 300);
    delay(300);
  }else{
    noTone(BUZZER);
  }*/

  int dist;
  if(direzione)
    dist = (getDistance(AVANTI_SINISTRA) + getDistance(AVANTI) + getDistance(AVANTI_DESTRA)) / 3;
  else
    dist = (getDistance(DIETRO_DESTRA) + getDistance(DIETRO_SINISTRA)) / 2;
  /*Serial.println(dist);
  Serial.println(direzione ? "avanti" : "retro");*/
  /*if (dist < 600)
  setVelocity(0);*/
  

  while(Serial.available() > 0){
    data = Serial.readString();
    /*tc = Serial.parseInt();
    tcaselect(tc);
    Serial.print("Nuovo tcaselect: ");
    Serial.println(tc);
    break;*/
    
    if(data == "dritto"){
      
        accendi();
        digitalWrite(dir_a, HIGH);
        digitalWrite(dir_b, HIGH);
        digitalWrite(dir_c, HIGH);
        digitalWrite(dir_d, HIGH);
        digitalWrite(led_freni, LOW);
        setVelocity(velocity);
        Serial.println("Vado dritto");
        direzione = true;

    }

    else if(data == "destra"){
        digitalWrite(dir_a, LOW);   //ruote di destra
        digitalWrite(dir_b, LOW);
        digitalWrite(dir_c, HIGH);
        digitalWrite(dir_d, HIGH);
        digitalWrite(led_freni, LOW);
        setVelocity(velocity);
        Serial.println("Svolto a destra");

    }

    else if(data == "gira-destra"){
        analogWrite(pwm_a, velocity -40);
        analogWrite(pwm_b, velocity -40);
        digitalWrite(dir_a, HIGH);   //ruote di destra
        digitalWrite(dir_b, HIGH);
        digitalWrite(dir_c, HIGH);
        digitalWrite(dir_d, HIGH);
        digitalWrite(led_freni, LOW);
        setVelocity(velocity);
        Serial.println("Giro a destra");
    }

    else if(data == "sinistra"){
        digitalWrite(dir_a, HIGH);
        digitalWrite(dir_b, HIGH);
        digitalWrite(dir_c, LOW); //ruote di sinistra
        digitalWrite(dir_d, LOW);
        digitalWrite(led_freni, LOW);
        setVelocity(velocity);
        Serial.println("Svolto a sinistra");
    }

    else if(data == "gira-sinistra"){
        analogWrite(pwm_c, velocity -40);
        analogWrite(pwm_d, velocity -40);
        digitalWrite(dir_a, HIGH);   //ruote di destra
        digitalWrite(dir_b, HIGH);
        digitalWrite(dir_c, LOW);
        digitalWrite(dir_d, LOW);
        digitalWrite(led_freni, LOW);
        setVelocity(velocity);
        Serial.println("giro a sinistra");
    }
    else if(data == "retro"){
      accendi();
        digitalWrite(dir_a, LOW);
        digitalWrite(dir_b, LOW);
        digitalWrite(dir_c, LOW); //ruote di sinistra
        digitalWrite(dir_d, LOW);
        digitalWrite(led_freni, HIGH);
        setVelocity(velocity);
        Serial.println("Torno indietro");
        direzione = false;
    }

    else if(data == "spegni"){
        spegni();
    }

    else if(data == "accendi"){
        accendi();
    }


    else if(isNum(data) && data.toInt() > 0 && data.toInt() <= 255){
        setVelocity(data.toInt());
        Serial.println("cambiata velocità a: " + data);
    }

    else {
      Serial.println("Comando non riconosciuto: " + data);
    }
    delay(200);
  }
  delay(200);
}

void spegni(){
  digitalWrite(led_freni, HIGH);
  setVelocity(0);
  isMoving = false;
  Serial.println("Spengo i motori");
}

void accendi(){
  digitalWrite(led_freni, LOW);
  setVelocity(255);
  isMoving = true;
  Serial.println("Accendo i motori");
}


//inserire solo velocità tra 0 e 255, altrimenti la funzione non cambierà lo stato del motore
void setVelocity(unsigned v){

  velocity = v;

  if(v > 255)
    return;

  analogWrite(pwm_a, v);
  analogWrite(pwm_b, v);  //minimo 190 o non partono wewo
  analogWrite(pwm_c, v);
  analogWrite(pwm_d, v);

  return;
}

bool isNum(String str){

  for(int i = 0; i < str.length(); i++){
    if(!isDigit(str[i]))
      return false;
  }

  return true;
}

void tcaselect(uint8_t i) {
  if (i > 7) return;

  Wire.beginTransmission(TCAADDR);
  Wire.write(1 << i);
  Wire.endTransmission();
}
