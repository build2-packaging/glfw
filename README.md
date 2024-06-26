# glfw

> Note: currently untested on anything apart from Linux.

Build2 package for the GLFW graphics library.

<!-- [![build2](/actions/workflows/build2.yml/badge.svg)](/actions/workflows/build2.yml) -->

## Configuration

This package provides user configuration variables directly in with the build system.
The following configuration variables are current supported:

- `config.glfw.build_wayland` (default true): Include Wayland support.
- `config.glfw.build_x11` (default true): Include X11 support.
- `config.glfw.usehybridhpg` (default false): Use hybrid high performance graphics card.
<!-- - `config.glfw.vulkan` (default false): Statically link with vulkan libraries -->


## Default setup on Linux

Uses both X11 and Wayland by default when building on linux. This requires `wayland-scanner` to be installed on the system (`wayland-protocols` is not required).
