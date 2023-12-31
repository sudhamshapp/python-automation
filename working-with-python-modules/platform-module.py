# the platform module is to access the underlying platform data such as hardware, os, and interpreter version info
import platform
print(dir(platform))
print(len(dir(platform)))
print(platform.platform())
print(help(platform))
print(f"this is {platform.platform()} os")
print(platform.system())
# print(help(platform))
print(platform.python_version())
print(platform.machine())
print(platform.release())
print(platform.processor())
print(platform.architecture())
print(platform.uname())
