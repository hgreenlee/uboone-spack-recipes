# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *

class Fememulator(Package):
    """MicroBooNE FEM-based beam trigger emulator and software trigger algorithms."""

    homepage = "https://github.com/uboone/fememulator"
    url = "https://github.com/uboone/fememulator/archive/refs/tags/v02_03_00.tar.gz"
    git = "https://github.com/uboone/fememulator.git"

    license("UNKNOWN")

    version("develop", branch="master")
    version("02.03.00", sha256="47be2db01c26f7fb0af790bfed674b4b6e79f3b7f84b2b7327692358f3860668")

    depends_on("cmake@2.8:", type="build")
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("root", type=("build", "link", "run"))
    depends_on("boost", type=("build", "link", "run"))
    depends_on("larlite", type=("build", "link", "run"))

    phases = ("build", "install") 

    def setup_build_environment(self, env):
        env.set("SWTRIGGER_BUILDDIR", join_path(self.stage.source_path, "build"))
        env.set("SWTRIGGER_INCDIR", self.stage.source_path)
        env.set("SWTRIGGER_LIBDIR", join_path(self.stage.source_path, "build", "lib"))
        env.set("SWTRIGGER_CXX", os.path.basename(self.compiler.cxx))
        env.set("SWTRIGGER_ROOT6", "1")

    def build(self, spec, prefix):
        mkdirp(join_path(self.stage.source_path, 'build'))
        with working_dir(join_path(self.stage.source_path, 'build')):
            cmake = Executable('cmake')
            cmake('-DCMAKE_INSTALL_PREFIX=%s/build' % prefix, '../' )
            make()


    def install(self, spec, prefix):
        install_tree(self.stage.source_path, prefix)

    def url_for_version(self, version):
        return f"https://github.com/uboone/fememulator/archive/refs/tags/v{str(version).replace('.', '_')}.tar.gz"
