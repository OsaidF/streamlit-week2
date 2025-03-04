import streamlit as st

class Conversion:
    def __init__(self, **kwargs):
        self.args = kwargs

class Types:
    def __init__(self, name, *args):
        self.name = name
        self.types = args

class Formulas:
    def __init__(self, **kwargs):
        self.attributes = kwargs
    
class Unit():
    def __init__(self, name, **kwargs):
        self.name = name
        self.formulas = Formulas(**kwargs)



# DEFINING UNIT TYPES IN LENGTH TYPE
Centimetre = Unit('Centimetre', Inch = '{0}/2.54', Foot= '{0}/30.48', Yard = '{0}/91.44', Mile = '{0}/160900', Nanometer = '{0}*1e+7', Micrometre = '{0}*10000', Millimetre = '{0}*10', Metre = '{0}/100', Killometre= '{0}/100000')
Metre = Unit('Metre', Inch = '{0}*39.37', Foot = '{0}*3.281', Yard = '{0}*1.094', Mile = '{0}/1609', Nanometer = '{0}*1e+9', Micrometer= '{0}*1e+6', Millimeter = '{0}*1000', Centimeter = '{0}*100', Kilometer= '{0}/1000' )
Kilometer = Unit('Kilometer', Inch = '{0}*3281', Foot = '{0}*39370', Yard = '{0}*1094', Mile = '{0}/1.609', Nanometer = '{0}*1e+12', Micrometer= '{0}*1e+9', Millimeter = '{0}*1e+6', Centimeter = '{0}*100000', Meter= '{0}*1000')
Millimeter = Unit('Millimeter', Inch = '{0}/25.4', Foot = '{0}/304.8', Yard = '{0}/914.4', Mile = '{0}/1.609e+6', Nanometer = '{0}*1e+6', Micrometer= '{0}*1000', Centimeter = '{0}/10', Meter= '{0}/1000', Kilometer= '{0}/1e+6')
Micrometer = Unit('Micrometer', Inch = '{0}/25400', Foot = '{0}/304800', Yard = '{0}/914400', Mile = '{0}/1.609e+9', Nanometer = '{0}*1000', Millimeter= '{0}/1000', Centimeter = '{0}/10000', Meter= '{0}/1e+6', Kilometer= '{0}/1e+9')
Nanometer = Unit('Nanometer', Inch = '{0}/2.54e+7', Foot = '{0}/3.048e+8', Yard = '{0}/9.144e+8', Mile = '{0}/1.609e+12', Micrometer = '{0}/1000', Millimeter= '{0}/1e+6', Centimeter = '{0}/1e+7', Meter= '{0}/1e+9', Kilometer= '{0}/1e+12')
Mile = Unit('Mile', Inch = '{0}*63360', Foot = '{0}*5280', Yard = '{0}*1760', Nanometer = '{0}*1.609e+12', Micrometer = '{0}*1.609e+9', Millimeter= '{0}*1.609e+6', Centimeter = '{0}*160900', Meter= '{0}*1609', Kilometer= '{0}*1.609')
Yard = Unit('Yard', Inch = '{0}*36', Foot = '{0}*3', Mile = '{0}/1760', Nanometer = '{0}*9.144e+8', Micrometer = '{0}*914400', Millimeter= '{0}*914.4', Centimeter = '{0}*91.44', Meter= '{0}/1.094', Kilometer= '{0}/1094')
Foot = Unit('Foot', Inch = '{0}*12', Yard = '{0}/3', Mile = '{0}/5280', Nanometer = '{0}*3.048e+8', Micrometer = '{0}*304800', Millimeter= '{0}*304.8', Centimeter = '{0}*30.48', Meter= '{0}/3.281', Kilometer= '{0}/3281')
Inch = Unit('Inch', Foot = '{0}/12', Yard = '{0}/36', Mile = '{0}/63360', Nanometer = '{0}*2.54e+7', Micrometer = '{0}*25400', Millimeter= '{0}*25.4', Centimeter = '{0}*2.54', Meter= '{0}/39.37', Kilometer= '{0}/39370')
# ASSIGNING UNITS TO LENGTH TYPE
Length = Types('Length', Centimetre, Metre, Kilometer, Millimeter, Micrometer, Nanometer, Mile, Yard, Foot, Inch)

