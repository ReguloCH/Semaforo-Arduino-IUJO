// -------- Semáforo 1 --------
const int V1 = 13;
const int AM1 = 12;
const int R1 = 11;
const int P1 = 10;

// -------- Semáforo 2 --------
const int V2 = 9;
const int AM2 = 8;
const int R2 = 7;
const int P2 = 6;

// -------- Semáforo 3 --------
const int V3 = 5;
const int AM3 = 4;
const int R3 = 3;
const int P3 = 2;

void setup() {
  for (int pin = 2; pin <= 13; pin++) {
    pinMode(pin, OUTPUT);
  }
}

void loop() {

 
  setRojoTodos();
  verde(V1, R1);
  delay(5000);

  amarillo(V1, AM1);
  delay(2000);

  rojo(R1);
  pasoPeatonal();

 
  setRojoTodos();
  verde(V2, R2);
  delay(5000);

  amarillo(V2, AM2);
  delay(2000);

  rojo(R2);
  pasoPeatonal();

 
  setRojoTodos();
  verde(V3, R3);
  delay(5000);

  amarillo(V3, AM3);
  delay(2000);

  rojo(R3);
  pasoPeatonal();
}


void setRojoTodos() {
  digitalWrite(R1, HIGH);
  digitalWrite(R2, HIGH);
  digitalWrite(R3, HIGH);

  digitalWrite(V1, LOW);
  digitalWrite(V2, LOW);
  digitalWrite(V3, LOW);

  digitalWrite(AM1, LOW);
  digitalWrite(AM2, LOW);
  digitalWrite(AM3, LOW);

  apagarPeatonal();
}


void verde(int verdePin, int rojoPin) {
  digitalWrite(rojoPin, LOW);
  digitalWrite(verdePin, HIGH);
}


void amarillo(int verdePin, int amarilloPin) {
  digitalWrite(verdePin, LOW);
  digitalWrite(amarilloPin, HIGH);
}


void rojo(int rojoPin) {
  digitalWrite(rojoPin, HIGH);
}


void pasoPeatonal() {
  encenderPeatonal();
  delay(3000);
  apagarPeatonal();
}