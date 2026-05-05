# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Cilantro(CMakePackage):
    """Point cloud processing and geometric estimation library."""

    homepage = "https://github.com/NuTufts/cilantro"
    git = "https://github.com/NuTufts/cilantro.git"

    license("MIT")

    version("2.me.06.03.prod.01", commit="b4a1b71bae8d7fbe6616ec54375617ce4bb4f34e")

    depends_on("cmake", type="build")
    depends_on("gmake", type="build")
    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("eigen", type=("build", "link", "run"))

    def setup_dependent_build_environment(self, env, dependent_spec):
        env.set("CILANTRO_LIB_DIR", join_path(self.prefix, "lib", "cmake", "cilantro"))

    def setup_run_environment(self, env):
        env.set("CILANTRO_LIB_DIR", join_path(self.prefix, "lib", "cmake", "cilantro"))
        env.prepend_path("LD_LIBRARY_PATH", join_path(self.prefix, "lib"))

    def cmake_args(self):
        return [
            self.define("BUILD_EXAMPLES", False),
        ]