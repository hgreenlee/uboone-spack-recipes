# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Larcv(Package):
    """Liquid Argon Computer Vision data format and image processing framework."""

    homepage = "https://github.com/LArbys/LArCV"
    url = "https://github.com/LArbys/LArCV/archive/refs/tags/v06_71_00c.tar.gz"
    git = "https://github.com/LArbys/LArCV.git"

    license("UNKNOWN")

    version("develop", branch="ubdl_dev")
    version("2.me.06.03.prod.01", commit="0c0c1f90497e64e697f2cbf01ffba9f34da9cada")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake", type="build")
    depends_on("gmake", type="build")
    depends_on("python", type=("build", "run"))
    depends_on("root", type=("build", "link", "run"))
    depends_on("boost", type=("build", "link", "run"))
    depends_on("eigen", type=("build", "link", "run"))
    depends_on("opencv@:3+imgproc+imgcodecs", type=("build", "link", "run"))
    depends_on("geo2d", type=("build", "link", "run"))
    depends_on("py-torch", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-pyzmq", type=("build", "run"))

    phases = ("build", "install")

    def patch(self):
        filter_file('find_package\( Torch \)',
                'find_package( Torch REQUIRED)',
                CMakeLists.txt)

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

        env.set("OPENCV_INCDIR", self.spec["opencv"].prefix.include)
        env.set("OPENCV_LIBDIR", self.spec["opencv"].prefix.lib)
        env.set("LIBTORCH_INCDIR", self.spec["py-torch"].prefix.include)
        env.set("LIBTORCH_LIBDIR", self.spec["py-torch"].prefix.lib)

        env.prepend_path("PATH", self.spec["root"].prefix.bin)
        env.prepend_path("PATH", self.spec["python"].prefix.bin)

        mkdirp(join_path(self.stage.source_path, "build", "lib"))
        mkdirp(join_path(self.stage.source_path, "build", "bin"))
        mkdirp(join_path(self.stage.source_path, "build", "include"))
        env.prepend_path("PATH", join_path(self.stage.source_path, "bin"))

    def build(self, spec, prefix):
        set_executable(join_path(self.stage.source_path, 'configure.sh'))
        configure = Executable('%s/configure.sh' % self.stage.source_path)
        configure()
        with working_dir(join_path(self.stage.source_path, 'build')):
            cmake = Executable('cmake')
            cmake('-DUSE_PYTHON3=ON', '-DUSE_OPENCV=ON', '-DLARCV_ANN=ON', '-DUSE_TORCH=ON', '%s' % self.stage.source_path )
            make()
            make('install')

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

