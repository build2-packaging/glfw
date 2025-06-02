#include <GLFW/glfw3.h>

#undef NDEBUG
#include <assert.h>

int
main ()
{
  assert (glfwInit () == GLFW_TRUE);
}
