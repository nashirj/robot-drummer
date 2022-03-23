# robot-drummer
Potential UCF Honors Undergraduate Thesis/Senior Design project

ideal: robot jazz drummer that comps effectively.

potential learning process: large temporal dataset pairing solos (e.g. horn/piano/etc) with drum comping. also need vocab of the great drummers.

the physical implementation should be a plug and play solution that can be placed onto basically any drumset with no extreme structural modification to the drumset. adjusting cymbal stand heights/etc is ok.

challenging to have good feel/dynamics/phrasing

maybe be able to "read" and play different styles?
- start with sightreading verbatim, translating directly to actuation signals
- sightread drum chart, first noting the "style", then playing in the style, and catching hits and stuff musically

One way to solve challenge of knowing when to go on for repeated sections is to mimic human approach
- when the soloist looks at the robot drummer, the drummer can use a camera to do facial recognition on the face of the soloist; this signifies it is the last repeat of the repeated section.
- ideally, a human can understand through listening and understanding of musical intent identify when the solo is coming to an end; need to think of a way to formalize this

One of the first steps for the baseline idea is to identify a representative language
- the set of distinct sounds you can make with a drumset is close to infinite
- want to identify the smallest set of sounds that represents the base language of a jazz drummer
- then need to figure out how to build electromechanical system that can create these sounds on the drums

Could "learn" songs through listening to it one time and build a "model" of the song that can then be played/improvised over

Very first version of project would be 
`computer -> midi -> program I write -> actuation signal -> microcontroller -> motor`

# References
https://www.youtube.com/watch?v=5rwhbBKfXnY
https://polyend.com/perc-drumming-machine/
https://www.instructables.com/Arduino-Controlled-Robotic-Drum/
https://www.instructables.com/Arduino-Drum-Man/
