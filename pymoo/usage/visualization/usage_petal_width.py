# START load_data
import numpy as np

np.random.seed(1234)
F = np.random.random((1, 6))
print(F)
# END load_data

# START petal_width
from pymoo.visualization.petal_width import petal_width

petal_width(bounds=[0, 1]).add(F).show()
# END petal_width

# START petal_width_reverse
petal_width(bounds=[0, 1], reverse=True).add(F).show()
# END petal_width_reverse

# START petal_width_custom
plot = petal_width(bounds=[0, 1],
                   cmap="tab20",
                   labels=["profit", "cost", "sustainability", "environment", "satisfaction", "time"],
                   title=("Solution A", {'pad': 20}))
plot.add(F)
plot.show()
# END petal_width_custom


# START petal_width_multiple
F = np.random.random((6, 6))
plot = petal_width(bounds=[0, 1], title=["Solution %s" % t for t in ["A", "B", "C", "D", "E", "F"]])
plot.add(F[:3])
plot.add(F[3:])
plot.show()
# END petal_width_multiple