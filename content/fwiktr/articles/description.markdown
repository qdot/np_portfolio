# Fwitkr - Generative-Captioned Photos

<CENTER><small>Originally posted on nonpolynomial.com, June 23, 2007</small></CENTER>

Weird things happen when I get bored.

Luckily, they're usually things that make both me and others less bored.

I've had a 3Com Audrey sitting on my computer desk for a few weeks now, staring at me, begging me to do something with it. Unfortunately, all it can really do is run a web browser. A web browser from the late 90's at that. No CSS love for me, nor even flash or anything else. Nope, only the basics of HTML. 

It seemed like it'd be a neat picture frame, at least. However, I didn't really want to just cycle random flickr pictures on it, because that's boring. There had to be some more interesting way to produce stuff for it, that would actually make me _want_ to look at it. 

Thus, Fwiktr was born.

**The Fwiktr Creation Process**

This is all done using python, because it seemed like a fun way to start picking up more parts of the language. 

Here's the ingredient list for everything that's not included with python these days:

* [Python Flickr API][1]
* [Python Twitter API][2]
* [Natural Language Toolkit][3]
* [Treetagger POS Tagging Utility][4]

The idea behind Fwiktr is simple. In its current form, it's bascially a [Chinese Room][5] artist. It pulls the last 20 lines from the public timeline of [Twitter][6], runs them through a parts of speech generator, and discards everything but the nouns. It then uses those nouns as basis to do tag searches on flickr. This is currently an "ANY" search, meaning that it will return pictures with any of the tags listed. It pulls a list of up to 100 images from flickr, picks one at random, dumps the information to a file, and uploads it to [http://www.30helensagree.com][7]

Right now, the Parts of Speech tagging happens through an external call to Treetagger. This is because before this project I'd had zero experience working with natural language processing, and I'm still working on figuring out exactly how one makes a nicely trained [Brill Tagger][8] in nltk. But I'll get to the future plans in a bit.

So, for all intents and purposes, Fwiktr is nothing but superglue right now. There's no real AI to speak of, it's a purely reactive behavioral system. Anything it does right is emergent, anything it does wrong is your fault for not understand the art it produces.

Now, I'm not the first person to do a twitter/flickr ma... mas... Ok, I can't bring myself to say that word. I'm not the first person to do a twitter/flickr combination before, there's some other neat ones out there:

* [Twitter+Flickr via Yahoo Pipes][9]
* [Flussgeist 1 - Waiting][10] - Twitter and Flickr and Video thru Flash. Warning: Will give you a nasty case of the ADDs
* [WPF Screensaver][11] - If you run Vista...

**What's Happened So Far**

[Here is the very first file Fwiktr ever put out][12] (File format: Flickr Message, Parts of Speech Output, Tag list, First 100 pictures returned by tag search)

That file cost me a good 30 minutes of time, just because I didn't format it nicely and found myself cutting and pasting URLs everywhere just so I could see what was going on. 

The first message:

_"Got my new Russian neighbor drunk on margaritas. USA! USA! USA!"_

The first URL gave me this image:

[![][13]][13]

Oh yeah, this was gonna be good.

Second message:

_"Laughing at Thomas' outburst in the maxipad section of the drug store: "Look Mum! All the vaginas are lined up in a neat row!" AH, 3. OY."_

Image?

[![][14]][14]

Ok, so, 2 for 2, but there was still the human element there, with me having to cut and paste the URLs. If Fwiktr was gonna work right, it would have to decide for itself which picture went with the message. So, it chooses a number between 1 and min(number of pictures returned, 100) and uses that image.

First automated message: 

_"Lovely spam, wonderful spa-a-m, Lovely spam, wonderful S Spam, Spa-a-a-a-a-a-a-am, Spa-a-a-a-a-a-a-am, SPA-A-A-A-A-A-A-AM, SPA-A-A-A-A-A-A-A"_

First automated image:

[![][15]][15]

I now firmly believe that God is communicating with me through Fwiktr.

Fwiktr has the capability to upload results on its own now, and is running a new image every 30 seconds at [30helensagree.com][7]. The current file format is:

  * Message Text
  * Image
  * Treetagger Output
  * Tag string sent to flickr
  * Random index selected and total result count
  * First 100 images returned

