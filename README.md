# Busy Bar #

### Description ###
Easily wrap a code block with a busy indicator in the terminal.<br/>
This module provides a context manager and a decorator that will print a 
small rotating cursor in the terminal with a chosen message while executing. 

### Usage: ###

```python
from busy_bar import Progress, progress
@progress()
def long_work():
    sleep(3)

def main():
    with Progress("Busy..."):
        sleep(3)
```
