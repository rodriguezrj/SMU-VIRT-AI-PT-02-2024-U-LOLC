# Laundry Pseudocode

```python
# Algorithm: Sorting Laundry

# Tasks:
# Sort white
# sort reds
# Sort delicates
# Sort everything else

# Pattern recognition:
# delicate clothes go into basket 1
# white clothes in white clothes basket 2
# red clothes in basket 3 
# everything else in basket 4

# Abstraction:
# ignore towels
# ignore rugs
# ignore blankets

# Sequence:
# Event 1: Sorting Laundry
# Loop: for (each item in the laundry that is not towels, rugs, blankets):
    # Conditional: 
        # If (item is delicate and white):
            # place in basket 1
        # Else if (item is white):
            # put them in basket 2
        # Else if (item is red):
            # put then in basket 3
        # Else
            # put in basket 4
```
