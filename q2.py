# You're building a simulation of a Smart Home system where different smart devices 
# (like lights, fans, and ACs) can be controlled. Each device should have basic functionalities like turning on,
#  turning off, and showing the device status. However, the internal working (like power consumption logic
#   , cooling intensity, etc.) is hidden from the user.

# Requirements:
# 1) Create an abstract class SmartDevice with:

# a constructor to set the device name.
# an abstract method operate() to simulate device-specific behavior.
# a concrete method show_status() that prints whether the device is ON or OFF.

# 2) Implement the following concrete classes that inherit from SmartDevice:

# SmartLight: Turns on the light and sets brightness level (default 70%).
# SmartFan: Turns on the fan and sets speed (default medium).
# SmartAC: Turns on the AC and sets temperature (default 24°C).

# 3) Use encapsulation:

# All device states (is_on, brightness, speed, temperature) must be private.
# Provide appropriate getter/setter methods to access and modify these values safely.

# 4) Demonstrate the usage:

# Create at least one object of each type.
# Call operate() and show_status() on each.
# Attempt to directly modify private attributes (should not work).
# Use setters to change brightness/speed/temperature and display updated values via getters.

# Evaluation Criteria:

# Proper use of abstract classes and methods.
# Correct implementation of encapsulation using private members and getters/setters.
# Demonstration of polymorphism via the operate() method.
# Attempt to access private variables directly should raise an AttributeError.



from abc import ABC, abstractmethod

class SmartDevice(ABC):
    #abstract class representing a smart device
    def __init__(self, name):
        self._name = name  # Private attribute
        self._is_on = False

    @abstractmethod
    def operate(self):
        pass

    def show_status(self):
        #print whether smartdevice is on or off
        status = "ON" if self._is_on else "OFF"
        print(f"{self._name} is {status}")

class SmartLight(SmartDevice):
    #smart  light for adjustive brightness
    def __init__(self, name):
        super().__init__(name)
        self._brightness = 70  # default brightness

    def operate(self):
        self._is_on = not self._is_on
        print(f"{self._name} has been toggled. Brightness is {self._brightness}%")

    def set_brightness(self, level):
        #for brightness level
        if 0 <= level <= 100:
            self._brightness = level
        else:
            print("Invalid brightness level. Must be between 0 and 100.")

    def get_brightness(self):
        return self._brightness

class SmartFan(SmartDevice):
    #smart fan for adjestable speed
    def __init__(self, name):
        super().__init__(name)
        self._speed = "Medium"  # default speed

    def operate(self):
        self._is_on = not self._is_on
        print(f"{self._name} has been toggled. Speed is {self._speed}")

    def set_speed(self, level):
        if level in ["Low", "Medium", "High"]:
            self._speed = level
        else:
            print("Invalid speed level. Choose from Low, Medium, or High.")

    def get_speed(self):
        return self._speed

class SmartAC(SmartDevice):
    #smart AC for adjustable temperature
    def __init__(self, name):
        super().__init__(name)
        self._temperature = 24  # default temperature

    def operate(self):
        self._is_on = not self._is_on
        print(f"{self._name} has been toggled. Temperature is {self._temperature}°C")

    def set_temperature(self, temp):
        if 16 <= temp <= 30:
            self._temperature = temp
        else:
            print("Invalid temperature. Must be between 16 and 30°C.")

    def get_temperature(self):
        return self._temperature

# demonstration
light = SmartLight("Living Room Light")
fan = SmartFan("Bedroom Fan")
ac = SmartAC("Office AC")

# operating devices
light.operate()
fan.operate()
ac.operate()

# showing statuses
light.show_status()
fan.show_status()
ac.show_status()

# attempting direct modification (should fail)
try:
    light._brightness = 100  # This should not be allowed
except AttributeError as e:
    print("Error:", e)

# using setters and getters
light.set_brightness(85)
print(f"Updated brightness: {light.get_brightness()}%")

fan.set_speed("High")
print(f"Updated speed: {fan.get_speed()}")

ac.set_temperature(22)
print(f"Updated temperature: {ac.get_temperature()}°C")