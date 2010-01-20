# Force Feedback Reality

<center><small>Originally posted on slashdong.org, July 31, 2007</small></center>

Slashdong started with me rewiring force feedback from an in-controller vibration motor to a sex toy. Now it's time to turn the tables: What if your current environment was causing the feedback? And more importantly, what if that feedback was routed to a toy and then taken to a large, outdoor BDSM fair for testing? Well, that's pretty much the story of my past week.

Now, I've been whining and complaining about interfaces since I started this site, but it's usually been software interfaces. For some reason that I'm not really sure of (probably the instant gratification of software versus hardware), I've never actually played with hardware interfaces to toys. I've got a couple of drawers full of robotics sensors that have been collecting dust for years, and [after the idea of the random board was floated][1], I started trying to figure out exactly how one could seed the random generation, and thus my sensors found use once again. This board doesn't actually implement the random generation quite yet; I'm still working on figuring out what I can do in the 900 bytes of memory I have left on the ATTiny13 I decided to use for this project. 

Note: I used an ATTiny13 specifically because it was the only 8 pin microcontroller I had around when I started this. You can get an ATTiny4x/8x for $1 more, which gives you MUCH more working room. So, unless $1 matters to your for production costs, I'd say go with something larger and avoid the challenge of "Oops, floating point math takes 2k of space!"

[![IMG_0160][2]][3]

This board is probably the simplest thing I've ever built that's still usable and coherent (The first SexBox was by far the simplest, but that was back in the heady days of "What do you mean I can't power 4 motors off a USB line?", so I dunno how usable _or_ coherent it was, really.) It has 2 ports, the usual 2.5mm mono jack for motors and a 3.5mm stereo jack for sensors (Stereo because you may need -/+/signal lines for some sensors). The board itself is powered by 2 AAA Batteries, giving it ~3v to operate the uC and run the motor on. 

The uC itself is running pure interrupt based code. The program sets up the PWM line and ADC, then simply moves the ADC value into the output match counter on every ADC read completion interrupt. No averaging, no smoothing, just pure, hard register bashing. However, the 3.5mm jack gives just a massive amount of extensibility. Now we can control those motor however we want. Well, however we want assuming it has an operating range of <= 3.0v (preferably less since there's no boost in the circuit) and enough variance to play well with no smoothing or input scaling.

In fact, here's the code:
    
    ISR(ADC_vect)
    {
    	OCR0A = ADC/4;
    }

    int main()
    {
    	DDRB = 0x1;
    	DIDR0 = 0b00100000;
    	TCCR0A = _BV(WGM01) | _BV(WGM00) | _BV(COM0A1);
    	TCCR0B = _BV(CS00);
    	ADCSRA = _BV(ADEN) | _BV(ADATE);
    	sei();
    	ADCSRA |= _BV(ADIE);
    	ADCSRA |= _BV(ADSC);
    	return 0;
    }

Yes, I realize there's an auto ADC shift option and no, I don't remember why I took it out.

So far, I've gotten 3 interfaces working: Knob, Touch, and Light

**Knob:** It's a potentiometer. This is pretty much just a physical interface to show off how everything else works. Turn knob, motor speed changes due to change in resistance between the signal and ground line. That's it. I'm not even gonna post pictures ('cause I forgot to take them)

[![IMG_0161][4]][5]

**Touch:** Touch is even simpler, but MUCH more interesting, depending on how it's built and triggered. This board is built specifically to be small; to fit in your pocket and taken out into public while still concealing well. Touch sensors can be placed to work as bump sensors, so that they'll trigger when walking through a crowd. 

[![IMG_0162][6]][7]

However, touch doesn't involve just buttons and levers, and this board may not usually be the only thing in your pocket. That's what the "antenna sensor" was built for. 

[![IMG_0165][8]][9]