# DEFINING UNIT TYPES IN AREA TYPE
Square_Kilometre = Unit('Square Kilometre', Square_Metre = '{0}*1e+6', Square_Mile = '{0}/2.59', Square_Yard = '{0}*1.196e+6', Square_Foot = '{0}*1.076e+7', Square_Inch = '{0}*1.55e+9', Hectare = '{0}*100', Acre = '{0}*247.1')
Square_Metre = Unit('Square Metre', Square_Kilometer = '{0}/1e+6', Square_Mile = '{0}/2.59e+6', Square_Yard = '{0}*1.196', Sqaure_Foot = '{0}*10.764', Sqaure_Inch = '{0}*1550', Hectare = '{0}/10000', Acre = '{0}/4047' )
Square_Mile = Unit('Square Mile', Square_Kilometer = '{0}*2.59', Square_Metre = '{0}*2.59e+6', Square_Yard = '{0}*3.098e+6', Sqaure_Foot = '{0}*2.788e+7', Sqaure_Inch = '{0}*4.014e+9', Hectare = '{0}*259', Acre = '{0}*640')
Square_Yard = Unit('Square Yard', Square_Kilometer = '{0}/1.196e+6', Square_Metre = '{0}/1.196', Square_Mile = '{0}/3.098e+6', Sqaure_Foot = '{0}*9', Sqaure_Inch = '{0}*1296', Hectare = '{0}/11960', Acre = '{0}/4840')
Square_Foot = Unit('Square Foot', Square_Kilometer = '{0}/1.076e+7', Square_Metre = '{0}/10.764', Square_Mile = '{0}/2.788e+7', Square_Yard = '{0}/9', Sqaure_Inch = '{0}*144', Hectare = '{0}/107600', Acre = '{0}/43560')
Square_Inch = Unit('Square Inch', Square_Kilometer = '{0}/1.55e+9', Square_Metre = '{0}/1550', Square_Mile = '{0}/4.014e+9', Square_Yard = '{0}/1296', Sqaure_Foot = '{0}/144', Hectare = '{0}/1.55e+7', Acre = '{0}/6.273e+6')
Hectare = Unit('Hectare', Square_Kilometer = '{0}/100', Square_Metre = '{0}*10000', Square_Mile = '{0}/259', Square_Yard = '{0}*11960', Sqaure_Foot = '{0}*107600', Square_Inch = '{0}*1.55e+7', Acre = '{0}*2.471')
Acre = Unit('Acre', Square_Kilometer = '{0}/247.1', Square_Metre = '{0}*4047', Square_Mile = '{0}/640', Square_Yard = '{0}*4840', Sqaure_Foot = '{0}*43560', Square_Inch = '{0}*6.273e+6', Hectare = '{0}/2.471')
# ASSIGNING UNITS TO AREA TYPE
Area = Types('Area', Square_Kilometre, Square_Metre, Square_Mile, Square_Yard, Square_Foot, Square_Foot, Hectare, Acre)

