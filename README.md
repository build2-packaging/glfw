# glfw

Build2 package for glfw graphics library

Provides user configuration variables directly in with the build system
The following configuration variables are current supported:

`config.glfw.usewayland`(default false): Use Wayland on Unix systems instead of X11\
`config.glfw.osmesa`(default false): Use OSMesa library\
`config.glfw.vulkan`(default false): Statically link with vulkan libraries\
`config.glfw.usehybridhpg`(default false): Use hybrid high performance graphics card
