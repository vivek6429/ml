int temp ;
int current ;
int vib;
float value=0;
float rev=0;
int rpm;
int oldtime=0;
int time;
void isr() //interrupt service routine
{
rev++;
}
void setup() 
{
 Serial.begin(9600);
attachInterrupt(0,isr,RISING);
}

void loop() 
{
 String data="";
 temp= analogRead(A1);
 current=analogRead(A0);
 vib=analogRead(A2);
 delay(1000);
 detachInterrupt(0); //detaches the interrupt
 time=millis()-oldtime; //finds the time
 rpm=(rev/time)*60000*3; //calculates rpm for blades
 oldtime=millis(); //saves the current time
 rev=0;
 attachInterrupt(0,isr,RISING);

  data=String(current)+"%"+String(temp)+"#"+String(rpm)+"&"+String(vib)+"@";
  Serial.println(data);
  delay(1000);
  
}