# DEFINING UNIT TYPES IN DATA TRANSFER RATE TYPE
Bit_Per_Second = Unit('Bit Per Second', Kilobit_Per_Second = '{0}/1000', Kilobyte_Per_Second = '{0}/8000', Kibibit_Per_Second = '{0}/1024', Megabit_Per_Second = '{0}/1e+6', Megabyte_Per_Second = '{0}/8e+6', Mebibit_Per_Second = '{0}/1.049e+6', Gigabit_Per_Second = '{0}/1e+9', Gigabyte_Per_Second = '{0}/8e+9', Gibibit_Per_Second = '{0}/1.074e+9', Terabit_Per_Second = '{0}/1e+12', Terabyte_Per_Second = '{0}/8e+12', Tebibit_Per_Second = '{0}/1.1e+12')
Kilobit_Per_Second = Unit('Kilobit Per Second', Bit_Per_Second = '{0}*1000', Kilobyte_Per_Second = '{0}/8', Kibibit_Per_Second = '{0}/1.024', Megabit_Per_Second = '{0}/1000', Megabyte_Per_Second = '{0}/8000', Mebibit_Per_Second = '{0}/1049', Gigabit_Per_Second = '{0}/1e+6', Gigabyte_Per_Second = '{0}/8e+6', Gibibit_Per_Second = '{0}/1.074e+6', Terabit_Per_Second = '{0}/1e+9', Terabyte_Per_Second = '{0}/8e+9', Tebibit_Per_Second = '{0}/1.1e+9')
Kilobye_Per_Second = Unit('Kilobyte Per Second', Bit_Per_Second = '{0}*8000', Kilobit_Per_Second = '{0}*8', Kibibit_Per_Second = '{0}*7.812', Megabit_Per_Second = '{0}/125', Megabyte_Per_Second = '{0}/1000', Mebibit_Per_Second = '{0}/131.1', Gigabit_Per_Second = '{0}/125000', Gigabyte_Per_Second = '{0}/1e+6', Gibibit_Per_Second = '{0}/134200', Terabit_Per_Second = '{0}/1.25e+8', Terabyte_Per_Second = '{0}/1e+9', Tebibit_Per_Second = '{0}/1.374e+8')
Kibibit_Per_Second = Unit('Kibibit Per Second', Bit_Per_Second = '{0}*1024', Kilobit_Per_Second = '{0}*1.024',  Kilobyte_Per_Second = '{0}*7.812', Megabit_Per_Second = '{0}/976.6', Megabyte_Per_Second = '{0}/7813', Mebibit_Per_Second = '{0}/1024', Gigabit_Per_Second = '{0}/976600', Gigabyte_Per_Second = '{0}/7.813e+6', Gibibit_Per_Second = '{0}/1.049e+6', Terabit_Per_Second = '{0}/9.766e+8', Terabyte_Per_Second = '{0}/7.813e+9', Tebibit_Per_Second = '{0}/1.074e+9')
Megabit_Per_Second = Unit('Megabit Per Second', Bit_Per_Second = '{0}*1e+6', Kilobit_Per_Second = '{0}*1000',  Kilobyte_Per_Second = '{0}*125', Kibibit_Per_Second = '{0}*976.6', Megabyte_Per_Second = '{0}/8', Mebibit_Per_Second = '{0}/1.049', Gigabit_Per_Second = '{0}/1000', Gigabyte_Per_Second = '{0}/8000', Gibibit_Per_Second = '{0}/1074', Terabit_Per_Second = '{0}/1e+6', Terabyte_Per_Second = '{0}/8e+6', Tebibit_Per_Second = '{0}/1.1e+6')
Megabyte_Per_Second = Unit('Megabyte Per Second', Bit_Per_Second = '{0}*8e+6', Kilobit_Per_Second = '{0}*8000',  Kilobyte_Per_Second = '{0}*1000', Kibibit_Per_Second = '{0}*7812.5', Megabit_Per_Second = '{0}*8', Mebibit_Per_Second = '{0}*7.629', Gigabit_Per_Second = '{0}/125', Gigabyte_Per_Second = '{0}/1000', Gibibit_Per_Second = '{0}/134.2', Terabit_Per_Second = '{0}/125000', Terabyte_Per_Second = '{0}/1e+6', Tebibit_Per_Second = '{0}/137400')
Mebibit_Per_Second = Unit('Mebibit Per Second', Bit_Per_Second = '{0}*1.049e+6', Kilobit_Per_Second = '{0}*1049',  Kilobyte_Per_Second = '{0}*131.1', Kibibit_Per_Second = '{0}*1024', Megabit_Per_Second = '{0}*1.049', Megabyte_Per_Second = '{0}/7.629', Gigabit_Per_Second = '{0}/953.7', Gigabyte_Per_Second = '{0}/7629', Gibibit_Per_Second = '{0}/1024', Terabit_Per_Second = '{0}/953700', Terabyte_Per_Second = '{0}/7.629e+6', Tebibit_Per_Second = '{0}/1.049e+6')
Gigabit_Per_Second = Unit('Gagabit Per Second', Bit_Per_Second = '{0}*1e+9', Kilobit_Per_Second = '{0}*1e+6',  Kilobyte_Per_Second = '{0}*125000', Kibibit_Per_Second = '{0}*976600', Megabit_Per_Second = '{0}*1000', Megabyte_Per_Second = '{0}*125', Mebibit_Per_Second = '{0}*953.7', Gigabyte_Per_Second = '{0}/8', Gibibit_Per_Second = '{0}/1.074', Terabit_Per_Second = '{0}/1000', Terabyte_Per_Second = '{0}/8000', Tebibit_Per_Second = '{0}/1100')
Gigabyte_Per_Second = Unit('Gigabyte Per Second', Bit_Per_Second = '{0}*8e+9', Kilobit_Per_Second = '{0}*8e+6',  Kilobyte_Per_Second = '{0}*1e+6', Kibibit_Per_Second = '{0}*7.813e+6', Megabit_Per_Second = '{0}*8000', Megabyte_Per_Second = '{0}*1000', Mebibit_Per_Second = '{0}*7629', Gigabit_Per_Second = '{0}*8', Gibibit_Per_Second = '{0}*7.451', Terabit_Per_Second = '{0}/125', Terabyte_Per_Second = '{0}/1000', Tebibit_Per_Second = '{0}/137.4')
Gibibit_Per_Second = Unit('Gibibit Per Second', Bit_Per_Second = '{0}*1.074e+9', Kilobit_Per_Second = '{0}*1.074e+6',  Kilobyte_Per_Second = '{0}*134200', Kibibit_Per_Second = '{0}*1.049e+6', Megabit_Per_Second = '{0}*1074', Megabyte_Per_Second = '{0}*134.2', Mebibit_Per_Second = '{0}*1024', Gigabit_Per_Second = '{0}*1.074', Gigabyte_Per_Second = '{0}/7.451', Terabit_Per_Second = '{0}/931.3', Terabyte_Per_Second = '{0}/7451', Tebibit_Per_Second = '{0}/1024')
Terabit_Per_Second = Unit('Terabit Per Second', Bit_Per_Second = '{0}*1e+12', Kilobit_Per_Second = '{0}*1e+9',  Kilobyte_Per_Second = '{0}*1.25e+8', Kibibit_Per_Second = '{0}*9.766e+8', Megabit_Per_Second = '{0}*1e+6', Megabyte_Per_Second = '{0}*125000', Mebibit_Per_Second = '{0}*953700', Gigabit_Per_Second = '{0}*1000', Gigabyte_Per_Second = '{0}*125', Gibibit_Per_Second = '{0}*931.3', Terabyte_Per_Second = '{0}/8', Tebibit_Per_Second = '{0}/1.1')
Terabyte_Per_Second = Unit('Terabyte Per Second', Bit_Per_Second = '{0}*8e+12', Kilobit_Per_Second = '{0}*8e+9',  Kilobyte_Per_Second = '{0}*1e+9', Kibibit_Per_Second = '{0}*7.813e+9', Megabit_Per_Second = '{0}*8e+6', Megabyte_Per_Second = '{0}*1e+6', Mebibit_Per_Second = '{0}*7.629e+6', Gigabit_Per_Second = '{0}*8000', Gigabyte_Per_Second = '{0}*1000', Gibibit_Per_Second = '{0}*7451', Terabit_Per_Second = '{0}*8', Tebibit_Per_Second = '{0}*7.276')
Tebibit_Per_Second = Unit('Tebibit Per Second', Bit_Per_Second = '{0}*1.1e+12', Kilobit_Per_Second = '{0}*1.1e+9',  Kilobyte_Per_Second = '{0}*1.374e+8', Kibibit_Per_Second = '{0}*1.074e+9', Megabit_Per_Second = '{0}*1.1e+6', Megabyte_Per_Second = '{0}*137400', Mebibit_Per_Second = '{0}*1.049e+6', Gigabit_Per_Second = '{0}*1100', Gigabyte_Per_Second = '{0}*137.4', Gibibit_Per_Second = '{0}*1024', Terabit_Per_Second = '{0}*1.1', Terabyte_Per_Second = '{0}/7.276')
# ASSIGNING UNITS TO DATA TRANSFER RATE TYPE
Data_Transfer_Rate = Types('Digital Transfer Rate', Bit_Per_Second, Kilobit_Per_Second, Kilobye_Per_Second, Kibibit_Per_Second, Megabit_Per_Second, Megabyte_Per_Second, Mebibit_Per_Second, Gigabit_Per_Second, Gigabyte_Per_Second, Gibibit_Per_Second, Terabit_Per_Second, Terabyte_Per_Second, Tebibit_Per_Second)

