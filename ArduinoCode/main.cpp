#include <Arduino.h>
void setup() {
  Serial.begin(9600); // Inicia la comunicación serial a 9600 baudios
}

void loop() {
  String mensaje = "Hola desde arduino";
  Serial.println(mensaje);
  delay(1000); 
}
