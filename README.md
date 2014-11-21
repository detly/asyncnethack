# Asynchronous Nethack Interface

A pseudo-terminal wrapper over the best game of all time. The plan is to
decouple the playing of Nethack from the presentation, and eventually serve a
game of Nethack over the web.

## A note about `ansiterm.py`

This wrapper wouldn't be possible without the rad `ansiterm.py` module, which is
from https://github.com/helgefmi/ansiterm and is distributed under the terms of
the MIT license. Itt is included directly to make the module work smoothly.
