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
