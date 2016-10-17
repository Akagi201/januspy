# januspy

Python client to interact with Janus Gateway.

## Deps

* Python 3, Please use [pyenv](https://github.com/yyuu/pyenv) and [pyenv-virtualenv](https://github.com/yyuu/pyenv-virtualenv)
* `pip install -r requirements.txt`
* For streaming you might need `gstreamer` installed.

## Run

* Modify configs in `config.py`
* `python -i janus.py`

## Commands

### `greet()`

Run this first to establish a session.

### `attach(plugin_name)`

Attach to the plugin, name is optional, cm.rtpbroadcast is default.

### `keepalive()`

Refresh the session timeout.

### `list()`

Run this after `attach()`, lists the mountpoints.

### `create(id)`

Create a mountpoint `id`, default is `Ababagalamaga`.

### `destroy(id)`

Destroy the mountpoint by `id`, default is `Ababagalamaga`.

### `stream(amin,amax,vmin,vmax)`

Create streaming streams, params means maximal and minimal bitrate and can be omitted with
default values.

### `unstream()`

Stops streaming. *Don't forget* to do this when you stop session. It's *not* done automatically. Manual kill:
```
killall gst-launch-1.0
```

### `session()`

Runs `greet()`, `attach()` and `create()`
