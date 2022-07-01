# glfw

Build2 package for glfw graphics library

Provides user configuration variables directly in with the build system
The following configuration variables are current supported:

`config.glfw.osmesa`(default false): Use OSMesa library.\
`config.glfw.usewayland`(default false): Use Wayland on Unix systems instead of X11\
`config.glfw.vulkan`(default false): Statically link with vulkan libraries\
`config.glfw.usehybridhpg`(default false): Use hybrid high performance graphics card


## Default setup on Linux

Uses X11 by default when building on linux. Set `config.glfw.usewayland = true` to enable Wayland support. This requires `wayland-scanner` to be installed on the system along with `wayland-protocols`.


## Offscreen Rendering

Set `config.glfw.osmesa = true` for Offscreen rendering support and requires `libOSMesa` to be installed on the system.\
Note: It is never expected that `config.glfw.usewayland` and `config.glfw.useosmesa` are true simultenously. In case it does happen, `config.glfw.osmesa` takes precedence over `config.glfw.usewayland`.
