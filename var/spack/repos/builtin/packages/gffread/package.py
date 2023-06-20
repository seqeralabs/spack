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
    url = "https://github.com/gpertea/gffread/archive/refs/tags/v0.12.7.zip"

    version("0.12.7", sha256="93921c27f7560d728122855ab1f0bb034ba569fb1a5c8a89043122cdedef34c2")

    executables = ["gffread"]

    def install(self, spec, prefix):
        make("../gclib")
        make("release")
        mkdirp(prefix.bin)
        install("gffread", prefix.bin)

