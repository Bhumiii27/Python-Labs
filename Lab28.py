from plotnine.data import economics
from plotnine import ggplot, aes, geom_line
print(economics)
(
    ggplot(economics)  # What data to use
    + aes(x="date", y="pop")  # What variable to use
    + geom_line()  # Geometric object to use for drawing
)
ggplot(mpg) + aes(x="class", y="hwy") + geom_point()
