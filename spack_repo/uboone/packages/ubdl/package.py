# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Ubdl(MakefilePackage):
    """MicroBooNE deep-learning reconstruction chain meta-repository."""

    homepage = "https://github.com/LArbys/ubdl"
    url = "https://github.com/LArbys/ubdl/archive/refs/tags/v2_me_06_03_prod_01.tar.gz"
    git = "https://github.com/LArbys/ubdl.git"

    license("UNKNOWN")

    phases = ("build", "install")

    version("trunk", branch="master")
    version("2.me.06.03.prod.01", tag="v2_me_06_03_prod_01", submodules=True)

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("python", type=("build", "run"))
    depends_on("root", type=("build", "link", "run"))
    depends_on("boost", type=("build", "link", "run"))
    depends_on("eigen", type=("build", "link", "run"))
    depends_on("opencv", type=("build", "link", "run"))
    depends_on("py-torch", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-pyzmq", type=("build", "run"))
    depends_on("larlite", type=("build", "link", "run"))
    depends_on("larcv", type=("build", "link", "run"))

    def build(self, spec, prefix):
        set_executable('%s/buildall_fnal.sh' % self.stage.source_path)
        build_script = Executable('%s/buildall_fnal.sh' % self.stage.source_path)
        build_script()

    def install(self, spec, prefix):
        install_tree(self.stage.source_path, prefix)

    def setup_run_environment(self, env):
        env.set("UBDL_BASEDIR", self.prefix)
        env.prepend_path("PATH", join_path(self.prefix, "scripts"))

        env.prepend_path("PYTHONPATH", join_path(self.prefix, "python"))
        env.prepend_path("PYTHONPATH", join_path(self.prefix, "ublarcvserver", "python"))
        env.prepend_path("PYTHONPATH", join_path(self.prefix, "ublarcvserver", "networks", "infill"))

    def url_for_version(self, version):
        return f"https://github.com/LArbys/ubdl/archive/refs/tags/v{str(version).replace('.', '_')}.tar.gz"
