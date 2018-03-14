
# "Pedestrian Crossing" v0.1 by Tiny Fruit 2018

# This program is intended for use with the "Pedestrian Crossing"
# piece of hardware designed to fit ontop of a Raspberry Pi.

# The "Pedestrian Crossing" was designed and intended
# as a base for learning programming at a beginners level.

# The PCB will be available for download as well as purchase
# additional parts and soldering is required!

# The push button, the Buzzer and all the LEDs
# are connected to the GPIO as stated below!

# Pin 17 - A Large 10mm Red LED
# Pin 27 - A Large 10mm Yellow LED
# Pin 22 - A Large 10mm Green LED

# Pin 5  - An Active Buzzer

# Pin 6  - A Medium 5mm Red LED
# Pin 13 - A Medium 5mm Green LED
# Pin 19 - A Small 3mm White LED

# Pin 16 - A push Button switch

# Import some important stuff, such as GPIO and time
import RPi.GPIO as GPIO
import time

# The sequence for turning on and off the buzzer and all of the LED lights
def do_the_light_changing_sequence():
    
    # Light up the white light and make a short beep
    GPIO.output(buzzer_pin, GPIO.HIGH)
    GPIO.output(small_white, GPIO.HIGH)
            
    time.sleep(0.2 * delay_multiplicator)
    
    # Stop the buzzer from beeping
    GPIO.output(buzzer_pin, GPIO.LOW)
            
    time.sleep(0.5 * delay_multiplicator)
    
    # Swap the large green light for a large yellow
    GPIO.output(large_green, GPIO.LOW)
    GPIO.output(large_yellow, GPIO.HIGH)
    
    time.sleep(1 * delay_multiplicator)
    
    # Swap the large yellow light for a large red  
    GPIO.output(large_yellow, GPIO.LOW)
    GPIO.output(large_red, GPIO.HIGH)
    
    time.sleep(1 * delay_multiplicator)
    
    # Swap the medium red light for a the medium green
    # ...also turn of the small white light!
    GPIO.output(medium_red, GPIO.LOW)
    GPIO.output(medium_green, GPIO.HIGH)
    GPIO.output(small_white, GPIO.LOW)

    time.sleep(3 * delay_multiplicator)
    
    # Start flashing the medium green light
    # and make a short beep each time
    for i in range(1,10):
        
            GPIO.output(medium_green, GPIO.LOW)
            GPIO.output(buzzer_pin, GPIO.LOW)
            time.sleep(0.2)
            GPIO.output(medium_green, GPIO.HIGH)
            GPIO.output(buzzer_pin, GPIO.HIGH)
            time.sleep(0.2)
               
    # Swap the medium green light for the medium red 
    GPIO.output(medium_green, GPIO.LOW)
    GPIO.output(medium_red, GPIO.HIGH)
    
    time.sleep(1 * delay_multiplicator)
    
    # Turn of the Buzzer
    GPIO.output(buzzer_pin, GPIO.LOW)
    
    # Turn on the large yellow light
    GPIO.output(large_yellow, GPIO.HIGH)
    
    time.sleep(1 * delay_multiplicator)
    
    # Turn of both the large red and the large yellow light
    # and turn on the large green light
    GPIO.output(large_red, GPIO.LOW)
    GPIO.output(large_yellow, GPIO.LOW)
    GPIO.output(large_green, GPIO.HIGH)
    
    time.sleep(1 * delay_multiplicator)

                
    # Wait for a few seconds before leving this function
    # in order to prevent another button push to early on!
    time.sleep(5)


### START OF INIT ################################
    
# GPIO version check
print ("Curently using GPIO version:", GPIO.VERSION)

GPIO.setmode(GPIO.BCM)

# Set all LED output pins
large_red = 17
large_yellow = 27
large_green = 22
medium_red = 6
medium_green = 13
small_white = 19

# Store all LED pin outs in one variable
led_output_pins = large_red, large_yellow, large_green, medium_red, medium_green, small_white

# Set the push Button pin
button_pin = 26

# Set the Buzzer pin
buzzer_pin = 5

# Just checking the total number of LEDs
number_of_leds = len(led_output_pins)
print ("Number of LEDs:", number_of_leds)

# A general value to change the output speed
# If it is set to 1 = no slowdown
# If it is set to 3 = a slowdown by three times
delay_multiplicator = 3

### END OF INIT ##################################



# Prepare the led output pins
print ("Preparing outputs")
for i in range(0, number_of_leds):
    pin = led_output_pins[i]
    print (pin)
    GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

# Prepare the buzzer output pin
GPIO.setup(buzzer_pin, GPIO.OUT, initial=GPIO.LOW)

# Prepare the Button output pin
print ("Prepare the Button output pin")
GPIO.setup(button_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# wait for five looong seconds...
print ("Adding a short delay...")
time.sleep(1)

# This loop flashes all the LEDs and the Buzzer repeatedly
# a few times just to check out if they are all responding
print ("Like a flash in the pan...")
print ("...a repetitive but short function test for all of the LEDs and the Buzzer")

for j in range (1,5):
    
    GPIO.output(buzzer_pin, GPIO.HIGH)
       
    for i in range (0, number_of_leds):
        pin = led_output_pins[i]  
        GPIO.output(pin, GPIO.HIGH)

    time.sleep(0.1)
    
    GPIO.output(buzzer_pin, GPIO.LOW)
    
    time.sleep(0.1)

    GPIO.output(buzzer_pin, GPIO.HIGH)
    
    for i in range (0, number_of_leds):
        pin = led_output_pins[i]  
        GPIO.output(pin, GPIO.LOW)
  
    time.sleep(0.2)
    
    GPIO.output(buzzer_pin, GPIO.LOW)
    
    time.sleep(0.1)
    # End of the flash-pan

# Set the initial state of crossing lights
GPIO.output(medium_red, GPIO.HIGH)
GPIO.output(large_green, GPIO.HIGH)   

# Helps to keep track of the number of loops
loop_count = 0

# The main loop that makes it all happen
try:
    while True:
            
        read_input = GPIO.input(button_pin)
        
        if read_input == True:
            
            # Print a message every 100th loop (ie about 10 seconds inbetween)
            if loop_count % 100 == 0:
                
                # Print a blank line...
                print ("")
                
                print ("Loop count:", loop_count)
                print ("The input for pin number", button_pin ,"is:", read_input)
                print ("...still waiting for a push!")

        else:
            # Print a blank line...
            print ("")
            
            print ("Pin", button_pin, "is LOW!")
            print ("Let's do the full light sequence!")
            
            do_the_light_changing_sequence()

        # Keep track of the number of loops made so far...
        loop_count += 1
        
        # Add a short delay between each reading of the Button pin
        time.sleep(0.1)

# Makes a nice and clean exit when the program is interupted
except KeyboardInterrupt:
    print ("cleaning up and exiting")
    GPIO.cleanup()

