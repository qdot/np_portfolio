# Everything you ever wanted to know about the FC2009 Fursuit Parade Scan 
<small>but didn't have time to ask because you had a fursuit head on or something...</small>

## Table of Contents: 

1. [History][1]
1. [Introduction][2]
1. [The Event][3]
1. [The People with the Truck][4]
1. [The Truck][5]
1. [The Data][6]
1. [The FC Scans][7]
1. [What data is available?][8]
1. [What you can do with it][9]
1. [Available Software/Viewers][10]
1. [Data Distribution][11]
1. [Available Media][12]
1. [Other Projects Using the Data][13]
1. [Licenses][14]

**[Don't care about the explanation? Just want to see the cool stuff? Skip to
the software section.][10]**

<A NAME="1"></A>
## History

  * 2009-02-08
    * Initial posting of information, software, data

<A NAME="2"></A>
## Introduction

Assuming you were at Further Confusion 2009 and around during the fursuit
parade, you may've seen a beat up truck with some spinny things on it. Or, you
may've been in a fursuit and told to get in a line around the median and then
a guy with a bullhorn walked around and yelled "HOLD YOUR POSE" constantly
without really explaining what was going on. Or, maybe you weren't even there.

You should've been. It was fun.

Either way, this page should answer any questions you have about the above
paragraph.

<A NAME="3"></A>
## The Event

The follow story took place at [Further Confusion 2009][15], a yearly furry
fandom convention held in San Jose, CA. Specifically, this happened during the
fursuit parade (for those not familiar with fursuit parades, [there's a
description here][16]. Ignore the footnote. I totally count.). To say the
experience is surreal is an understatement.

[![][17]][18]

[Image via Kyreeth/Tugrik][18]

At the 2009 con, there were 530 suits in the parade, and over 2500 attendees
overall.

