# logMap
#### Map of all TF2 Players from Logs

#### How it works
Used python to gather all the data and deposit into csvs. Then used more python to add in the "correct" names for players based on id. (still isn't that accurate)
Then used Gephi (project files included) to create the image itself.
I used OpenOrd -> Fruchterman Reingold -> Force Atlas 2 until I liked how it looked. I had to run Expansion at various stages as well to avoid extreme overlapping and clumping.

#### Future Plans
I want to make this with all log data. I have about 9000 RGL Names (some of which have ESEA as well), ETF2L has an API, demoticks.tf has many names, and finally I can use basic steamAPI to get literal profile names should every other means fail.

The exported big image is 14000x14000. I didn't have any luck with the SVG or PDF outputs, found them both clunky and buggy.
I would like to make maps of different eras, years, and seasons, as well as a total set. In addition it is definitely possible to collect more data, however Kastaling has more projects coming up in the future in that regard.

I also want to figure out the best way to actually visualize the data, it feels clunky to use gephi, not sure what other programs exist and how well they perform. I wasn't able to get fantastic looking results really.
