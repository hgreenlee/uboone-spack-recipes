# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Geo2d(CMakePackage):
    """2D geometry and ROOT dictionary utilities used by LArCV/UBDL."""

    homepage = "https://github.com/LArbys/Geo2D"
    git = "https://github.com/LArbys/Geo2D.git"

    license("UNKNOWN")

    version("master", branch="master")
    version("2.me.06.03.prod.01", commit="ff2a2d13d7fa19d1a50d0a9b81df091095a92305")

    depends_on("cmake@3.10:", type="build")
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("root", type=("build", "link", "run"))
    depends_on("opencv", type=("build", "link", "run"))
    depends_on("python@3:", type=("build", "link", "run"))
    depends_on("py-numpy", type=("build", "run"))

    def cmake_args(self):
        args = [
            self.define("USE_PYTHON3", True),
            self.define("USE_PYTHON2", False),
            self.define("GIT_SUBMODULE", False),
        ]
        return args