I've been going to Further Confusion for the past 3 years (for the record,
[I'm a cube][19]), and it always ends up being an interesting time. While I
was working at [Linden Lab][20], I ran the Second Life panel, which was one of
the few times I was subjected to real life, phsyical griefing attacks. In
2006, I managed to [video a line dance][21], [get sued for doing so][22] and
then [thanks to the EFF, win the case and open source the dance under the
Creative Commons License][23]. I even have [a cubesuit][24] that I wear in the
fursuit parade, which, in 3 years of use (sadly, as of 2009, the cubesuit is
dead. Long live cubesuit v2, to be seen at FC2010) has somehow has not gotten
me beaten senseless by everyone else in the parade. _Yet._

Like I said. Interesting time. I just couldn't let this year go by being any
less interesting.

<A NAME="4"></A>
## The People with the Truck

I currently work for a place called [510 Systems][25]. We're a navigation,
robotics, and controls research lab located in Berkeley, CA. We research and
create solutions related to problems in high accuracy navigation, surveying,
and geographic data analysis.

Or, more to the point, there's some robotic bulldozers and cars that drive
themselves and lasers. Lots of lasers.

[DID I MENTION WE'RE HIRING?][26] (if this link doesn't work, just search
craigslist for "robotics" in Berkeley. Our job ads usually pop up there.)

To give you an idea of some of the things 510 systems has done:

  * [Velodyne LIDAR Processing on the Radiohead House of Cards Video][27]

  * [Work on the self-driving PriBot that was featured on the Discovery Channel's Prototype This][28]

We also have vehicle mounted systems that can create a 3D "point cloud" of the
area surrounding the vehicle, through a combination of specialized hardware,
sensors, and processing software. It looks something like this.

[![][29]][25]

The week before FC2009, I was telling some of my con stories to a couple of
coworkers over lunch. After explaining the fursuit parade, I joked that we
should take one of our scanning vehicles and create a 3d scan of the fursuit
parade. To my surprise, this got a positive reaction, plans were made, and
come Saturday, the truck showed up.

Holy crap, we were actually gonna do this thing.

<A NAME="5"></A>
## The Truck

This is the truck, and more importantly, this is our system that is attached
to the truck.

[![FC2009 Fursuit Parade 3D Scanning][30]][31]

And from the side:

[![][32]][33]

[Cropped from image by Aatheus][33]

The rig in those pictures consists of (to get an idea of placement, go to the
flickr picture in the first link):

  * IP-S2 Integrated Positioning System
    * The heart and brains of the operation. This is the box everything
connects to. The box takes all of the data coming from all of the sensors,
timestamps it with a very accurate timestamp, and sends it out a network port
to be logged on a computer.
  * Velodyne LIDAR
    * A 360 degree spinning LIDAR with 64 lasers. Capable of spinning at
between 5-15 rotations per second, and outputting ~1.5 million points per
second, each with a maximum distance of ~180m. Each point represents a
distance in space with a certain amount of reflectivity. For example, the
LIDAR can tell you that when a laser fired, it was rotated at 34 degrees from
top, and that there was something 64.21m away at that distance, with a
reflectivity based on whatever the laser bounced off of. For more information,
see the [House of Cards Making-Of Video][34]
  * SICK LIDAR
    * In this specific case, ~90 degree LIDAR. Pointed at the street, and not
rendered in distributed point sets. Unless you really want accurate shots of
the street
  * GPS
    * For positioning of the vehicle. Most everyone is familiar with these
nowadays.
  * IMU
    * An IMU is made up of 3 accelerometers and 3 gyros. It gives you an idea
of which direction you're headed, and how you're rotated while heading that
direction.
  * Wheel Encoders
    * Attached to the hubs of the back wheels. Gives you information about
exactly how fast you were going at a point in time.

This isn't all the sensors the IP-S2 can handle, but reflects the set we had
on the truck that day. As the truck is driven around, all of the sensors
listed above feed data into the IP-S2, which then feeds it into another
computer. All of this data is very, very accurately timestamped.

<A NAME="6"></A>
## The Data

What does this get us?

  * The ability to reconstruct what's around us at a certain time. We can take
our place in the world as found by the GPS at time A, match that with a laser
scan taken as close to time A as possible, which gives us distance, and use
math to give back a geographically referenced version of that point. Multiply
that times thousands if not millions of points, and you can have a 3D model of
a town with a single drive through. Images taken by a system controlled camera
can also be matched to this model so that it can be colorized (like in the
image in the point cloud image earlier in this document).
  * If GPS drops out, as it often does in environments with "things" and
"stuff" (especially of the tall, opaque variety) in them, we can use the rest
of the sensors to approximate our position. We do this using [magic][35].
  * Much, much more, but this is about a specific event, not the system in
general, so I'll stop. But it's freaking awesome, isn't it?

To give you an idea of uses for this system... Say you're a department of
transportation, and you want to know where your streets are painted, with
what, and if they need to be repainted. Now, you could send drivers out to
eyeball this. But, with the system above, when all of the data comes back
together, you can see things like this:

[![streetpc][36]][37]

The scan above is from the Doubletree Hotel parking lot, taken during the
parade. Each one of those points that make up the image scan is georeferenced,
and you can see both the old arrow and the newly repainted ones. With some
processing, you can even have software pick out features these features, and
possibly have it give back a rating of the quality, so that if something needs
to be repainted, the software can add that to a schedule automatically.

[![FC2009 Fursuit Parade Point Cloud Screenshot][38]][39]

Or you can take scans of people in fursuits. Isn't living in the future fun?

<A NAME="7"></A>
## The FC Scans

Ok, down to business. Here's the information on the scans we took at FC.

### Scan 1 - Pre-fursuit Parade

[![kmlrun1][40]][41]

**Point Count:** ?

**Information:** Taken before the fursuit parade, while the lineup was just
starting. Interesting view of the back area of the hotel. This honestly ends
up looking more like a zombie attack than a fursuit parade, especially when
played in real time.


### Scan 2 - Pre-fursuit Parade

[![kmlrun2][42]][43]

**Point Count:** ?

**Information:** Taken while the fursuit parade was entering the hotel. The
honking was not our fault: blame the wolf in the dragon suit. :)


### Scan 3 - Post-fursuit Parade

[![kmlrun3][44]][45]

**Point Count:** 331 Million Points

**Information:** The cloud that's been in the pictures and videos so far. This
was taken after the fursuit parade, when all of the suiters were lined up
around the median in the parking lot. 3 sets of scans were taken of this (once
clockwise around, two counterclockwise around).

<A NAME="8"></A>
## What data is available?

Before we can go into what can be done with the data, we need to discuss what
data is available. The data is presented on a per-point basis, but the main
question, what data can be used where? Well, let's take a look at a couple of
pictures.

[![Point Cloud Viewing in Processing using HoC Viewer][46]][47]

This cloud is made up of 5 million points, about the maximum the House of
Cards Renderer (see the Available Software Section) can handle before choking.
We call this number our point budget. Now, you're probably saying _"BUT I CAN
RUN THE CRYSIS ENGINE AT MAXIMUM WHY CAN'T I RENDER MANY POINTS
WAAAAAAAAAAAAAAH."_. Well, get ahold of yourself. When rendering point clouds,
it's a completely different ballgame. Since the points are disconnected, you
can't use point indexing. Since there's no polygons, there's none of the
pipeline optimizations inherent in using triangles. Of course, there's
solutions for these problems, mainly having to do with spacial data structures
and compression that can easily deal with hundreds of millions of points, but
since the easiest way for everyone on every platform to view the clouds was
using the prewritten, Processing (and therefore java) based House of Cards
viewer... Well, there you go.

So, yeah, 5000000 points up there. If you look at the larger version of it
(available on flickr), you'll notice that we're blowing a TON of our point
budget on the large, flat surfaces in the surrounding world. The road, the
hotel, things like that. Now, a point reduced version.

[![fullrun][48]][49]

This is a zoomed out version of the full first pass of the fursuit parade.
This _whole view_ is only 3,405,808 points. This was created by isolating the
usable scan angles to a 30 degree arc, and limiting the maximum acceptable
scan distance to around 5m from the sensor position at the time of laser
firing. This still gets all of the suit data into the cloud, while eliminating
the road, the hotel detail, other people, etc...

Now, this data can sometimes be interesting. For instance, this shot taken
during the second run:

[![FC2009 Point Cloud Demo Picture - Large (See "All Sizes")][50]][51]

This shot got the whole back of the hotel, which, while filling up the point
budget quick, looks really cool. So, the tradeoff is in providing the maximum
amount of data to people who want to parse it, while still giving interesting
smaller sets for people who just want to see pretty 3D stuff. The current
distribution method will be a set of points with cartesian position and
intensity, and a basic path of the sensor through this cloud so you can easily
crop out things in the far background if need be. Once interesting optimized
sets are produced, we'll also post those.

<A NAME="9"></A>
## What to do with the data


### Viewing

Now that you've either trudged through my geekout or skipped to this portion,
it's time to talk about how you can see the data. I've done a little work and
modified the [House of Cards Viewer][52] to fit our needs. I added a vaugely
movable camera, and changed the loading to use a buffered reader since we tend
to have much, much larger files than what was originally used with the viewer.
The viewer is available in [software section][10]. It's based on
[Processing][53], which is in turn based on Java, so it's pretty mcuh
instantly crossplatform. Also, fairly slow, and maddening to work with if
you've ever done stuff with OpenGL (They flip the handedness of the system and
do odd things with screen versus world coordinates, so be warned. I sure
wasn't). But, what it loses in ease of development for me, it gains in being
crossplatform, easily accessible to people who don't have a job doing this,
and already mostly written.

### Mesh Forming

Miss playing Connect The Dots, but felt like conventional, 2d, numbered
connect the dots doesn't really provide that same "kick" anymore? Well, point
cloud tesellation is right for you!

The following images were created using [Meshlab][54], a free program for
working with 3D mesh and point data. Other 3D rendering/creation programs may
handle this data, but this one is free and fairly simple. Just take a fairly
small portion of the overall cloud (Meshlab doesn't play well with
tessellating tons of points at the moment, espectially with this setup...

[![ml1][55]][56]

Then hit Filter->Create Surface from Points, and...

[![ml2][57]][58]

Eureka! An incredibly noisy mesh, but still, something to work with. A lot of
things can be done to optimize the point cloud before putting it through
MeshLab or other software, but that's left as an exercise for the reader.

### Sculpties

Point clouds are ripe for usage with [Sculpted Prims][59] in Second Life.
Sculpties work by creating a displacement map on a sphere, which can easily be
done by taking a spacially optimized portion of the cloud, centering a sphere
behind it, and creating the displacement map texture based on the distance of
the points from the surface of the sphere. Since the point coordinates are in
real world measurements (meters or millimeters usually), the measurements
should translate easily into SL models.

### Arbitrary Image Colorization and Matching

Lots of people were taking lots of pictures while we were scanning. For
instance, this photo:

[![][60]][61]

[Cropped from image by Aatheus][33]

Could easily be matched to a shot of the point cloud taken from roughly the
same position and perspective:

[![pointcompare1][62]][63]

Since we know that the picture contains less dimensional information than the
scan, we scan create a projection that matches the picture (and therefore the
colors) to the most protruding point in the scan at the same location,
providing us with a partial coloring of the point cloud.

(I realize the above two images aren't very well matched, but this is more for
example than implementation, and it's hard to make out features of the cloud
if the screenshot is taken from the same perspective as the picture. So use
your imagination or something.)

<A NAME="10"></A>
## Available Software/Viewers

### Pointy - Open Source Point Cloud Viewer

Pointy is an open source point cloud viewer, currently based in the
[Processing][53] language. It was forked off the [Radiohead "House of Cards"
Viewer][27]. This fork adds a movable camera and buffered file loading, as
well as other features as I work up the patience to deal with Processing.

[Code repository hosted at github][64]

[Installation files and datasets hosted at sourceforge][65]

**Current Version:** 0.0.1

**PACKAGED WITH RUN 3, PASS 1 DATA. NO NEED TO DOWNLOAD DATA DISTRIBUTION
PACKAGE.**

  * [Windows Version (30mb)][66]
  * [OSX Version (30mb)][66]
  * [Linux Version (30mb)][66]

_Controls:_

Controls are "Resident Evil" style. Yeah, I hate them too, but I'm just trying
to get the first version out right now. :)

  * w/up arrow : forward
  * s/down arrow : backward
  * a/left arrow : turn left
  * d/right arrow : turn right
  * e : move upward
  * c : move downward

<A NAME="11"></A>
## Data Distribution

Check back often for more data postings.

* [CSV Format of Run 3, Pass 1 (Angle/distance reduced)][67]
    * You do not need this to use the viewer. This is posted for those who want to use the data outside of the viewer.
    * Size: 19mb
    * Format: CSV, Position and Reflectivity data only, "x,y,z,r,g,b" (In order to conform to House of Cards cloud format). R = G = B since there was no color data is available.

<A NAME="12"></A>
## Media

* [Flickr Cloud Generation Photo Set][68] - Includes links to other photo sets

* [FC2009 Fursuit Parade Point Cloud Test Render][69] from [qDot][70] on [Vimeo][71].

<A NAME="13"></A>
## Other Projects using this data

None yet! If you have a project that's using this data, and would like to be
included on this page, please email the "kyle" address at the domain you're
currently on.

<A NAME="14"></A>
## Licenses

* House of Cards Viewer originally written by and copyright 2008 Aaron Koblin
* Licensed under the Apache License, Version 2.0 (the "License");
    * Viewable at [http://www.apache.org/licenses/LICENSE-2.0][72]
* All distributed data Copyright 2009 [510 Systems][25]
    * Made available under the Creative Commons Attribution-Noncommercial-Share Alike 3.0 License
    * Viewable at [http://creativecommons.org/licenses/by-nc-sa/3.0/us/][73]

   [1]: #1

   [2]: #2

   [3]: #3

   [4]: #4

   [5]: #5

   [6]: #6

   [7]: #7

   [8]: #8

   [9]: #9

   [10]: #10

   [11]: #11

   [12]: #12

   [13]: #13

   [14]: #14

   [15]: http://www.furtherconfusion.org/fc2009/

   [16]: http://furry.wikia.com/wiki/Fursuit_parade

   [17]: http://images.nonpolynomial.com/nonpolynomial.com/portfolio/fc2009-point-cloud/post-parade.jpg

   [18]: http://www.furaffinity.net/view/1961292/

   [19]: http://www.flickr.com/photos/qdot76367/366743514/in/set-72157594495327675/

   [20]: http://www.lindenlab.com

   [21]: http://www.youtube.com/watch?v=y9pCuRHmQvw

   [22]: http://news.cnet.com/2100-1030_3-6156021.html

   [23]: http://w2.eff.org/legal/cases/electricslide/

   [24]: http://www.flickr.com/photos/qdot76367/367648572/in/set-72157594495327675/

   [25]: http://www.510systems.com

   [26]: http://sfbay.craigslist.org/eby/sof/1011718477.html

   [27]: http://code.google.com/creative/radiohead/

   [28]: http://news.cnet.com/8301-11386_3-10042320-76.html?tag=newsLeadStoriesArea.0

   [29]: http://images.nonpolynomial.com/nonpolynomial.com/portfolio/fc2009-point-cloud/510building_cloud.jpg

   [30]: http://farm4.static.flickr.com/3523/3227766296_c518b4949a.jpg

   [31]: http://www.flickr.com/photos/qdot76367/3227766296/ (FC2009 Fursuit Parade 3D Scanning by qdot76367, on Flickr)

   [32]: http://images.nonpolynomial.com/nonpolynomial.com/portfolio/fc2009-point-cloud/trucksideview.jpg

   [33]: http://www.taur.net/coppermine/displayimage.php?album=21&pos=93

   [34]: http://www.youtube.com/watch?v=cyQoTGdQywY&hl

   [35]: http://mitpress.mit.edu/catalog/item/default.asp?ttype=2&tid=10668

   [36]: http://farm4.static.flickr.com/3383/3264791625_b13c62b63e.jpg

   [37]: http://www.flickr.com/photos/qdot76367/3264791625/ (streetpc by qdot76367, on Flickr)

   [38]: http://farm4.static.flickr.com/3420/3235848346_838ce9bb52.jpg

   [39]: http://www.flickr.com/photos/qdot76367/3235848346/ (FC2009 Fursuit Parade Point Cloud Screenshot by qdot76367, on Flickr)

   [40]: http://farm4.static.flickr.com/3390/3265829560_e289c09f2a_m.jpg

   [41]: http://www.flickr.com/photos/qdot76367/3265829560/ (kmlrun1 by qdot76367, on Flickr)

   [42]: http://farm4.static.flickr.com/3448/3265829744_2e687c0297_m.jpg

   [43]: http://www.flickr.com/photos/qdot76367/3265829744/ (kmlrun2 by qdot76367, on Flickr)

   [44]: http://farm4.static.flickr.com/3431/3265829374_4eb75bb0b8_m.jpg

   [45]: http://www.flickr.com/photos/qdot76367/3265829374/ (kmlrun3 by qdot76367, on Flickr)

   [46]: http://farm4.static.flickr.com/3485/3239949109_3e01e0fc05.jpg

   [47]: http://www.flickr.com/photos/qdot76367/3239949109/ (Point Cloud Viewing in Processing using HoC Viewer by qdot76367, on Flickr)

   [48]: http://farm4.static.flickr.com/3493/3265953766_a7790490f3.jpg

   [49]: http://www.flickr.com/photos/qdot76367/3265953766/ (fullrun by qdot76367, on Flickr)

   [50]: http://farm4.static.flickr.com/3418/3232692660_9d7479a48d.jpg

   [51]: http://www.flickr.com/photos/qdot76367/3232692660/ (FC2009 Point Cloud Demo Picture - Large (See "All Sizes") by qdot76367, on Flickr)

   [52]:

   [53]: http://www.processing.org

   [54]: http://meshlab.sourceforge.net/

   [55]: http://farm1.static.flickr.com/245/3264871876_6a1365d8b3.jpg

   [56]: http://www.flickr.com/photos/qdot76367/3264871876/ (ml1 by qdot76367,on Flickr)

   [57]: http://farm1.static.flickr.com/198/3264872006_aeb4163442.jpg

   [58]: http://www.flickr.com/photos/qdot76367/3264872006/ (ml2 by qdot76367,on Flickr)

   [59]: http://wiki.secondlife.com/wiki/Sculpted_Prims

   [60]: http://images.nonpolynomial.com/nonpolynomial.com/portfolio/fc2009-point-cloud/pccomparison.jpg

   [61]: http://www.taur.net/coppermine/displayimage.php?album=21&pos=82

   [62]: http://farm4.static.flickr.com/3338/3268111361_ca066e2c79.jpg

   [63]: http://www.flickr.com/photos/qdot76367/3268111361/ (pointcompare1 byqdot76367, on Flickr)

   [64]: http://github.com/qdot/pointy/tree/master

   [65]: http://www.sourceforge.net/projects/pointy

   [66]: https://sourceforge.net/project/showfiles.php?group_id=252958&package_id=309439&release_id=659871

   [67]: http://images.nonpolynomial.com/other/fcrun1.tar.bz2

   [68]: http://www.flickr.com/photos/qdot76367/sets/721576129

   [69]: http://vimeo.com/3116248

   [70]: http://vimeo.com/user154518

   [71]: http://vimeo.com

   [72]: http://www.apache.org/licenses/LICENSE-2.0

   [73]: http://creativecommons.org/licenses/by-nc-sa/3.0/us/