# DEFINING UNIT TYPES IN TEMPERATURE TYPE
Celcius = Unit('Celcius', Kelvin = '{0}+273.15', Fahrenheit = '{0}*9/5 + 32')
Kelvin = Unit('Kelvin', Celcius = '{0}-273.15', Fahrenheit = '{0}-273.15*9/5+32')
Fahrenheit = Unit('Fahrenheit', Celcius = '({0}- 32) * 5/9', Kelvin = '{0} -32 * 5/9 + 273.15')
# ASSIGNING UNITS TO TEMPERATURE TYPE
Temperature = Types('Temperature', Celcius, Kelvin, Fahrenheit)


# DEFINING UNIT TYPES IN ENERGY TYPE
Joule = Unit('Joule', Kilojoule = '{0}/1000', Gram_Calorie = '{0}/4.184', Kilocalorie = '{0}/4184', Watt_Hour = '{0}/3600', Killowatt_Hour = '{0}/3.6e+6', Electronvolt = '{0}*6.242e+18', British_Thermal_Unit = '{0}/1055', US_Therm = '{0}/1.055e+8', Foot_Pound = '{0}/1.356')
Kilojoule = Unit('Kilojoule', Joule = '{0}*1000', Gram_Calorie = '{0}*239', Kilocalorie = '{0}/4.184', Watt_Hour = '{0}/3.6', Killowatt_Hour = '{0}/3600', Electronvolt = '{0}*6.242e+21', British_Thermal_Unit = '{0}/1.055', US_Therm = '{0}/105500', Foot_Pound = '{0}*737.6')
Gram_Calorie = Unit('Gram Calorie', Joule = '{0}*4.184', Kilojoule = '{0}/239', Kilocalorie = '{0}/1000', Watt_Hour = '{0}/860.4', Killowatt_Hour = '{0}/860400', Electronvolt = '{0}*2.611e+19', British_Thermal_Unit = '{0}/252.2', US_Therm = '{0}/2.521e+7', Foot_Pound = '{0}*3.086')
Kilocalorie = Unit('Kilocalorie', Joule = '{0}*4184', Kilojoule = '{0}*4.184', Gram_Calorie = '{0}*1000', Watt_Hour = '{0}*1.162', Killowatt_Hour = '{0}/860.4', Electronvolt = '{0}*2.611e+22', British_Thermal_Unit = '{0}*3.966', US_Therm = '{0}/25210', Foot_Pound = '{0}*3086')
Watt_Hour = Unit('Watt Hour', Joule = '{0}*3600', Kilojoule = '{0}*3.6', Gram_Calorie = '{0}*860.4', Kilocalorie = '{0}/1.162', Killowatt_Hour = '{0}/1000', Electronvolt = '{0}*2.247e+22', British_Thermal_Unit = '{0}*3.412', US_Therm = '{0}/29300', Foot_Pound = '{0}*2655')
Kilowatt_Hour = Unit('Kilowatt Hour', Joule = '{0}*3.6e+6', Kilojoule = '{0}*3600', Gram_Calorie = '{0}*860400', Kilocalorie = '{0}*860.4', Watt_Hour = '{0}*1000', Electronvolt = '{0}*2.247e+25', British_Thermal_Unit = '{0}*3412', US_Therm = '{0}/29.3', Foot_Pound = '{0}*2.655e+6')
Electronvolt = Unit('Electronvolt', Joule = '{0}/6.242e+18', Kilojoule = '{0}/6.242e+21', Gram_Calorie = '{0}/2.611e+19', Kilocalorie = '{0}/2.611e+22', Watt_Hour = '{0}/2.247e+22', Kilowatt_Hour = '{0}/2.247e+25', British_Thermal_Unit = '{0}/6.585e+21', US_Therm = '{0}/6.584e+26', Foot_Pound = '{0}/8.462e+18')
British_Thermal_Unit = Unit('British Thermal Unit', Joule = '{0}*1055', Kilojoule = '{0}*1.055', Gram_Calorie = '{0}*252.2', Kilocalorie = '{0}/3.966', Watt_Hour = '{0}/3.412', Kilowatt_Hour = '{0}/3412', Electronvolt = '{0}*6.585e+21', US_Therm = '{0}/99980', Foot_Pound = '{0}*778.2')
US_Therm = Unit('US Therm', Joule = '{0}*1.055e+8', Kilojoule = '{0}*105500', Gram_Calorie = '{0}*2.521e+7', Kilocalorie = '{0}*25210', Watt_Hour = '{0}*29300', Kilowatt_Hour = '{0}*29.3', Electronvolt = '{0}*6.584e+26', British_Thermal_Unit = '{0}*99980', Foot_Pound = '{0}*7.78e+7')
Foot_Pound = Unit('Foot Pound', Joule = '{0}*1.356', Kilojoule = '{0}/737.6', Gram_Calorie = '{0}/3.086', Kilocalorie = '{0}/3086', Watt_Hour = '{0}/2655', Kilowatt_Hour = '{0}/2.655e+6', Electronvolt = '{0}*8.462e+18', British_Thermal_Unit = '{0}/778.2', US_Therm = '{0}/7.78e+7')
# ASSIGNING UNITS TO TEMPERATURE TYPE
Energy = Types('Energy', Joule, Kilojoule, Gram_Calorie, Kilocalorie, Watt_Hour, Kilowatt_Hour, Electronvolt, British_Thermal_Unit, US_Therm, Foot_Pound)

