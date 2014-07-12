DumbBar
=======

A (very) simple text based loading bar in python.

Most Basic usage:
    # Create the bar with default options.
    bar = DumbBar.DumbBar()
    # Draw the bar at 50% loaded.
    bar.drawBar(50)
    # Move to the next line
    bar.done()

would create a bar that looks like so:

    [==================================                                   ]  50%

In order to update the progress of the bar, simply call drawBar(percent) where percent is a number between 0 and 100.
drawBar can be called as many times as you like, up until done() is called.


Currently, these are the available options:
 * start:       The characters that will be at the left of the bar. Default is "["
 * end:         The characters that will be at the right of the bar. Default is "]"
 * fill:        The characters to fill the loaded section of the bar with. Default is "="
 * empty:       The characters to fill the unloaded section of the bar with. Default is " "
 * showPercent: Show or hide the percent at the end of the bar. Default = True
 * length:      The size in characters of the bar and percentage if enabled. Default = 79

 Note: if length is greater than the size of the terminal, the bar will spill into the next line.



Another example:

	bar = DumbBar.DumbBar(start="-=<", end=">=-", fill="#!#|", empty="_._")
	bar.drawBar(50)
	bar.done()

Would create a bar that looks like this:

    -=<#!#|#!#|#!#|#!#|#!#|#!#|#!#|#!#|_.__.__.__.__.__.__.__.__.__.__._>=-  50%

These options:

	bar = DumbBar.DumbBar(start="", end="", fill="=", empty="         |", showPercent=False)
	bar.drawBar(50)
	bar.done()

Would create a bar that looks like this:

	======================================        |         |         |         |


