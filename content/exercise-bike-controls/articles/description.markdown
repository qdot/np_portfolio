# Hooking up the Stamina 4700R Exercise Bike

<CENTER><SMALL>Originally posted on deathbots.com, May 2005</SMALL></CENTER>

![][1]

## Table of Contents

  1. [About the Bike][3]
  2. [How it (normally) works][4]
  3. [Bike meets Xport][5]
  4. [Getting time/distance info][6]
  5. [Increasing encoder frequency, the ghetto way][7]

<A NAME="1"></A>
## About the Bike 

I could just sum this section up in one phrase:
"$99 at WalMart" But, since I know I'm catering to a ridiculously technical
audience, I'll flesh out the inner working of the bike a little more.

![][9]

![][10] 

The Stamina 4700R Silent Magnetic Recumbent Exercise Bike is a sexy
little number that will have all the [insert opposite sex of reader,
or same sex, or whatever the hell you kids are into these days]
turning their heads from the second you get your big ol' ass on
it. Featuring multiple resistence levels through its silent "Magnetic
Resistance" feature (read: It's a screw with a magnet on it, for
christ sake) and a start of the art LCD display, you can wash those
pounds away in style on its "Match your crappy rental house carpet"
beige frame. Note: All the pictures in this article kind of suck,
because I could only get one pedal off of the bike, so I had to leave
the other side of the bike on. Sure, I could've gone and gotten a
wrench, but why do the job right in 3 minutes when you can half ass it
now...

<A NAME="2"></A>
## How it works 

Well, for those of you that read the intro post to this project,
you'll know that this all started when I discovered that there was a
simple two pin connector hooking the LCD info screen into the
mysterious inner workings of the bike. Yup, that's it right there. So
the spacing on those pins is just perfect for header! That means it's
easy to craft a connection to my development board of choice, the
[Charmed Labs Xport Board][12].

For this project, I also used the Xport Botball Controller, since it
already had digital ports on it, which means I didn't have to code up
the verilog myself. Anyways, I needed to figure out what was on the
other side of those pins. Out comes the screwdriver! I took the bike
apart, then left it for two weeks just to make The Woman angry. After
I'd gotten bitched at to clean up my mess and put the bike back
together enough times that I'd gotten sick of it, I finally got in and
figured out what was making this encoder tick (heh.).

![][13] 

Hey, that's a [Hall Sensor][14]! With only one magnet, too! My god,
those cheap bastards! Here's how it works, in basic terms. There's a magnet
attached to the wheel. When the magnet passes next to the wires, it creates a
voltage. When the voltage is created, the rising edge considered to be one
encoder tick, which activates the LCD screen if it's not already on. If it is
already on, it calculates the time between the current tick and the last tick
to tell you how fast you're going. So, every time the pedals on the bike make
one full revolution, the magnet is guarenteed to pass by the sensor at least
once. That's how it keeps distance and speed. Time is kept by an oscillator in
the circuit, and viola, there's your cheapo information device! Time to scrap
that piece of junk and put some REAL hardware on there. 

<A NAME="3"></A>
## Bike Meets Xport 

Now comes the easy part, hooking the bike up to the Xport to make sure
the sensor works! Here's the test code (most likely gibberish to anyone not
familiar with the Xport): 

    #include "gpioint.h"
    #include "textdisp.h"

    int main()
    {
            //Set up GPIO Object
            //For those not familiar with the Xport and XBC, GPIO is a way of 
            //setting up the I/O pins (on the Xport) or digital sensor ports 
            //(on the XBC/XRC) in software so that they can be either input 
            //or output, and so that they can fire interrupts on different
            //events (posedge, negedge, etc...). This means you can build 
            //simple I/O systems without having to build a new bitstream. Great
            //for simple testing setups.
            CGpioInt m_digitalSensors;

            //Set all GPIO pins (or in this case, digital ports) to input
            m_digitalSensors.m_dataDir = 0;

            while(1)
            {
                    //Print state of pins on every loop
                    printf("%04x\n", m_digitalSensors.m_data);
            }
            return 0;
    }
  
A converter was made to hook the bike sensor into the Xport. As can be
seen in the picture, this connector enjoys good music. 

![][15] 

Sure enough,0's on the screen when the magnet was far away, 1's when the magnet lined up
perpendicularly to the sensor! We have connection! 

<A NAME="4"></A>
## Getting time/distance info