# DEFINING UNIT TYPES IN MASS TYPE
Kilogram = Unit('Kilogram', Tonne = '{0}/1000', Gram = '{0}*1000', Milligram = '{0}*1e+6', Microgram = '{0}*1e+9', Imperial_Ton = '{0}/1016', US_Ton = '{0}/907.2', Stone = '{0}/6.35', Pound = '{0}*2.205', Ounce = '{0}*35.274')
Tonne = Unit('Kilogram', Gram = '{0}*1e+6', Kilogram = '{0}*1000', Milligram = '{0}*1e+9', Microgram = '{0}*1e+12', Imperial_Ton = '{0}/1.016', US_Ton = '{0}*1.102', Stone = '{0}*157.5', Pound = '{0}*2205', Ounce = '{0}*35270')
Gram = Unit('Kilogram', Tonne = '{0}/1e+6', Kilogram = '{0}/1000', Milligram = '{0}*1000', Microgram = '{0}*1e+6', Imperial_Ton = '{0}/1.016e+6', US_Ton = '{0}/907200', Stone = '{0}/6350', Pound = '{0}/453.6', Ounce = '{0}/28.35')
Milligram = Unit('Kilogram', Tonne = '{0}/1e+9', Kilogram = '{0}/1e+6', Gram = '{0}/1000', Microgram = '{0}*1000', Imperial_Ton = '{0}/1.016e+9', US_Ton = '{0}/9.072e+8', Stone = '{0}/6.35e+6', Pound = '{0}/453600', Ounce = '{0}/28350')
Microgram = Unit('Kilogram', Tonne = '{0}/1e+12', Gram = '{0}/1e+6', Kilogram = '{0}/1e+9', Milligram = '{0}/1000', Imperial_Ton = '{0}/1.016e+12', US_Ton = '{0}/9.072e+11', Stone = '{0}/6.35e+9', Pound = '{0}/4.536e+8', Ounce = '{0}/2.835e+7')
Imperial_Ton = Unit('Kilogram', Tonne = '{0}*1.016', Gram = '{0}*1.016e+6', Kilogram = '{0}*1016', Milligram = '{0}*1.016e+9', Microgram = '{0}*1.016e+12', US_Ton = '{0}*1.12', Stone = '{0}*160', Pound = '{0}*2240', Ounce = '{0}*35840')
US_Ton = Unit('Kilogram', Tonne = '{0}/1.102', Gram = '{0}*907200', Kilogram = '{0}*907.2', Milligram = '{0}*9.072e+8', Microgram = '{0}*9.072e+11', Imperial_Ton = '{0}/1.12', Stone = '{0}*142.9', Pound = '{0}*2000', Ounce = '{0}*32000')
Stone = Unit('Kilogram', Tonne = '{0}/157.5', Gram = '{0}*6350', Kilogram = '{0}*6.35', Milligram = '{0}*6.35e+6', Microgram = '{0}*6.35e+9', Imperial_Ton = '{0}/160', US_Ton = '{0}/142.9', Pound = '{0} *14', Ounce = '{0}*224')
Pound = Unit('Kilogram', Tonne = '{0}/2205', Gram = '{0}*453.6', Kilogram = '{0}*2.205', Milligram = '{0}*453600', Microgram = '{0}*4.536e+8', Imperial_Ton = '{0}/2240', US_Ton = '{0}/2000', Stone = '{0}/14', Ounce = '{0}*16')
Ounce = Unit('Kilogram', Tonne = '{0}/35270', Gram = '{0}*28.35', Kilogram = '{0}/35.274', Milligram = '{0}*28350', Microgram = '{0}*2.835e+7', Imperial_Ton = '{0}/35840', US_Ton = '{0}/32000', Stone = '{0}/224', Pound = '{0}/16')
# ASSIGNING UNITS TO MASS TYPE
Mass = Types('Mass', Kilogram, Tonne, Gram, Milligram, Microgram, Imperial_Ton, US_Ton, Stone, Pound, Ounce)

