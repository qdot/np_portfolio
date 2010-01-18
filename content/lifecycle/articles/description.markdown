1. [Building a Virtual Bicycle](#1)
2. [Overview of the Project](#2)
3. [Setting up the Bike](#3)
4. [Communicating with Second Life](#4)
5. [What to do with a Second Life Bicycle](#5)
6. [Plans for the Future](#6)

![Lifecycle Second Life Exhibit](http://images.nonpolynomial.com/nonpolynomial.com/projects/lifecycle/lifecycle1.jpg)
    
<A NAME="1"></A>
## Building a Virtual Bicycle
 
Second Life can be an incredibly immersive world, seeing that it is based solely on user created content. However, there is only so much immersion that can happen through a keyboard/mouse control scheme. There are many different ways to control vehicles in real life, such as steering wheels, pedals, handle bars, and sticks, just to name a few. Implementing these control structures in Second Life allows users to get closer to the virtual world by giving them mechanisms they are familiar with in the real world.
 
Biking is the first of these controls we have decided to implement, because it is so ubiquitous. The bicycle is used around the world for cheap, self-powered transportation, and has embedded itself into many interesting contextual situations. Romantic ideas such as biking through the park or using paddle boats, the thrill of the Tour De France, the metaphor of training wheels, are all based on bicycles. Using the LifeCycle, users will now be able to move themselves from place to place in the Second Life world using a stationary exercise bike.
 
<A NAME="2"></A>
## Overview of the Project
 
![Lifecycle Flow Description](http://images.nonpolynomial.com/nonpolynomial.com/projects/lifecycle/lifecycle5.jpg)
 
This project consists of four parts:
 
* Creating a sensor to relay bike speed
* Moving the information from the sensor to the computer thru serial communications
* Translating the sensor information on the computer and sending it to the Second Life Client
* Using the received data in Second Life to control speed
 
For this project we'll be using two major pieces of hardware (other than the computer)
 
![Stamina 4700R Exercise Bike](http://images.nonpolynomial.com/nonpolynomial.com/projects/lifecycle/lifecycle7.jpg)
 
* Stamina 4700R Silent Magnetic Recumbent Exercise Bike with LCD Status Readout
* [Xport Botball Controller](https://botballstore.org/catalog/product_info.php?cPath=25&products_id=52) - for sensor pickup and data transfer
 
Please note that this project could be easily done with a much cheaper microprocessor setup. The Xport is used because it's the platform I happen to be most familiar with.
 
<A NAME="3"></A>
## Setting up the Bike
 
The first thing we need to do is take apart the bike and figure out exactly how it relays speed information to the status LCD it came with.
 
On disassembly and inspection of the bike, it is discovered that all of the work is being done by around 2 cents worth of plastic and metal. Namely, a Hall Effect Sensor. 
 
![Exercise Bike Sensor](http://images.nonpolynomial.com/nonpolynomial.com/projects/lifecycle/lifecycle2.jpg)
 
A Hall Effect Sensor is a digital sensor (meaning it returns either an off or on state), depending on the magnetic field present in the area of the sensor. If a field perpendicular to the sensor is introduced, a small voltage is created, causing the sensor to return an activated (on) state. 
 
In terms of how this works in the bike, there is a magnet on the wheel, and a hall sensor screwed to the middle post. Whenever the magnet on the wheel passes the sensor, it is activated, which then tells the LCD screen to update. The screen powers on if it is currently off. If it is already on, it pulls the time from an oscillator in the circuit. It then compares the time between the current tick and the last tick in order to calculate distance traveled, speed, and calories burned. 

![Sensor Connection Wire](http://images.nonpolynomial.com/nonpolynomial.com/projects/lifecycle/lifecycle3.jpg)
 
Next, we needed to figure out the velocity produced by one revolution of the pedals in 1 second. To do this, a sensor adapter was created to make the LCD input header compatible with the Xport. After this adapter was made, the xport was programmed to send a pulse through the sensor port every second. 
 
![Test Bench Setup](http://images.nonpolynomial.com/nonpolynomial.com/projects/lifecycle/lifecycle4.jpg)
 
Using this method, the LCD readout showed 9 miles per hour, meaning that turning the pedals one full rotation once per second would give us a velocity of 9m/h. This data could be used to add physically correct velocity to the bike in the Second Life world. 
 
Observant readers will probably notice that I refer to the magnet on the wheel in the singular. There is only one magnet on the wheel, meaning the encoder will only register on every full turn of the pedals. This is an extremely low encoder resolution, so our speed control for this version will mainly consist of "go" and "stop" speeds. In the next version of the LifeCycle, we will cover ways to increase encoder resolution both with the hall sensor, and with other types of encoders. 
 
That being said, speed control in LifeCycle version 1 works as follows. When the encoder is triggered, a 2 second timer is started. Every time the encoder is triggered after that, the timer is reset to 2 seconds. If the 2 second timer runs out, the keystroke is set to up, and the bike is stopped. This means that the user needs to be aware of where the bike will be in 2 seconds. They are also required to keep a minimum speed of at least 4.5 miles per hour. Future versions of the project will make the Second Life Bike explode and throw the Av 10 sims over if they drop below this speed. 
 
<A NAME="4"></A> 
## Communicating with Second Life
 
To communicate with Second Life, we'll be using a specialized version of the [Hooky program](http://www.nonpolynomial.com/portfolio/hooky).   
 
The Xport sends the encoder counts to the machine 10 times a second. Hooky takes these values, translates them into keystroke lengths, and sends them to Second Life.  
 
According to the [Second Life LSL Wiki](http://secondlife.com/badgeo/wakka.php?wakka=LindenVehicleTutorial#AEN815) (Last paragraph of Definitions section), Vehicles can receive and process updates at around 10hz. Therefore, we set the duty cycle (length of time per keystroke) to 150ms, to make sure that our keystrokes will be out of phase with the input cycle (so that we won't have any sub-phase-length keystrokes). This means that if we want to set the vehicle to 60% of it's maximum speed with an according keystroke, the key will be set to a down state for 90ms, and then up for 60ms. Due to the way input interaction works with Second Life and system hooks, this will not be an incredibly accurate control method, but it's really the best that can be done under the circumstances. 
 
For the first version of this project, we will be using the bicycle to control the duty cycle of the "w" and "s" keys. Pedaling will only work as a speed controller. Since we are using a basic encoder instead of a quadrature encoder, we have no way to telling whether the user is pedaling forward or backward. Therefore, we will use a button on the controller to let the user signify which direction they want to go. Similarly, we have no way to control turning on the bike. Turning is taken care of through an analog stick on the controller. So, as the user pedals to control speed, he can use the joystick to navigate the world. 
 
<A NAME="5"></A>
## What to do with a Second Life Bicycle
 
![Lifecycle usage setup](http://images.nonpolynomial.com/nonpolynomial.com/projects/lifecycle/lifecycle8.jpg)
 
This method can be used to control almost any vehicle in Second Life, meaning you can bike using a bike, a car, a plane, a hamburger, a horse, or any other type of vehicle SL has to offer (of which there are a ridiculous number). However, there are many other interesting ideas that can be built with this. 
 
![Boat in Second Life](http://images.nonpolynomial.com/nonpolynomial.com/projects/lifecycle/lifecycle6.jpg)
 
For instance, assuming two users each had a LifeCycle setup, they could it to simultaniously control a vehicle, such as a paddle-boat or tandem bike. Using a paddle boat, the speed of each bike would also control the angular velocity.  
Other ideas: 
 
* Assuming multiple users had their bikes calibrated to the same speed output, bike races using real bikes would be feasable.
* Speed could control some sort of visual actuator on the avatar (i.e. pulse, glow, bling, etc...) in order to reflect that the user was working out while they played.
* Controling the height of a flying vehicle. Assuming prims could be generated fast enough and you had a whole sim to play in, this could be turned into a 3D Online Exercise Bike controlled version of <A HREF='http://www.sfcave.com/javaCave.php'>SFCave</A></LI></UL> 
 
<A NAME="6"></A>
## Plans for the Future
 
![Lifecycle in use](http://images.nonpolynomial.com/nonpolynomial.com/projects/lifecycle/lifecycle9.jpg)
 
Plans for future projects and additions using knowledge learned from this project include: 
 
* Handlebar turning interface for greater realism
* Combining bike with [Eyesore 3D Projection Project](http://www.nonpolynomial.com/portfolio/eyesore) to allow users to bike through a 3D Second Life
* Treadmill interface for walking locomotion in Second Life
* Creating a Second Life Fitness Actuator similar to the [G-Link](http://miolnir.co.uk/glink/), where avatar condition is dependant upon usage of control scheme
 
