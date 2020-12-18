## pixmastree

Some scripts for https://thepihut.com/products/3d-rgb-xmas-tree-for-raspberry-pi

You will need `tree.py` from https://github.com/ThePiHut/rgbxmastree

### Scripts

- **off:** As simple as the "on" behaviour tree.py has by itself, just shuts your tree off. Handy after trying other examples, including the stock ones.
- **enumerate:** Walks through lighting each LED red in turn while printing its number to the console. Useful if you want to work out their mapping, or for testing they're each responding.
- **twinkle:** A rather hacky approximation of twinkling fairy lights that each independently heat up and trip a simulated bimetallic strip that shorts them, so the extra current spreads to the rest of the lights. Inspired by [Technology Connections](https://www.youtube.com/watch?v=zeOw5MZWq24) gushing about them, if a little abstractly pleasant rather than particularly accurate to the real thing.