Now that we know the Xport works with the bike, we want
to do the most basic of tests: Getting it to replicate what's going on in the
LCD readout. First off, we need to figure out the velocity of one full
revolution per second. Doing this by hand, I came up with around 11.2 mph.
However, it was fluctuating between 9.5 and 12, so the human factor was
foobaring the whole experiment. Time to replace people with good ol' trusty
electronics. All I needed to do was switch one of the digital inputs to output
on the XBC, set a clock to fire an interrupt every second, and I could get the
info I needed. Here's the code for that:

    //Contains Register Definitions
    #include "gba.h"
    //Contains Printf function for Xport
    #include "textdisp.h"
    //Contains GPIO accessors, explained in last code example
    #include "gpioint.h"
    //Contains the Interrupt Container for managing ISRs
    #include "intcont.h"
    //Contains the ISR interface 
    #include "iinterupt.h"

    class CReadoutTest : public IInterrupt
    {
            int m_count;
            CGpioInt m_digitalSensors;
    public:

            CReadoutTest(CInterruptCont &intCont)
            {	
                    //Set the first digital port to be output
                    m_digitalSensors.m_dataDir = 1;

                    //Register this with the interrupt vector 
                    //for GBA Timer 1, which is 4. 
                    intCont->Register(*this, 4);	
                    //Turn on the interrupt for GBA Timer 1
                    intCont->Unmask(4);

                    //Set the timer on, with interrupt on 
                    //overflow, and 1 tick every 64 ticks
                    //of the CPU clock
                    GBA_REG_TM1CNT = 0x00c1;

                    //Since we're on a 16Mhz CPU, running
                    //at 1 timer tick per 64 CPU ticks, a
                    //second progresses at 262192 timer 
                    //ticks. Since we want to have a 10hz 
                    //interrupt time, we just divide this by
                    //10 and set the GBA timer to overflow at 
                    //2^16 minus that number. This number is 
                    //reloaded automatically by the GBA on 
                    //every overflow, so we only have to set
                    //this once.
                    GBA_REG_TM1D = 0xffff - (262192/10);
            }
            ~CReadoutTest() {}

            void RunTest()
            {
                    while(1)
                    {
                            //Sit in this loop forever, printing out
                            //the output state of the pin we're testing
                            //on, just to make sure things are working
                            //correctly
                            printf("%d\n", m_digitalSensors.m_data);
                    }		
            }

            //Interrupt handling routine
            //Takes the interrupt vector that has 
            //been activated, just in case an object deals
            //with multiple interrupts
            virtual void Interrupt(int vector)
            {
                    ++m_count;
                    if(m_count == 10)
                    {
                            //We've waiting 1 second, so set the
                            //pin high
                            m_digitalSensors.m_data = 1;
                            m_count = 0;
                    }
                    else
                    {
                            //We're waiting, so set the pin low
                            m_digitalSensors.m_data = 0;
                    }
            }
    }

    int main()
    {
            CInterruptCont intCont;
            CReadoutTest test(intCont);
            test.RunTest();
            return 0;
    }


![][17] 

Well, I think the picture says it better than I could. I was pretty
far off. So, just out of sheer curiosity, I decided to see what wheel size the
bike was simulating. 

9.0 miles/hr at 1 tick (or full wheel revolution) per second. 

9mph * 5280f/m * 12i/f = 570240i/h / 3600s/h = 158.4i/s / pi = ~50.42 inch diameter wheel? 

I'm just going to assume a ~25in wheel at ~2:1 gear ratio. Yeah. 

## Increasing encoder frequency, the ghetto way 

So now we know that the bike will talk to the xport, and what speed we
need to calculate for using the bike, we're pretty much done in terms
of simulation.  But what about the important part, **games!** One tick
per rotation isn't going to be nearly enough to support control for a
game, as you really can't get higher than 2-3 ticks per second, and
that's if you're really working at it. So, we need to add more encoder
ticks to the system. How? More magnets!

![][19] 

Now, I've done some serious ghetto rigging on projects, but electrical
taping magnets to the flywheel of an already ghetto exercise bike? That's just
something special right there. You're going to need fairly strong magnets in
order to get this to work, due to the distance of the wheel from the sensor. I
went down to the local hardware store and get some ceramic magnets, shattered
them with a hammer (why I didn't take pictures of this, I don't know, 'cause
it was FREAKIN' AWESOME), and a taped them into the inside of the wheel. Soon,
I was getting 10 ticks per revolution instead of 1! Still not my ideal (I'd
love to have around 100 or so), but it works for the moment. 

That's it! This bike is ready to go!

   [1]: http://images.nonpolynomial.com/deathbots.com/projects/bike1/4700R.jpg
   [3]: #1
   [4]: #2
   [5]: #3
   [6]: #4
   [7]: #5
   [9]: http://images.nonpolynomial.com/deathbots.com/projects/bike1/bike1.jpg
   [10]: http://images.nonpolynomial.com/deathbots.com/projects/bike1/bike2.jpg
   [12]: http://www.charmedlabs.com
   [13]: http://images.nonpolynomial.com/deathbots.com/projects/bike1/sensor.jpg
   [14]: http://en.wikipedia.org/wiki/Hall_effect_sensor
   [15]: http://images.nonpolynomial.com/deathbots.com/projects/bike1/converter.jpg
   [17]: http://images.nonpolynomial.com/deathbots.com/projects/bike1/speedtest.jpg
   [19]: http://images.nonpolynomial.com/deathbots.com/projects/bike1/magnet.jpg

        
