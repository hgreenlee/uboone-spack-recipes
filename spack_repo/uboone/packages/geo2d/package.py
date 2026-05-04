# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Geo2d(Package):
    """2D geometry and ROOT dictionary utilities used by LArCV/UBDL."""

    homepage = "https://github.com/LArbys/Geo2D"
    git = "https://github.com/LArbys/Geo2D.git"

    license("UNKNOWN")

    version("master", branch="master")
    version("2.me.06.03.prod.01", commit="642470be0694396c6eb000892c368fa0e592bb68")

    depends_on("gmake", type="build")
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("root", type=("build", "link", "run"))
    depends_on("opencv@:3+imgproc+imgcodes", type=("build", "link", "run"))
    depends_on("python@3:", type=("build", "link", "run"))
    depends_on("py-numpy", type=("build", "run"))

    phases = ("build", "install")


    def setup_build_environment(self, env):
        env.set("GEO2D_BASEDIR", self.stage.source_path)
        env.set("GEO2D_INCDIR", self.stage.source_path)
        env.set("GEO2D_LIBDIR", join_path(self.stage.source_path, "lib"))
        env.set("GEO2D_BINDIR", join_path(self.stage.source_path, "bin"))
        env.set("GEO2D_COREDIR", join_path(self.stage.source_path, "Geo2D", "core"))

        env.set("GEO2D_CXX", "c++")
        env.set("GEO2D_ROOT6", "1")
        env.set("GEO2D_PYTHON_VERSION", "3")
        env.set("GEO2D_PYTHON", "python3")

        env.set("OPENCV_INCDIR", self.spec["opencv"].prefix.include)
        env.set("OPENCV_LIBDIR", self.spec["opencv"].prefix.lib64)

        env.prepend_path("PATH", self.spec["root"].prefix.bin)
        env.prepend_path("PATH", self.spec["python"].prefix.bin)

        mkdirp(join_path(self.stage.source_path, "build", "lib"))
        mkdirp(join_path(self.stage.source_path, "build", "bin"))
        mkdirp(join_path(self.stage.source_path, "build", "include"))
        env.prepend_path("PATH", join_path(self.stage.source_path, "bin"))

    def build(self, spec, prefix):
        make('-j4')

    def install(self, spec, prefix):
        install_tree(self.stage.source_path, prefix)