# DEFINING UNIT TYPES IN FREQUENCY TYPE
Hertz = Unit('Hertz', Kilohertz = '{0}/1000', Megahertz = '{0}/1e+6', Gigahertz = '{0}/1e+9')
Kilohertz = Unit('Kilohertz',  Hertz = '{0}*1000', Megahertz = '{0}/1000', Gigahertz = '{0}/1e+6')
Megahertz = Unit('Megahertz',  Hertz = '{0}*1e+6', Kilohertz = '{0}*1000', Gigahertz = '{0}/1000')
Gigahertz = Unit('Gigahertz',Hertz = '{0}*1e+9',  Kilohertz = '{0}*1e+6', Megahertz = '{0}*1000')
# ASSIGNING UNITS TO FREQUENCY TYPE
Frequency = Types('Frequency', Hertz, Kilohertz, Megahertz, Gigahertz)

# DEFINING UNIT TYPES IN FUEL ECONOMY TYPE
Kilometer_Per_Liter = Unit('Kilometer Per Liter', Mile_Per_US_Gallon = '{0}*2.352', Mile_Per_Gallon = '{0}*2.825', Liter_Per_100_Kilometers = '282.481/({0}) ')
Mile_Per_US_Gallon = Unit('Mile Per US Gallon', Kilometer_Per_Liter = '{0}/2.352', Mile_Per_Gallon = '{0}*1.201', Liter_Per_100_Kilometers = '235.215/({0})')
Mile_Per_Gallon = Unit('Mile Per Gallon', Kilometer_Per_Liter = '{0}/2.825', Mile_Per_US_Gallon = '{0}/1.201', Liter_Per_100_Kilometers = '282.481/({0})')
Liter_Per_100_Kilometers = Unit('Liter Per 100 Kilometers', Kilometer_Per_Liter = '100/({0})', Mile_Per_US_Gallon = '235.215/({0})', Mile_Per_Gallon = '282.481/({0})')
# ASSIGNING UNITS TO FUEL ECONOMY TYPE
Fuel_Economy = Types('Fuel Economy', Kilometer_Per_Liter, Mile_Per_Gallon, Mile_Per_US_Gallon, Liter_Per_100_Kilometers)

