#-----------------------------------------------------------------Description-----------------------------------------------------------------
# This python file is a library that can be used to control via Ethernet or USB the Siglent function generator SDG1032X.
#-----------------------------------------------------------------lib used-----------------------------------------------------------------
import pyvisa   #lib used to send SCPI command to the equipment throught the VISA library

#-----------------------------------------------------------------Main-----------------------------------------------------------------
def SFG_SDG1032X_Reset(StrVisaName):   #Tested
    """function that reset the function generator

    Args:
        StrVisaName (string): visa name of the signal generator
    """
    visaHandle = pyvisa.ResourceManager().open_resource(StrVisaName)
    visaHandle.write("*RST")
    visaHandle.query("*OPC?")
    visaHandle.close()
    
def SFG_SDG1032X_SetSineWave(StrVisaName, NumChannel, NumFrequency, NumAmplitude, NumOffset, NumPhase): #TESTED
    """function used to setup a sinawase signal on any channel of the signal function generator

    Args:
        StrVisaName (string): visa name of the signal generator
        NumChannel (number): channel number of the signal generator (1 or 2)
        NumFrequency (number): frequency of the output (Hz)
        NumAmplitude (number): amplitude of the output (Vpp)
        NumOffset (number): offset of the output (V)
        NumPhase (number): phase of the output (degree)
    """
    SFG_SDG1032X_OuputWaveForm(StrVisaName, NumChannel, "SINE")   #set the waveform type
    SFG_SDG1032X_ChannelFrequency(StrVisaName, NumChannel, NumFrequency)    #set the output frequency
    SFG_SDG1032X_ChannelAmplitude(StrVisaName, NumChannel, NumAmplitude)    #set the channel amplitude
    SFG_SDG1032X_ChannelOffset(StrVisaName, NumChannel, NumOffset) #set the offset
    SFG_SDG1032X_ChannelPhase(StrVisaName, NumChannel, NumPhase)    #set the phase of the signal

def SFG_SDG1032X_SetSquareWave(StrVisaName, NumChannel, NumFrequency, NumAmplitude, NumOffset, NumPhase, NumDuty):  #TESTED
    """function used to setup a square wave signal on any channel of the signal function generator

    Args:
        StrVisaName (string): visa name of the signal generator
        NumChannel (number): channel number of the signal generator (1 or 2)
        NumFrequency (number): frequency of the output (Hz)
        NumAmplitude (number): amplitude of the output (Vpp)
        NumOffset (number): offset of the output (V)
        NumPhase (number): phase of the output (degree)
        NumDuty (number): duty of the output (percent)
    """
    SFG_SDG1032X_OuputWaveForm(StrVisaName, NumChannel, "SQUARE")   #set the waveform type
    SFG_SDG1032X_ChannelFrequency(StrVisaName, NumChannel, NumFrequency)    #set the output frequency
    SFG_SDG1032X_ChannelAmplitude(StrVisaName, NumChannel, NumAmplitude)    #set the channel amplitude
    SFG_SDG1032X_ChannelOffset(StrVisaName, NumChannel, NumOffset) #set the offset
    SFG_SDG1032X_ChannelPhase(StrVisaName, NumChannel, NumPhase)    #set the phase of the signal
    SFG_SDG1032X_ChannelDuty(StrVisaName, NumChannel, NumDuty)  #set the duty of the signal

def SFG_SDG1032X_SetRampWave(StrVisaName, NumChannel, NumFrequency, NumAmplitude, NumOffset, NumPhase, NumSymmetry):    #TESTED
    """function used to setup a ramp wave signal on any channel of the signal function generator

    Args:
        StrVisaName (string): visa name of the signal generator
        NumChannel (number): channel number of the signal generator (1 or 2)
        NumFrequency (number): frequency of the output (Hz)
        NumAmplitude (number): amplitude of the output (Vpp)
        NumOffset (number): offset of the output (V)
        NumPhase (number): phase of the output (degree)
        NumSymmetry (number): symmetry of the output (percent)
    """
    SFG_SDG1032X_OuputWaveForm(StrVisaName, NumChannel, "RAMP")   #set the waveform type
    SFG_SDG1032X_ChannelFrequency(StrVisaName, NumChannel, NumFrequency)    #set the output frequency
    SFG_SDG1032X_ChannelAmplitude(StrVisaName, NumChannel, NumAmplitude)    #set the channel amplitude
    SFG_SDG1032X_ChannelOffset(StrVisaName, NumChannel, NumOffset) #set the offset
    SFG_SDG1032X_ChannelPhase(StrVisaName, NumChannel, NumPhase)    #set the phase of the signal
    SFG_SDG1032X_ChannelSymmetry(StrVisaName, NumChannel, NumSymmetry)  #set the symmetry of the signal