It's definitely had [some][16] [hits][17] as well as [some more artistic moments][18].

**The Future of Fwiktr**

Fwiktr has a long, long way to go. Right now, I'm content to revel in its emergence and work on a better interface for the display. But, I do have feature plans:

* Use Python Image Library to overlay the message on the image
  * Far future: Do this in some interesting, artistic way.
* Language Processing Tasks
  * Vary parts of speech used for tags
    * Obviously, tags are not just nouns. People use verbs, adjectives, and other parts of speech. These should get picked up while still dropping parts of speech that are rarely used for tags.
  * Use neural nets and manual feedback (via rating system on the site) to train tag combination system
    * When we pass tags to flickr, right now the only data Fwiktr knows is "I've got a pile of nouns, you do somnething with them!". If we could possibly say "Ok, I've got this set of nouns and this set of verbs and they go together with these boolean operations", we lose our chance for crazy emergence but possibly gain contextual search
  * An example of all of the above: In the first text file, one of the twitter messages was _"At board walk. Got an ice cream."_. Fwiktr did a good job of pull tags, and gave us back the list "board,walk,ice,cream". Unfortunately, when this pile was passed to flickr, it saw "board OR walk OR ice OR cream", and gave us back ANY images with tagged with board, walk, ice, or cream in them, which means, that we got lots of winter pictures of iced over trees, too. If Fwiktr knew to pass "boardwalk AND icecream", then we'd have gotten back 48 completely contextual images versus many thousand hits and misses. Of course, the AI between "board,walk,ice,cream" and "boardwalk AND icecream" is a mighty step.
  * Train up specific tagger for Fwiktr versus using treetagger
    * Natural Language Processing programs are trained off of what are called "Corpora", which is the plural of "corpus". Basically, it's text that's been marked up to show different grammatical structures and parts of speech to make it easy to process. Unfortunately, most of the big, usable corpora are stuck with HUGE, unusable costs to get to, because they're used by academic institutions who can afford them. Now, I'm not sure I really need to get able to hit all of [treebank][19] to get this working correctly, but I don't know if I'm gonna have much luck working with just the [Brown Corpus][20] either. Still lots to learn in this area, but I'm rather eager.

So, that's it for right now. Fwiktr is slaving away throwing new files up on the site, so keep an eye out. I hope to have a nice auto-reloading interface up by tomorrow. 

   [1]: http://beej.us/flickr/flickrapi/
   [2]: http://code.google.com/p/python-twitter/
   [3]: http://www.nltk.org
   [4]: http://www.ims.uni-stuttgart.de/projekte/corplex/TreeTagger/
   [5]: http://en.wikipedia.org/wiki/Chinese_room
   [6]: http://www.twitter.com
   [7]: http://www.30helensagree.com
   [8]: http://en.wikipedia.org/wiki/Brill_Tagger
   [9]: http://www.901am.com/2007/mashing-mashups-every-twitterer-tells-a-story-dont-they.html
   [10]: http://incident.net/works/flussgeist/waiting/flash/index.html
   [11]: http://windowsvistablog.com/blogs/windowsexperience/archive/2007/05/01/wpf-screensaver-flittrbook-from-mix07.aspx
   [12]: http://www.nonpolynomial.com/fwiktr.txt
   [13]: http://farm2.static.flickr.com/1110/594318483_1c8fd484c2.jpg
   [14]: http://farm2.static.flickr.com/1259/594386622_48f11538a0.jpg
   [15]: http://farm2.static.flickr.com/1250/592326463_dab506a4f2.jpg
   [16]: http://www.30helensagree.com/28e9ece0-e890-4e0b-a212-927bd15e19c4.html
   [17]: http://www.30helensagree.com/5fe7711d-4466-4e7c-ad45-032dad2508e1.html
   [18]: http://www.30helensagree.com/d250ddff-3e37-46d2-8834-f380d0fd2c83.html
   [19]: http://www.cis.upenn.edu/~treebank/
   [20]: http://en.wikipedia.org/wiki/Brown_Corpus

