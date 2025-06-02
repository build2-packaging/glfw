# GLFW - A C library

This is a `build2` package for the [`GLFW`](https://github.com/glfw/glfw) C library. It provides a simple API for creating windows, contexts and surfaces, receiving input and events.


## Usage

To start using `GLFW` in your project, add the following [`depends`](https://build2.org/bpkg/doc/build2-package-manager-manual.xhtml#manifest-package-depends) value to your [`manifest`](https://build2.org/bpkg/doc/build2-package-manager-manual.xhtml#manifests), adjusting the version constraint as appropriate:

```
depends: GLFW ^3.4.0
```

Then import the library in your `buildfile`:

```
import libs += glfw%lib{glfw}
```


## Importable targets

This package provides the following importable targets:

```
lib{glfw}
```

### Importable targets description

* `glfw` - Multi-platform library for OpenGL, OpenGL ES and Vulkan development on the desktop.


## Configuration variables

This package provides the following configuration variables:

```
[bool] config.glfw.build_x11 ?= false
[bool] config.glfw.build_wayland ?= false
[bool] config.glfw.use_hybrid_hpg ?= false
[bool] config.glfw.use_msvc_runtime_library_dll ?= false
```

### Configuration variables description

* `build_x11` - Build support for X11.
* `build_wayland` - Build support for Wayland.
* `use_hybrid_hpg` - Force use of high-performance GPU on hybrid systems.
* `use_msvc_runtime_library_dll` - Use MSVC runtime library DLL
