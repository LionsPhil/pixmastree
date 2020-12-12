from tree import RGBXmasTree
from time import sleep
import random

tree = RGBXmasTree()

def incandesce(brightness):
	brightness = max(0.0, min(brightness, 1.0))
	# Ideally, this should have a emissive temperature curve
	r = brightness * 0.5
	g = brightness * brightness * 0.2
	# Blue seems almost binary in its behaviour; any at all is POWERFUL
	b = 0 # brightness * brightness * brightness * 0.1
	return (r, g, b)

resistances = [1.0] * len(tree)
temps_fil = [0.0] * len(tree) # filament temperatures
temps_bi = [0.0] * len(tree) # bimetallic strip temperatures
new_pixels = [(0, 0, 0)] * len(tree) # buffer to batch-setting pixels

voltage = 0.5 * len(tree) # enough for bulbs to normally run at 50%
bms_every = 1 # doesn't work very well
bimetallic_open_temp = 0.5
heat_rate = 0.1
heat_variance = 0.05
heat_transfer_rate = 0.1
cool_rate = 0.05
open_resistance = 0.01

try:
	while True:
		total_resistance = sum(resistances)
		for index, pixel in enumerate(tree):
			# Work out the voltage across this bulb
			v_drop = voltage * (resistances[index] / total_resistance)
			# Clamp it, should we be the only one on
			v_drop = min(v_drop, 1.0)
			# Does this one *have* a bimetallic strip?
			has_bms = ((index % bms_every) == 0)
			# Heat filament based on current and noise if not yet shorted
			if not has_bms or temps_bi[index] < bimetallic_open_temp:
				temps_fil[index] += (v_drop * heat_rate * random.uniform(1.0 - heat_variance, 1.0 + heat_variance))
			# Light it based on temperature
			#pixel.color = incandesce(temps_fil[index])
			new_pixels[index] = incandesce(temps_fil[index])
			# Transfer heat to the bimetallic strip
			temps_bi[index] += temps_fil[index] * heat_transfer_rate
			temps_fil[index] *= 1.0  - heat_transfer_rate
			# Radiate heat out from the bimetallic strip
			temps_bi[index] *= 1.0 - cool_rate
			# Recalculate its resistance for next cycle
			if not has_bms or temps_bi[index] < bimetallic_open_temp:
				resistances[index] = temps_fil[index] + 1.0
			else:
				resistances[index] = open_resistance
			# Debug
			if False and index == 0:
				print(f"Lamp {index} v {v_drop} tf {temps_fil[index]} tb {temps_bi[index]} r {resistances[index]}")
		tree.value = new_pixels
		# This should really have a proper limiter
		sleep(0.1)
except KeyboardInterrupt:
	tree.off()
	tree.close()
