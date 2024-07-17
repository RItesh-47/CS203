Bertrand\'s Paradox Simulation

Each and every of the given three Python scripts simulate a solution
method for Bertrand\'s paradox.

1\. The first solution focuses on the condition where all chords passing
through some point within the incircle of an equilateral triangle
inscribed in a circle are longer than the side of the triangle.

2\. In the second solution we basically allocate one endpoint of chord
to one of the vertex of triangle then this chord will be larger than the
sides only if the other endpoint lies on the minor arc between the other
2 remaining vertices of triangle.

3\. In the third solution we consider the distance of chords from the
centre , all chords with distance greater than r/2 (r=radius) are longer
than the sides of triangle.

How to run the code:

1\. Dependencies: - Python 3.x - Matplotlib library

2\. Installation: - Ensure you have Python installed on your system. -
Install Matplotlib library using pip: pip install matplotlib.

3\. Running the Script: - Download the specific script (Bertland1.py or
Bertland2.py or Bertland3.py) which you want to view and save it in your
directory. - Open a terminal or command prompt. - Navigate to the
directory where the script is saved. - Run the script by executing the
command: python Bertland1.py or simply open the desried file in VS Code.

4\. Understanding the Output: (a) The first script displays all the
chords passing through 2 set of points , firstly through points outside
the incircle of triangle and secondly within the incircle. Both of these
chords are colored differently. - The script will display a visual
representation of a circle with random chords drawn inside. - Chords
intersecting a smaller circle (centered at the midpoint of the chord)
are plotted in blue. - Chords not intersecting the smaller circle are
plotted in red. - The script will print the ratio of chords longer than
the side of an triangle inscribed within the circle in the terminal.

(b)The second script shows all the chords whose one endpoint is fixed at
the vertex (0,0) and how many of these chords' endpoints lie on the
minor arc between the remaining 2 vertices of the triangle. - An
equilateral triangle is inscribed within the circle, with vertices
located at (-1, 0), (1/2, sqrt(3)/2), and (1/2, -sqrt(3)/2). - Points
falling within a certain range of slopes with respect to the x-axis are
colored green, while points outside this range are colored red. - The
script prints the proportion of points falling within the specified
range out of the total number of generated points.

(c)The third script shows 2 sets of chords , one that are at a distance
less than r/2 from centre and others that are at a distance greater than
r/2 from centre. - Each line segment is randomly generated with one
endpoint at the center of the circle (0,0) and the other endpoint at a
random distance from the center. - Line segments where the distance from
the center is less than or equal to 1/2 of the circle\'s radius are
plotted in green, while those with distance beyond this are plotted in
red. - The script prints the proportion of chords at a distance less
than ½ from centre to total number of chords.

5\. Interpreting the Results: (a) For method 1: - The printed ratio
indicates the likelihood of randomly drawn chords being longer than the
side of an equilateral triangle inscribed in the circle. - According to
Bertrand\'s paradox, if all chords passing through some point within the
incircle of the triangle are considered, they are likely to be longer
than sides of the triangle.

\(b\) For method 2: - The printed proportion represents the likelihood
of randomly generated other endpoints of the chord whose one endpoint is
fixed at (0,0) , falling within the region defined by the slope range
relative to the x-axis, which is basically the whole minor arc between
the remaining 2 vertices of the triangle.

\(c\) For method 3: - The script prints the probability of randomly
selecting a line segment within a distance of 1/2 of the circle\'s
radius from the center. - This probability represents the likelihood of
a randomly chosen line segment satisfying the specified condition

6\. Customization:  - You can adjust the number of simulated chords (n)
by changing the variable value in the script.  - The radius of the
circle can also be modified by changing the radius variable.
