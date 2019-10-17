def temperature(wartosc, temperature_type=""):
    if temperature_type=="Fahrenheit":
        return wartosc*1.8+32
    if temperature_type=="Rankine":
        return (wartosc+273.15)*1.8
    if temperature_type=="Kelvin":
        return wartosc+273.15


print(temperature(-20, "Fahrenheit"))
print(temperature(-20, "Rankine"))
print(temperature(-20, "Kelvin"))