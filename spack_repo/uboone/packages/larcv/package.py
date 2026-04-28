# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Larcv(MakefilePackage):
    """Liquid Argon Computer Vision data format and image processing framework."""

    homepage = "https://github.com/uboone/LArCV"
    url = "https://github.com/uboone/LArCV/archive/refs/tags/v06_71_00c.tar.gz"
    git = "https://github.com/uboone/LArCV.git"

    license("UNKNOWN")

    version("develop", branch="develop")
    version("06.71.00c", sha256="3694afa0c2320360d40a6a65f7f05f2cb0dfae276ab05b5f2c167fd8dc59f766")

    depends_on("cxx", type="build")
    depends_on("gmake", type="build")
    depends_on("python", type=("build", "run"))
    depends_on("root", type=("build", "link", "run"))
    depends_on("boost", type=("build", "link", "run"))

    phases = ("build", "install")

    def setup_build_environment(self, env):
        env.set("LARCV_BASEDIR", self.stage.source_path)
        env.set("LARCV_BUILDDIR", join_path(self.stage.source_path, "build"))
        env.set("LARCV_COREDIR", join_path(self.stage.source_path, "core"))
        env.set("LARCV_APPDIR", join_path(self.stage.source_path, "app"))
        env.set("LARCV_LIBDIR", join_path(self.stage.source_path, "build", "lib"))
        env.set("LARCV_INCDIR", join_path(self.stage.source_path, "build", "include"))
        env.set("LARCV_BINDIR", join_path(self.stage.source_path, "build", "bin"))

        env.set("LARCV_CXX", self.compiler.cxx)
        env.set("LARCV_ROOT6", "1")
        env.set("LARCV_NUMPY", "0")
        env.set("LARCV_OPENCV", "0")
        env.set("LARCV_ANN", "0")

        env.set("BOOST_INC", self.spec["boost"].prefix.include)
        env.set("BOOST_LIB", self.spec["boost"].prefix.lib)

        env.prepend_path("PATH", self.spec["root"].prefix.bin)
        env.prepend_path("PATH", self.spec["python"].prefix.bin)

        mkdirp(join_path(self.stage.source_path, "build", "lib"))
        mkdirp(join_path(self.stage.source_path, "build", "bin"))
        mkdirp(join_path(self.stage.source_path, "build", "include"))
        env.prepend_path("PATH", join_path(self.stage.source_path, "bin"))

    def build(self, spec, prefix):
        make()

    def install(self, spec, prefix):
        install_tree(self.stage.source_path, prefix)

    def setup_run_environment(self, env):
        env.set("LARCV_BASEDIR", self.prefix)
        env.set("LARCV_BUILDDIR", join_path(self.prefix, "build"))
        env.set("LARCV_COREDIR", join_path(self.prefix, "core"))
        env.set("LARCV_APPDIR", join_path(self.prefix, "app"))
        env.set("LARCV_LIBDIR", join_path(self.prefix, "build", "lib"))
        env.set("LARCV_INCDIR", join_path(self.prefix, "build", "include"))
        env.set("LARCV_BINDIR", join_path(self.prefix, "build", "bin"))

        env.prepend_path("PATH", join_path(self.prefix, "bin"))
        env.prepend_path("PATH", join_path(self.prefix, "build", "bin"))
        env.prepend_path("PYTHONPATH", join_path(self.prefix, "python"))
        env.prepend_path("LD_LIBRARY_PATH", join_path(self.prefix, "build", "lib"))

    def url_for_version(self, version):
        return f"https://github.com/uboone/LArCV/archive/refs/tags/v{str(version).replace('.', '_')}.tar.gz"