def SFG_SDG1032X_SetPulseWave(StrVisaName, NumChannel, NumFrequency, NumAmplitude, NumOffset, NumPulseWidth, NumRiseEdge, NumDelay):    #TESTED
    """function used to setup a pulse wave signal on any channel of the signal function generator

    Args:
        StrVisaName (string): visa name of the signal generator
        NumChannel (number): channel number of the signal generator (1 or 2)
        NumFrequency (number): frequency of the output (Hz)
        NumAmplitude (number): amplitude of the output (Vpp)
        NumOffset (number): offset of the output (V)
        NumPulseWidth (number): pulse signal width (S)
        NumRiseEdge (number): set the rise edge of the signal (S)
        NumDelay (number): set the delay of the signal (S)
    """
    SFG_SDG1032X_OuputWaveForm(StrVisaName, NumChannel, "PULSE")   #set the waveform type
    SFG_SDG1032X_ChannelFrequency(StrVisaName, NumChannel, NumFrequency)    #set the output frequency
    SFG_SDG1032X_ChannelAmplitude(StrVisaName, NumChannel, NumAmplitude)    #set the channel amplitude
    SFG_SDG1032X_ChannelOffset(StrVisaName, NumChannel, NumOffset) #set the offset
    SFG_SDG1032X_ChannelPulseWidth(StrVisaName, NumChannel, NumPulseWidth)  #set the pulse width
    SFG_SDG1032X_ChannelRiseEdge(StrVisaName, NumChannel, NumRiseEdge)  #set the rise edge of the signal
    SFG_SDG1032X_ChannelDelay(StrVisaName, NumChannel, NumDelay)   #set the delay of the signal

def SFG_SDG1032X_SetNoiseWave(StrVisaName, NumChannel, NumStdDev, NumMean): #TESTED
    """function used to setup a noise wave signal on any channel of the signal function generator

    Args:
        StrVisaName (string): visa name of the signal generator
        NumChannel (number): channel number of the signal generator (1 or 2)
        NumStdDev (number): standard deviation of the noise output (V)
        NumMean (number): mean of the noise output (V)
    """
    SFG_SDG1032X_OuputWaveForm(StrVisaName, NumChannel, "NOISE")   #set the waveform type
    SFG_SDG1032X_ChannelStdDev(StrVisaName, NumChannel, NumStdDev)  #set the standard deviation of the noise
    SFG_SDG1032X_ChannelMean(StrVisaName, NumChannel, NumMean)  #set the mean of the noise

def SFG_SDG1032X_SetDcWave(StrVisaName, NumChannel, NumDcOffset):   #TESTED
    """function that set a specific channel to the DC waveform type

    Args:
        StrVisaName (string): visa name of the signal generator
        NumChannel (number): channel number of the signal generator (1 or 2)
        NumDcOffset (number): offset of the output (V)
    """
    SFG_SDG1032X_OuputWaveForm(StrVisaName, NumChannel, "DC")   #set the waveform type
    SFG_SDG1032X_ChannelOffset(StrVisaName, NumChannel, NumDcOffset) #set the offset

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
def SFG_SDG1032X_ChannelOnOff(StrVisaName, NumChannel, NumOnOff):   #TESTED
    """Function that turn On and Off a channel output

    Args:
        StrVisaName (string): visa name of the signal generator
        NumChannel (number): channel number of the signal generator (1 or 2)
        NumOnOff (number): 0 to turn off the output, 1 to turn it on
    """
    visaHandle = pyvisa.ResourceManager().open_resource(StrVisaName)
    if (NumOnOff==1):
        visaHandle.write("C" + str(NumChannel) +":OUTP ON")
    else:
        visaHandle.write("C" + str(NumChannel) +":OUTP OFF")
    visaHandle.query("*OPC?")
    visaHandle.close()

def SFG_SDG1032X_ChannelImpedance(StrVisaName, NumChannel, NumImpedance):   #TESTED
    """function that set the load of the output

    Args:
        StrVisaName (string): visa name of the signal generator
        NumChannel (number): channel number of the signal generator (1 or 2)
        NumImpedance (number): set the impedance of the output of the generator (under 50, the output is set to 50ohms. over 50 set the impedance to High impedance)
    """
    visaHandle = pyvisa.ResourceManager().open_resource(StrVisaName)
    if (NumImpedance <= 50):
        visaHandle.write("C" + str(NumChannel) +":OUTP LOAD,50")
    else:
        visaHandle.write("C" + str(NumChannel) +":OUTP LOAD,HZ")
    visaHandle.query("*OPC?")
    visaHandle.close()

