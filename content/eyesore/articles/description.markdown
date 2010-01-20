# EyeSore: Real Time 3D Projection with Second Life

<small><center>Originally posted on nonpolynomial.com, September 22, 2005</center></small>

![][2]

## Table Of Contents

  1. [Making 2D Life Into 3D Life][3]
  2. [Background Theory of Polarized Projection Systems][4]
  3. [Second Life Implementation][5]
  4. [Plans for the Future][6]

Thanks to Cubey Terra, and RenZephyr Zircon for helping out on this project

<A NAME='1'></A>
## 1. Making 2D Life Into 3D Life

Second Life (SL) is an amazing virtual world, capable of letting its users
produce beautiful, gigantic 3D structures. However, most users are stuck with
a 2D screen to view these on, making them lose their depth and graduer. The
EyeSore project (So named for the headaches it can cause when the system falls
out of sync, not to mention the fact that there is a large portion of builds
in SL that could easily be described as such) allows a user to navigate
through the world using the view points of two avatars, combined using a
polarized projection system onto a metalic reflective screen. Through the use
of polarized glasses and the vision capabilities of the human brain, the
images produced by the two viewpoints of the avatars are combined to create a
3D picture.

The system for this project was originally built for the [Copernicus Rover
Mission][7] at Amboy Crater in May of 2004. It was used as a Lunar Rover view
simulator for study of user interface and driver fatigue conditions for space
missions. More info on that project can be found at [Deathbots.com][8].

<A NAME='2'></A>
## 2. Background Theory of Polarized Projection Systems

![][9]

Polarized lenses are a common thing these days. From sunglasses to LCD
monitors, polarization is responsible for light and glare reduction in many
products. The theory behind it is fairly simple.

When light is emitted from a source such as a light bulb, it goes in all
directions. As it reflects off of different surfaces, the vibrations of the
light particles start to line up and point in the direction of the normal of
the reflecting surface. This effect is known as polarization. Orthoganal
polarization is responsible for what we usually call "glare".

More information on how polarization works can be found in [the sunglasses
article of How Stuff Works][10].

![][11]

To create a 3D image, we need to have two 2D images of the same scene, offset
so that they mimic the distance between human eyes. There are multiple ways to
do this. For examples, VR Headsets use shutters running at 30FPS per eye. The
graphics core will render 1 frame from the left eye, then 1 frame from the
right eye, and transfer each frame to the corresponding eye in the headset.

![][12]

In this project, we use a set of orthogonal polarized lenses to create a 3D
perspective. In front of each of two projects, we set a polarized lens. One
lens will only let "horizontal" waves through, while the other will only let
"verticle" waves through. The user then puts on glasses with the same setup:
One direction for the right eye, the other for the left eye. The rest of the
processing is done by the user's brain.

![][13]

When the brain combines images from each eye, it does the proper calculations
to form a triangle between the two eye positions and the point of light
reflection in that image. The result of these calculations is what we call
"depth perception". In 3D graphics, "projections" are used to turn this
perception into a single 2D image. The Eyesore project undoes the projection
by providing the user with 2 images, set over each other. Since each eye can
only see one image, the brain can once again triangulate between the two, and
depth is formed.

<A NAME='3'></A>
## 3. Second Life Implementation

![][14]

To play Second Life in 3D, we need 2 Second Life accounts, 2 fairly high end
machines, and a hefty broadband connection to deal with the massive amount of
object data coming in through each viewport. We used a Apple G5 and Intel P4
2.4ghz, both with 1.5 GB of ram, and ATI Radeon 9800 Pro video cards. These
machines seemed to handle the load with no problems. The projectors used are
BenQ, with a custom built X-channel stacking system.

![][15]

In the game, we put two cube primitives (or "prims") close together, and
linked them, meaning they would move as a single unit. We had the two avs sit
on the cubes, and put each of them into mouselook mode. After adjusting their
viewing points so that their vision lined up with the width of normal human
eyes, the screen snapped into 3D.

![][16]

As can be seen in the picture, the view without glasses isn't pretty. It looks
like two screen offset slightly from each other. Through the polarized
glasses, however, one eye can only see one image, and assuming both images are
synched in terms of distance and speed, the view becomes 3D.

![][17]

RenZephyr Zircon was nice enough to come walk in circles in front of the
camera in order for us to judge what dynamic movement would look like.
Animations tend to desynch slightly between the clients, but the basic object
position was close enough between viewports that it did still look 3D, if a
little glitchy.

<A NAME='4'></A>
## 4. Plans for the Future

Our plans for the future include attaching the viewport settings into vehicle
code in order to automatically set the eye positions. This will do away with
the rather sloppy mouselook setup process we had to deal with in this version.
Combining this with autopilot paths through the prettier parts of the world
(SeaCliff, Lusk, etc...) would make for some very neat flythru demos.

   [2]: http://images.nonpolynomial.com/nonpolynomial.com/projects/eyesore/eyesoreintro.jpg
   [3]: #1
   [4]: #2
   [5]: #3
   [6]: #4
   [7]: http://www.deathbots.com/gallery/AmboyCrater
   [8]: http://www.deathbots.com
   [9]: http://images.nonpolynomial.com/nonpolynomial.com/projects/eyesore/eyesorepolar.jpg
   [10]: http://travel.howstuffworks.com/sunglass4.htm
   [11]: http://images.nonpolynomial.com/nonpolynomial.com/projects/eyesore/eyesorepolarcompare.jpg
   [12]: http://images.nonpolynomial.com/nonpolynomial.com/projects/eyesore/eyesorepolarexplain.jpg
   [13]: http://images.nonpolynomial.com/nonpolynomial.com/projects/eyesore/eyesorepolartriangle.jpg
   [14]: http://images.nonpolynomial.com/nonpolynomial.com/projects/eyesore/eyesoreg5.jpg
   [15]: http://images.nonpolynomial.com/nonpolynomial.com/projects/eyesore/eyesoreslsetup.jpg
   [16]: http://images.nonpolynomial.com/nonpolynomial.com/projects/eyesore/eyesoredoorview.jpg
   [17]: http://images.nonpolynomial.com/nonpolynomial.com/projects/eyesore/eyesoreren.jpg

