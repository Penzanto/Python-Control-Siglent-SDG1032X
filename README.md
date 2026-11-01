# Python-Control-Siglent-SDG1032X
A python lib file that can be used to control a Siglent SDG1032X via ethernet or USB using VISA command.

This python file can be called to use the following function on the Siglent SDG1032X signal generator:
-	Reset the signal generator
-	Set a sine wave
-	Set a square wave
-	Set a ramp
-	Set a pulse wave
-	Set a noise wave
-	Set a DC signal

At the end of the python file, you will see an example of how to use each of the function of this lib.

This python file uses the Pyvisa library. So, to use it you would need to install the Pyvisa lib and a visa library (Like the ni-visa library from National Instrument).

Exemple of how to use the principal function of this library.
```python
import SDG1032X_Lib  #import the python file

StrVisaName = "USB0::0xF4EC::0x1103::SDG1XCAD3R3735::INSTR"  #link a variable to the Visa name of the generator

SDG1032X_Lib.SFG_SDG1032X_Reset(StrVisaName)  #reset the signal generator
SDG1032X_Lib.SFG_SDG1032X_SetSineWave(StrVisaName, 1, 5e3, 5, 2, 100)  #set the generator to a sine wave
SDG1032X_Lib.SFG_SDG1032X_SetSquareWave(StrVisaName, 2, 300, 5, 2, 60, 95)  #set the generator to a square wave
SDG1032X_Lib.SFG_SDG1032X_SetRampWave(StrVisaName, 1, 100, 5, 2, 100, 50)  #set the generator to a ramp wave
SDG1032X_Lib.SFG_SDG1032X_SetNoiseWave(StrVisaName, 2, 1, 2)  #set the generator to a noise source
SDG1032X_Lib.SFG_SDG1032X_SetPulseWave(StrVisaName, 1, 200, 5, 1, 100e-6, 200e-6, 150e-6)  #set the generator to a pulse wave
SDG1032X_Lib.SFG_SDG1032X_SetDcWave(StrVisaName, 1, 10)  #set the generator to a DC signal generator
```
