#include "ACS712.h"


// Arduino UNO tem 5,0 volts com um valor máximo de ADC de 1023 passos

ACS712  ACS(A0, 5.0, 1023, 100);
//  ESP 32 example (pode requer resistores para diminuir a tensão lógica)
//  ACS712  ACS(25, 3.3, 4095, 185);

//Com auxilio de um multimetro, verifique a tensão fornecida na linha de 5V pela sua placa ARDUINO  e digite no lugar do valor atual.
//ESSA ETAPA É FUNDAMELTAL PARA GARANTIR A PRECISÃO DO SEU VOLTIMETRO!

  int Vlida = 0;
  float Vin = 0;
  int valorSensor = 0;
  
void setup() {

  
  //Para ESP32 115200 na Serial.begin
  Serial.begin(9600);
  ACS.autoMidPoint();
  //  Serial.println(ACS.getMidPoint());

  Serial.println("LABEL, Data, Hora, Corrente, Tensão");
}

void loop() {

  Serial.print("DATA, DATE, TIME,");
  sensor_corrente1();
  Serial.print(",");
  divisor_tensao();
  Serial.print(",");
  Serial.println("ROW,SET,2");

}

void sensor_corrente1(){

// ACS712 5A usa 185 mV por A
// ACS712 20A usa 100 mV por A
// ACS712 30A usa 66 mV por A
  float const calibrar = 0.100;
  
  int adc = analogRead(A0);
  float U = adc * 5 / 1023.0;
  float I = (U - 2.5) / calibrar;
  
  Serial.print(I);
  delay(100);

}
void sensor_corrente2(){
  float I = 0;
  //float U = 72;
  I = ACS.mA_DC();

  // Para caulcular potência, só multiplicar pela tensão nominal da bateria
  //float P = U * I;

  Serial.print(I);
  delay(100);
}


void divisor_tensao(){

  float const Vref = 4.1;
  float const Vt = 28.985;
  Vlida = analogRead(A2); //FAZ A LEITURA DO PINO ANALÓGICO E ARMAZENA NA VARIÁVEL O VALOR LIDO
  
  Vin = (Vt*Vlida*(Vref/1023));
  
  Serial.println(Vin,2); //IMPRIME NA SERIAL O VALOR DE TENSÃO DC MEDIDA E LIMITA O VALOR A 2 CASAS DECIMAIS
  delay(100); 

}
void temperatura(){
//Especificações  LM34 , LM335, LM35
//Escala Usada , Fahrenheit , Kelvin , Celsius
//Temperatura de trabalho em °C, -50°C até 150°C ,-40°C até 100°C ,-55°C até 150°C
//Linearidade, 10 mV/°F , 10 mV/K ,10 mV/°C
//Precisão a 25 °C,  ± 1°F, ± 1 K ,± 0.5°C

  valorSensor = analogRead(A1);
  
  //Conversão para tensão
  tensaoSaida = (valorSensor*5000)/1023;[

  //Calculo de temperatura
  tempC = tensaoSaida/10;

  Serial.print(tempC);
}
  
