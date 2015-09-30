#! /usr/bin/python
# Time-stamp: Wed Jun  4 12:47:50 CDT 2008 angenent

from grapher import *

setViewBox(-4.0,-1.6, 3.0,1.6)

openOutputFile("03signOFx",180)

#axes
line([-3,0], [3,0])
arrowhead([-3,0], [3,0], overshoot=-0.1)
line([0, -1.55], [0, -1])
line([0, 1.55], [0, 1])
arrowhead([0, 1], [0, 1.45], overshoot=1)

#dotted line at the jump
linewidth(0.5)
setdash("[1 4] 0")
line([0.0, -1.0], [0.0, 1.0])
setdash("[] 0")

#graph of sign(x)
linewidth(2.0)
setrgbcolor('red')
line([-2.5, -1.0], [0.0, -1.0])
line([2.5, 1.0], [0.0, 1.0])

#points on or not on the graph 
linewidth(1)
roundPoint([0.0, 0.0], 0.06, "", fillcolor='red')
roundPoint([0.0, 1.0], 0.06, "")
roundPoint([0.0,-1.0], 0.06, "")

#annotations
annotate([1.0,1.0], [0.0, 8.0], "$y=\\sign(x)$")
annotate([0,1], [-3,-2], makeboxr("$1$") )
annotate([0,-1], [2,-2], makeboxl("$-1$") )
closeOutputFile()


