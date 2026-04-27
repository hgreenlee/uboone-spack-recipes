# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Larlite(MakefilePackage):
    """LArLite event data format and lightweight analysis framework."""

    homepage = "https://github.com/uboone/larlite"
    url = "https://github.com/uboone/larlite/archive/refs/tags/v06_71_00a.tar.gz"
    git = "https://github.com/uboone/larlite.git"

    license("UNKNOWN")

    version("trunk", branch="trunk")
    version("06.71.00a", sha256="0099f77a99941c72b72d0d0fb69984ebbd0e444fa2cc631679a6ab8d0102e4b4")

    depends_on("cxx", type="build")
    depends_on("gmake", type="build")
    depends_on("python", type=("build", "run"))
    depends_on("root", type=("build", "link", "run"))

    phases = ("build", "install")

    def setup_build_environment(self, env):
        base = self.stage.source_path

        env.set("LARLITE_BASEDIR", base)
        env.set("LARLITE_LIBDIR", join_path(base, "lib"))
        env.set("LARLITE_COREDIR", join_path(base, "core"))
        env.set("LARLITE_USERDEVDIR", join_path(base, "UserDev"))
        env.set("USER_MODULE", "")

        env.set("LARLITE_CXX", self.compiler.cxx)
        env.set("LARLITE_CXXSTDFLAG", "-std=c++11")
        env.set("LARLITE_ROOT6", "1")
        env.set("ROOTSYS", self.spec["root"].prefix)

        env.prepend_path("PATH", self.spec["root"].prefix.bin)
        env.prepend_path("PATH", self.spec["python"].prefix.bin)
        env.prepend_path("PYTHONPATH", self.spec["root"].prefix.lib)

        mkdirp(join_path(base, "lib"))

    def build(self, spec, prefix):
        python = spec["python"].command
        python(join_path(self.stage.source_path, "config", "python", "gen_usermakefile.py"))
        python(join_path(self.stage.source_path, "config", "python", "gen_topmakefile.py"))
        make()

    def install(self, spec, prefix):
        install_tree(self.stage.source_path, prefix)

    def setup_run_environment(self, env):
        env.set("LARLITE_BASEDIR", self.prefix)
        env.set("LARLITE_LIBDIR", join_path(self.prefix, "lib"))
        env.set("LARLITE_COREDIR", join_path(self.prefix, "core"))
        env.set("LARLITE_USERDEVDIR", join_path(self.prefix, "UserDev"))

        env.prepend_path("PATH", join_path(self.prefix, "bin"))
        env.prepend_path("LD_LIBRARY_PATH", join_path(self.prefix, "lib"))
        env.prepend_path("PYTHONPATH", join_path(self.prefix, "python"))

    def url_for_version(self, version):
        return f"https://github.com/uboone/larlite/archive/refs/tags/v{str(version).replace('.', '_')}.tar.gz"
