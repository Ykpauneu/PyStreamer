# PySAMP-streamer

[Streamer](https://github.com/samp-incognito/samp-streamer-plugin) plugin handler for [PySAMP](https://github.com/pysamp/PySAMP)

## Installation

1. To install, you need to download the streamer plugin. After that you must put `streamer.dll` into your server folder (`server/plugins`).

2. After that, download (or clone) the repository and put the pystreamer folder in your server folder.

```bash
git clone https://github.com/pysamp/PySAMP-streamer.git
```

## Example

```python
from pysamp import on_gamemode_init
import pystreamer
from pystreamer.dynamicobject import DynamicObject

@on_gamemode_init
def on_ready():
    pystreamer.register_callbacks()
    global my_object
    my_object = DynamicObject.create(
        994,
        1161.73767,
        -1741.43555,
        13.06450,
        0.0,
        0.0,
        0.0
    )

@DynamicObject.on_moved
def on_dynamic_object_moved(object: DynamicObject):
    ...

```

## Important

Change the order in which plugins are loaded

```
# server.cfg
plugins streamer PySAMP
```
If you use [open.mp](https://www.open.mp/en)
```json
    "pawn": {
        "legacy_plugins": ["streamer", "PySAMP"],
        "main_scripts": [
            "empty"
        ]
    },
```

Otherwise, loading PySAMP **before** streamer leads to various **bugs** (double-triggering of callbacks, etc.)

## Thanks to

* [Incognito](https://github.com/samp-incognito) for Streamer plugin
* [denNorske](https://github.com/dennorske), [habecker](https://github.com/habecker), [Cheaterman](https://github.com/Cheaterman) for developing PySAMP
* To everyone who helped in the development of the project
