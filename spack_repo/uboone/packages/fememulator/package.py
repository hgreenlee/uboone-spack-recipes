# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Fememulator(CMakePackage):
    """MicroBooNE FEM-based beam trigger emulator and software trigger algorithms."""

    homepage = "https://github.com/uboone/fememulator"
    url = "https://github.com/uboone/fememulator/archive/refs/tags/v02_03_00.tar.gz"
    git = "https://github.com/uboone/fememulator.git"

    license("UNKNOWN")

    version("develop", branch="master")
    version("02.03.00", sha256="47be2db01c26f7fb0af790bfed674b4b6e79f3b7f84b2b7327692358f3860668")

    depends_on("cmake@2.8:", type="build")
    depends_on("cxx", type="build")

    variant(
        "cxxstd",
        default="17",
        values=("14", "17", "20"),
        multi=False,
        description="Use the specified C++ standard when building.",
    )

    @cmake_preset
    def cmake_args(self):
        args = [
            self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"),
        ] 
        return args

    def url_for_version(self, version):
        return f"https://github.com/uboone/fememulator/archive/refs/tags/v{str(version).replace('.', '_')}.tar.gz"