def SFG_SDG1032X_OuputWaveForm(StrVisaName, NumChannel, StrWaveType):   #TESTED
    """function that set the output wave of a specific channel

    Args:
        StrVisaName (string): visa name of the signal generator
        NumChannel (number): channel number of the signal generator (1 or 2)
        StrWaveType (string): set the wave type of a specific channel 
                                SINE = sinewave
                                SQUARE = square wave
                                RAMP = ramp
                                PULSE = pulse 
                                NOISE = noise
                                DC = DC
    """
    visaHandle = pyvisa.ResourceManager().open_resource(StrVisaName)
    visaHandle.write("C" + str(NumChannel) +":BSWV WVTP," + StrWaveType)
    visaHandle.query("*OPC?")
    visaHandle.close()

def SFG_SDG1032X_ChannelOffset(StrVisaName, NumChannel, NumOffset):   #TESTED
    """function used to change the offset of the channel

    Args:
        StrVisaName (string): visa name of the signal generator
        NumChannel (number): channel number of the signal generator (1 or 2)
        NumOffset (number): offset of the output (V)
    """
    visaHandle = pyvisa.ResourceManager().open_resource(StrVisaName)
    visaHandle.write("C" + str(NumChannel) + ":BSWV OFST," + str(NumOffset))
    visaHandle.query("*OPC?")
    visaHandle.close()

def SFG_SDG1032X_ChannelFrequency(StrVisaName, NumChannel, NumFrequency):   #TESTED
    """function used to change the freqeuncy of the output

    Args:
        StrVisaName (string): visa name of the signal generator
        NumChannel (number): channel number of the signal generator (1 or 2)
        NumFrequency (number): frequency of the output (Hz)
    """
    visaHandle = pyvisa.ResourceManager().open_resource(StrVisaName)
    visaHandle.write("C" + str(NumChannel) + ":BSWV FRQ," + str(NumFrequency))
    visaHandle.query("*OPC?")
    visaHandle.close()

def SFG_SDG1032X_ChannelAmplitude(StrVisaName, NumChannel, NumAmplitude):   #TESTED
    """function used to change the frequency of the output

    Args:
        StrVisaName (string): visa name of the signal generator
        NumChannel (number): channel number of the signal generator (1 or 2)
        NumAmplitude (number): amplitude of the output (Vpp)
    """
    visaHandle = pyvisa.ResourceManager().open_resource(StrVisaName)
    visaHandle.write("C" + str(NumChannel) + ":BSWV AMP," + str(NumAmplitude))
    visaHandle.query("*OPC?")
    visaHandle.close()

def SFG_SDG1032X_ChannelPhase(StrVisaName, NumChannel, NumPhase):   #TESTED
    """function used to change the phase of the output

    Args:
        StrVisaName (string): visa name of the signal generator
        NumChannel (number): channel number of the signal generator (1 or 2)
        NumPhase (number): phase of the output (degree)
    """
    visaHandle = pyvisa.ResourceManager().open_resource(StrVisaName)
    visaHandle.write("C" + str(NumChannel) + ":BSWV PHSE," + str(NumPhase))
    visaHandle.query("*OPC?")
    visaHandle.close()

def SFG_SDG1032X_ChannelDuty(StrVisaName, NumChannel, NumDuty):   #TESTED
    """function used to change the duty of the output

    Args:
        StrVisaName (string): visa name of the signal generator
        NumChannel (number): channel number of the signal generator (1 or 2)
        NumDuty (number): duty of the output (percent)
    """
    visaHandle = pyvisa.ResourceManager().open_resource(StrVisaName)
    visaHandle.write("C" + str(NumChannel) + ":BSWV DUTY," + str(NumDuty))
    visaHandle.query("*OPC?")
    visaHandle.close()

def SFG_SDG1032X_ChannelSymmetry(StrVisaName, NumChannel, NumSymmetry):   #TESTED
    """function used to change the duty of the output

    Args:
        StrVisaName (string): visa name of the signal generator
        NumChannel (number): channel number of the signal generator (1 or 2)
        NumSymmetry (number): symmetry of the output (percent)
    """
    visaHandle = pyvisa.ResourceManager().open_resource(StrVisaName)
    visaHandle.write("C" + str(NumChannel) + ":BSWV SYM," + str(NumSymmetry))
    visaHandle.query("*OPC?")
    visaHandle.close()

def SFG_SDG1032X_ChannelStdDev(StrVisaName, NumChannel, NumStdDev):   #TESTED
    """function used to change the standard deviation of noise

    Args:
        StrVisaName (string): visa name of the signal generator
        NumChannel (number): channel number of the signal generator (1 or 2)
        NumStdDev (number): standard deviation of the noise output (V)
    """
    visaHandle = pyvisa.ResourceManager().open_resource(StrVisaName)
    visaHandle.write("C" + str(NumChannel) + ":BSWV STDEV," + str(NumStdDev))
    visaHandle.query("*OPC?")
    visaHandle.close()

