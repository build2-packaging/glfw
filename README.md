# GLFW - Multi-platform library for OpenGL, OpenGL ES and Vulkan development on the desktop.

This is a [`build2`](https://build2.org/) package repository for [`GLFW`](https://github.com/glfw/glfw)

This file contains setup instructions and other details that are more appropriate for development rather than consumption. If you want to use [`GLFW`](https://github.com/glfw/glfw) in your [`build2`](https://build2.org/)-based project, then instead see the accompanying [`PACKAGE-README.md`](glfw/PACKAGE-README.md) file.

The development setup for [`GLFW`](https://github.com/glfw/glfw) uses the standard [`bdep`](https://build2.org/bdep/doc/bdep.xhtml)-based workflow. For example:

```
git clone .../glfw.git
cd glfw

bdep init -C @gcc cc config.cxx=g++
bdep update
bdep test
```

### Notes for Linux and BSD-based systems

On **FreeBSD** and **Linux**, you must set at least one of the following configuration variables during `bdep init`:

* `config.glfw.build_wayland=true` — to enable Wayland support
* `config.glfw.build_x11=true` — to enable X11 support

It is valid to set both to `true`.

### Installing required system dependencies

#### Fedora

On Fedora, you can use bdep to install the required system packages. For example:

```
bdep init -C @gcc cc config.cxx=g++ -- config.glfw.build_x11=true \
  --sys-install --sys-no-stub sys:libXcursor                      \
                              sys:libXi                           \
                              sys:libXinerama                     \
                              sys:libXrandr                       \
                              sys:libxkbcommon                    \
                              sys:mesa-libGL
```

#### Debian

On **Debian 12** and **later**, the required development packages are typically already available. If not, they can be installed using bdep exactly as shown above for Fedora. The package names are identical and fully compatible with build2's system package support.

#### Other distributions

Finally, on **other Linux distributions**, you may need to install the equivalent development packages manually. Refer to your system's package manager for how to install the following libraries:

* libXcursor
* libXi
* libXinerama
* libXrandr
* libxkbcommon
* mesa-libGL

###### Wayland

* libwayland
