# CC0, originally by monomere
# A utility script to create symlinks from the upstream into
# the build2 source directories. This only needs to be ran
# once per GLFW update (if they create/move/delete/... files)
# by the person updating the package.

import shutil, fnmatch, os.path, os

blacklist = {"CMake*", ".*"} # both files and directories.
whitelist = {"*.[hmc]", "*.png", "*.md"} # files only.

dirs = {
	"./upstream/src":          "./glfw/src",
	"./upstream/include/GLFW": "./glfw/include/GLFW",
	"./upstream/tests":        "./glfw-tests",
	"./upstream/examples":     "./glfw-examples",
	"./upstream/deps":         "./glfw-examples/deps",
	"./upstream/README.md":    "./glfw-examples/README.md",
	"./upstream/LICENSE.md":   "./glfw-examples/LICENSE.md",
	"./upstream/deps":         "./glfw-tests/deps",
	"./upstream/README.md":    "./glfw-tests/README.md",
	"./upstream/LICENSE.md":   "./glfw-tests/LICENSE.md",
}


def matches_any(name: str, pats: set[str]) -> bool:
	return any((fnmatch.fnmatch(name, pat) for pat in pats))


def unlink_file(target_file: str):
	if     matches_any(os.path.basename(target_file), blacklist): return
	if not matches_any(os.path.basename(target_file), whitelist): return

	link_path = os.path.normpath(os.path.join(
		os.path.dirname(target_file),
		os.readlink(target_file)
	))
	print(f"{link_path:<48} -x- {target_file}")
	os.unlink(target_file)


def unlink_dir(target_dir: str):
	'''Remove all links from target matching the whitelist.'''

	if not os.path.exists(target_dir): return
	if matches_any(os.path.basename(target_dir), blacklist): return

	print(f"{'':<48} -x- {target_dir}/")

	for name in os.listdir(target_dir):
		target_name = os.path.join(target_dir, name)
		if os.path.islink(target_name): unlink_file(target_name)
		elif os.path.isdir(target_name): unlink_dir(target_name)


def link_file(source_file: str, target_file: str):
	if     matches_any(os.path.basename(source_file), blacklist): return
	if not matches_any(os.path.basename(source_file), whitelist): return

	print(f"{source_file:<48} --> {target_file}")

	try:
		os.symlink(
			os.path.relpath(source_file, os.path.dirname(target_file)),
			target_file
		)
	except FileExistsError:
		print(f"file exists, skipping.")


def link_dir(source_dir: str, target_dir: str):
	'''Create all links from source to target.'''

	if matches_any(os.path.basename(source_dir), blacklist): return

	os.makedirs(target_dir, exist_ok=True)

	print(f"{source_dir + '/':<48} --> {target_dir}/")

	for name in os.listdir(source_dir):
		source_name = os.path.join(source_dir, name)
		target_name = os.path.join(target_dir, name)

		if os.path.isfile(source_name): link_file(source_name, target_name)
		elif os.path.isdir(source_name): link_dir(source_name, target_name)


def main():
	for target_name in dirs.values():
		if os.path.isdir(target_name):
			unlink_dir(target_name)
		elif os.path.islink(target_name):
			unlink_file(target_name)

	# for source_name, target_name in dirs.items():
	# 	if os.path.isdir(source_name):
	# 		link_dir(source_name, target_name)
	# 	elif os.path.isfile(source_name):
	# 		link_file(source_name, target_name)


if __name__ == '__main__': exit(main() or 0)