def SFG_SDG1032X_ChannelMean(StrVisaName, NumChannel, NumMean):   #TESTED
    """function used to change the mean of noise

    Args:
        StrVisaName (string): visa name of the signal generator
        NumChannel (number): channel number of the signal generator (1 or 2)
        NumMean (number): mean of the noise output (V)
    """
    visaHandle = pyvisa.ResourceManager().open_resource(StrVisaName)
    visaHandle.write("C" + str(NumChannel) + ":BSWV MEAN," + str(NumMean))
    visaHandle.query("*OPC?")
    visaHandle.close()

def SFG_SDG1032X_ChannelPulseWidth(StrVisaName, NumChannel, NumPulseWidth):   #TESTED
    """function used to change the pulse width of a signal

    Args:
        StrVisaName (string): visa name of the signal generator
        NumChannel (number): channel number of the signal generator (1 or 2)
        NumPulseWidth (number): pulse signal width (S)
    """
    visaHandle = pyvisa.ResourceManager().open_resource(StrVisaName)
    visaHandle.write("C" + str(NumChannel) + ":BSWV WIDTH," + str(NumPulseWidth))
    visaHandle.query("*OPC?")
    visaHandle.close()

def SFG_SDG1032X_ChannelRiseEdge(StrVisaName, NumChannel, NumRiseEdge):   #TESED
    """function used to change the pulse width of a signal

    Args:
        StrVisaName (string): visa name of the signal generator
        NumChannel (number): channel number of the signal generator (1 or 2)
        NumRiseEdge (number): set the rise edge of the signal (S)
    """
    visaHandle = pyvisa.ResourceManager().open_resource(StrVisaName)
    visaHandle.write("C" + str(NumChannel) + ":BSWV RISE," + str(NumRiseEdge))
    visaHandle.query("*OPC?")
    visaHandle.close()

def SFG_SDG1032X_ChannelDelay(StrVisaName, NumChannel, NumDelay):   #
    """function used to change the delay of the signal

    Args:
        StrVisaName (string): visa name of the signal generator
        NumChannel (number): channel number of the signal generator (1 or 2)
        NumDelay (number): set the delay of the signal (S)
    """
    visaHandle = pyvisa.ResourceManager().open_resource(StrVisaName)
    visaHandle.write("C" + str(NumChannel) + ":BSWV DLY," + str(NumDelay))
    visaHandle.query("*OPC?")
    visaHandle.close()

#-----------------------------------------------------------------__name__ guard-----------------------------------------------------------------
if __name__ == "__main__":
    None

    #Exemple use of this library
    # StrVisaName = "USB0::0xF4EC::0x1103::SDG1XCAD3R3735::INSTR"

    # SFG_SDG1032X_Reset(StrVisaName)
    # SFG_SDG1032X_ChannelOnOff(StrVisaName, 2, 0)
    # SFG_SDG1032X_ChannelImpedance(StrVisaName, 2, 55)
    # SFG_SDG1032X_OuputWaveForm(StrVisaName, 1, "DC")
    # SFG_SDG1032X_ChannelOffset(StrVisaName, 2, 6)
    # SFG_SDG1032X_SetDcWave(StrVisaName, 1, 2)
    # SFG_SDG1032X_ChannelFrequency(StrVisaName, 1, 2e2)
    # SFG_SDG1032X_ChannelAmplitude(StrVisaName, 1, 1)
    # SFG_SDG1032X_ChannelPhase(StrVisaName, 1, 250)
    # SFG_SDG1032X_SetSineWave(StrVisaName, 1, 5e3, 5, 2, 100)

    # SFG_SDG1032X_ChannelDuty(StrVisaName, 1, 70)
    # SFG_SDG1032X_SetSquareWave(StrVisaName, 2, 300, 5, 2, 60, 95)

    # SFG_SDG1032X_ChannelSymmetry(StrVisaName, 1, 15)
    # SFG_SDG1032X_SetRampWave(StrVisaName, 1, 100, 5, 2, 100, 50)

    # SFG_SDG1032X_ChannelStdDev(StrVisaName, 1, 0.5)
    # SFG_SDG1032X_ChannelMean(StrVisaName, 1, 3)
    # SFG_SDG1032X_SetNoiseWave(StrVisaName, 2, 1, 2)

    # SFG_SDG1032X_ChannelPulseWidth(StrVisaName, 1, 100e-6)
    # SFG_SDG1032X_ChannelRiseEdge(StrVisaName, 1, 150-6)
    # SFG_SDG1032X_ChannelDelay(StrVisaName, 1, 150e-6)
    # SFG_SDG1032X_SetPulseWave(StrVisaName, 1, 200, 5, 1, 100e-6, 200e-6, 150e-6)