# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Gffread(Package):
    """GFF/GTF utility providing format conversions, region filtering, FASTA sequence extraction and more.

    GTF (Gene Transfer Format) and GFF (General Feature Format) are popular
    file formats used by bioinformatics programs to represent and exchange
    information about various genomic features, such as gene and transcript
    locations and structure. GffRead and GffCompare are open source programs
    that provide extensive and efficient solutions to manipulate files in a GTF
    or GFF format. While GffRead can convert, sort, filter, transform, or
    cluster genomic features, GffCompare can be used to compare and merge
    different gene annotations."""

    homepage = "http://ccb.jhu.edu/software/stringtie/gff.shtml"
    url = "https://github.com/gpertea/gffread/archive/refs/tags/v0.12.7.tar.gz"

    version("0.12.7", sha256="6f3417090b3beb74f435bf5d462c87475b3c704a8a0d71821f6c1321c47dbbbe")

    # Not sure whether gclib and gffread versions should match to work. Tried matching 0.12.1 but
    # gffread breaks. It seems gclib is a repo storing shared header files, and a new version is
    # cut on all dependencies when a new version of the library is made. Force match for now.
    depends_on("gclib@0.12.7", when="@0.12.7", type=("build", "link"))

    phases = ["build", "install"]
    executables = ["gffread"]

    def setup_build_environment(self, env):
        env.set("GCLDIR", self.spec['gclib'].prefix.include)

    def build(self, spec, prefix):
        make("gffread")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install("gffread", prefix.bin)