# DEFINING UNIT TYPES IN PLANE ANGLE TYPE
Degree = Unit('Degree', )
# ASSIGNING UNITS TO PLANE ANGLE TYPE
Plane_Angle = Types('Plane Angel', )

# DEFINING CONVERSION TYPES
Conversion_List = Conversion(Length = Length, Area = Area, Data_Transfer_Rate = Data_Transfer_Rate, Temperature = Temperature, Energy = Energy, Mass = Mass, Frequency = Frequency, Fuel_Economy = Fuel_Economy)


st.header(":scales: Unit Converter _by :red[Osaid]_ ")

type = st.selectbox(
        "Select a unit type group:",
        (list(Conversion_List.args.keys())),
        index=0,
        key=1212,
        placeholder="select a unit",
    )

# GETTING THE TYPE INPUT VALUE FROM SLECTBOX INPUT EG:- AREA, LENGTH, TEMPERATURE ETC. 
# AND RETURNING THE UNITS ASSOCIATED WITH THAT TYPE
getType = Conversion_List.args[type]

col1, col2 = st.columns(2)
# MAPPING THE UNITS FOR THE SELECTED TYPE IN THIS SELECTBOX
with col1:
    unit1 = st.selectbox(
        "Select a unit for the conversion",
        (list(map(lambda p: p.name, getType.types))),
        index=0,
        placeholder="select a unit",
    )

# GETTING THE VALUE YOU WANT TO CONVERT
with col2:
    quantity =  st.number_input(
        "Quantity", value=1, placeholder="Type a number..."
    )


# GETTING THE FORMULAS FOR THE SELECTED UNIT AND REMOVING UNDERSCORE FROM THEIR NAME
getUnit = next((p for p in getType.types if p.name == unit1), None)
List = {k.replace( '_', ' '): v for k, v in getUnit.formulas.attributes.items()}


# MAPPING THE FORMULAS (THE CONVERTIBLE UNITS) IN THE SELECTBOX
unit2 = st.selectbox(
        "Select A Unit To Convert To",
        (List),
        key=2,
        index=0,
        placeholder="select a unit",
    )

# Adding underscore back
addUnderscore = unit2.replace(' ', '_')

# ADDING SUBSTRING IN THE FORMULA STRING TO COMPLETE THE FORMULA
output = getUnit.formulas.attributes[addUnderscore].format(quantity)

# FORMATTING THE NUMBER TO LIMIT TO JUST TWO DECIMAL PLACES

final = format(round(eval(output), 2))


st.header(f"{quantity} {unit1} = {final} {unit2}")
st.caption(f"Exact value: {eval(output)} {unit2}")


