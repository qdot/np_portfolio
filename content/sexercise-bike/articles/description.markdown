# SEXERCISE - IT'S SEXILLENT!

<CENTER><small>Originally posted on [slashdong.org][13] on May 16, 2005</small></CENTER>

## Table of Contents

  1. [Worst Project Name Ever][2]
  2. [Project Description (Or: Damn we love stealing)][3]
  3. [How it works][4]
  4. [Why this will revolutionize exercise][5]
  5. [Movies!][6]

![][7] 

## Worst Project Name Ever

SEXCUSE ME!

Oh come the hell on. Like I could resist that shit. I was just as much of a
Gwar fan as anyone else who's ever been 15 while Gwar has been around, and
there ain't no way I'm gonna diss on the Sexecutioner. Can't wait to see them
on the [Sounds of the Underground tour][8] this year. TULSA IN JULY, BABY!
STRAPPING YOUNG MOTHERFUCKING LAD!

Ok, I'm done.

## Project Description (Or: Damn we love stealing)

The wonderful thing about running a network of sites is that if one site does
something cool, there's a damn good chance another site can steal recycle
content from another site, just changing one small thing, and making it look
like a completely original, novel idea (for instance, the Gawker people are
masters at this. Much better at it than I am, since they actually like, you
know, make money doing it).

[Deathbots][9] just released the [Open Source Gym][10] project, which is a
suite of applications targeting at making exercise equipment more fun, through
generating infoporn from exercise sessions and controlling video games.
However, here at Slashdong, we know what REALLY drives people. Which page in
the NonPoly network has 100k+ hits? Huh? Damn motherfucking straight.

Anyways, here's the articles those dorks wrote:

[Hacking an Exercise Bike][11] [Nibbles (The Snake Game, not the small bites)
on an Exercise Bike][12]

So, let's see... These boards (or hell, anything with a motor driver and a
proper circuit or processor) can generate a PWM! And a PWM is all we need
to...

## How it works

Well, shit, I guess I kinda already said how it works. Oh well, no pain in
redundancy.

Oh yeah, so the project materials needed now are:

  * Exercise bike

  * Circuit capable of generating PWM with at least 3.3v coming through it (We
do not promote any certain board to do this. There are roughly a bazillion of
them, go find one and learn how to do it yourself.)

  * Sex toy of your choice (Remember guys, [this isn't just limited to
dildos][13])

[PWM! That wonderful control mechanism!][14]

If you don't want to read the wikipedia link, here's a quick explanation.
Pulse-Width Modulation is pretty self explanitory. You modulate the width of
the pulse to a certain duty cycle. So, say you've got a 50% duty cycle, that
means whatever you are sending power to will get it 50% of the time. That's
it. You wanna know more, read wikipedia or go to deathbots (or wait until we
post our teledildonics tutorial. We just hate repeating ourselves. Oh, and
hypocrites. We hate hypocrites too.)

[The Nibbles Game][15] that deathbots put together is a good example of how
this is going to work. In their game, the faster you pedal, the faster the
snake goes. In our game, the faster you pedal, the faster the snake goes.

*rimshot*

So, it's screen actuation versus physical actuation. Ours is much better
though.

The velocity of the bike is controlled by magnets on the flywheel and their
proximity to the hall sensor in the bike. The faster you pdeal, the more times
the magnet passes the sensor, and the higher your encoder velocity reads.

PWM is usually a 2 byte signed value between -255 < x < 255. We really aren't
interested in which direction we're going (unless you're using a dildo with
LEDs embedded in it, in which case, if you send the PWM the wrong way, your
LEDs arn't gonna light up, but we'll get to that in our LED dildo tutorial,
also coming soon!), so let's just deal with the positive side of the
inequality here.

There's a good chance that the lower 50% of the PWM range ain't gonna do shit
for your vibration motor. The power required to spin-up the motor usually
pretty high since the weight is loaded on the motor. We'll have our software
starting at 50% duty cycle or 255/2, which we'll just round to 127. Therefore,
the equation will be:

127+(128.0*(float)((currentVelocity < topVelocity) ? (currentVelocity /
topVelocity) : 1))

For all of you non-coders (but not non-math/logic people. If you can't do
those, just look at the purdy pictures and laugh when we tell you to) out
there, here's what's going on with that. We start out with 127, and then add
some value between 0 and 128 to it. This value is calulated one of two ways.
If we have some threshold velocity (i.e. topVelocity) we want to achieve to
get the full PWM, and we havn't hit it yet, we calculate the quotient of that
with our current velocity, which provides the scaling value for our PWM
modifier. If we've exceeded the topVelocity, good for us! We just add in the
full 128 and **FUCKIN GIVE'R**.

That's it! We've now got a simple encoder controlled PWM generator!

## Why this will revolutionize exercise

Oh come on, isn't it fucking obvious already? If you got some nice, vibratey
love every time you got on the exercise bike, wouldn't you exercise ALL THE
GOD DAMN TIME? Hell yes you would!

Just imagine! Legions of fit, buff, ripped women! Armies of men getting
stronger 3 minutes at a time with 2 hour breaks in the middle! LET THE
REVOLUTION BEGIN!

![][16] 

## Movies!

Need proof? [Here's a completely unsexy film of one of our test runs!][17]

   [2]: #1

   [3]: #2

   [4]: #3

   [5]: #4

   [6]: #5

   [7]: http://www.slashdong.org/images/bike/exercise0.jpg

   [8]: http://www.soundsoftheundergroundtour.com/

   [9]: http://www.deathbots.com

   [10]: http://www.deathbots.com/content/projects-open_source_gym.php

   [11]: http://www.deathbots.com/content/projects/open_source_gym/hooking_up_the_stamina_4700r_exercise_bike-000264.php

   [12]: http://www.deathbots.com/content/projects/open_source_gym/nibbles_the_exercise_bike_controlled_game-000266.php

   [13]: http://www.slashdong.org/boards/viewtopic.php?t=16

   [14]: http://en.wikipedia.org/wiki/Pulse-width_modulation

   [15]: http://www.deathbots.com/boards/viewtopic.php?t=16

   [16]: http://www.slashdong.org/images/bike/exercise1.jpg

   [17]: http://www.youtube.com/watch?v=pextgJtmt1g