Throw it in the same pocket at your keys, and suddenly you get a semi-random interface based on the combination of your walk structure and the placement of the keys/change/whatever else in your pocket (though there's also the question of tightness of pants effecting this, but we'll let, uh, I guess civil engineers deal with that. [They're good at that sort of thing][10]). 

[![IMG_0163][11]][12]

**Light:** Light has turned out to be quite a bit of fun, and gives almost a "random with context" type feel in its current incarnation. A light sensor is a resistor that's value decreases (and therefore current increases) as it gets nearer a light. Now, the light sensors I have are very sensitive. Taking them out in daylight will completely spike them which means you're either always on or always off, depending on how the board is set up. However, if you manage to have a decently sized pocket, you'll still get reflectance from the sun or other light sources, but with enough of an intensity drop-off to fit within the range of the sensor. 

[![IMG_0142][13]][14]

Once again, crowds become REALLY fun, because if you stand next to a moving line, you can pretty much be... "activated" by the shadow of every person walking by (Warning: Watch out where you do this. You never know where these shadows have been.). 

[![IMG_0137][15]][16]

At Dore Alley, I ended up calling it the "Dark Alley Detector" as the toy was accidentally wired to go off in the dark. Therefore, whenever the motor was going, you should be aware that you are in a dark place where more interesting things than a vibe motor could be happening. (I build slut superpowers!) In addition to this, light can work much the same way as touch, depending on where it's placed. In a large enough pocket (say, pants from the bargain rack at Hot Topic back when wearing anything above a 32" meant you were getting pant legs larger than the width of the waist...), while walking the pocket will open and close, causing light level changes and sorta picking up walking rhythm. Combine this with it being bumped open and closed by the rather tightly packed crowd, adding a level of randomness, and you realize that while it can be nice and beautiful and elegant, most of the time science has no god damn rhythm whatsoever. 

However, for things like clubs, this has much potential.

![][17]

**Rangefinder:** This is one that I haven't gotten working yet (due to the fact that this board does not yet supply enough power. Next version is a 9v run through a 7805, damnit!) is a rangefinder. This sensor returns a value scaled by the distance of things in front of it. With the ones I've got (Sharp GP2D12s), this distance can be anywhere between 8-30cm. In a crowd, this would be totally awesome.

There's many other sensors I'd like to get working with this board, but as a first version, this has been rather fun.

One of the most interesting aspects of this is sensory replacement (think Kevin Warwick/Steve Mann, except, you know, pervy). For situations involving medium to heavy bondage with sensory deprivation, senses can be replaced instead of deprived. If properly blindfolded/hooded, the light sensor can be used to detection of light, shadows, and with enough sensors, direction. How this is represented is an exercise for the reader, but I'm all for abstract ideas (i.e. direction maps to speeds of a certain motors somewhere while intensity maps to a electrostim unit elsewhere). In robotics this is known as "sensor fusion", and a bot is obviously programmed to aggregate all of its sensor values into something more meaningful than each sensors single value. However, since I've somehow turned this description/tutorial/story into a "so you want to be an evil bastard dom/me", I'll just run with this. I'm all about the idea of "thinking through endorphines". Same idea as movies like Cube/Saw/Any other flick involving life or death situations integrated with puzzles, except here we're worried about sexual interaction, not sharp things and internal organs interaction (unless you're doing a guro scene or something, I guess). Anyways, if you flood the brain with endorphines, it makes it awful hard to think. Give someone the basic pretext of the sensor setup and something they need to figure out about the environment to make something about it (for themselves) better, and watch the neural net go to work! Who needs code when you have brains to play with. 

Ok, I've got more sensors to make and a random board to work on. I'll chart this out on opendildonics.org sometime later this week and post info here after I do. 

   [1]: http://tacit.livejournal.com/214115.html
   [2]: http://farm2.static.flickr.com/1083/958114377_28b80448f5.jpg
   [3]: http://www.flickr.com/photos/qdot76367/958114377/ (Photo Sharing)
   [4]: http://farm2.static.flickr.com/1271/958115289_a2b6e1ce96.jpg
   [5]: http://www.flickr.com/photos/qdot76367/958115289/ (Photo Sharing)
   [6]: http://farm2.static.flickr.com/1288/958968328_fe08913cd0.jpg
   [7]: http://www.flickr.com/photos/qdot76367/958968328/ (Photo Sharing)
   [8]: http://farm2.static.flickr.com/1341/958119803_d21b854d9f.jpg
   [9]: http://www.flickr.com/photos/qdot76367/958119803/ (Photo Sharing)
   [10]: http://education.guardian.co.uk/egweekly/story/0,,1652498,00.html
   [11]: http://farm2.static.flickr.com/1121/958969142_7206136586.jpg
   [12]: http://www.flickr.com/photos/qdot76367/958969142/ (Photo Sharing)
   [13]: http://farm2.static.flickr.com/1196/957701885_355c34f436.jpg
   [14]: http://www.flickr.com/photos/qdot76367/957701885/ (Photo Sharing)
   [15]: http://farm2.static.flickr.com/1381/958541218_433cd4529e.jpg
   [16]: http://www.flickr.com/photos/qdot76367/958541218/ (Photo Sharing)
   [17]: http://images.nonpolynomial.com/slashdong.org/blog/gp2d12.gif

