#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import sys
import time
from optparse import OptionParser
sys.path.append("/home/zhaibingbing/workdir/03.Software/PYTHONPATH/lib/python2.7/site-packages")
import pysam

version = 1.1


if __name__ == '__main__':

    usage = 'usage: %prog [options]'
    description = "To caculate statistics aganist bam; including 'Nucleic acid quality and quantity' 'Library qualification and quantification' 'Depth of coverage' 'Uniformity of coverage' 'GC bias' 'Cluster density and alignment rate(>95%' 'Base call quality scores' 'Mapping quality' 'Duplication rate' 'Strand bias'"
    epilog = """
Bed-based statistics types(accroding the bed region):

    *[Total] Library Peak Size(bp)
    *[Total] Library IQR size(bp)
    *[Total] Raw Reads (All reads)
    *[Total] Raw Reads Rmdup (All reads)
    *[Total] Raw Data(Mb)
    *[Total] Raw Data Rmdup(Mb)
    *[Total] Average Len of Reads(bp)
    *[Total] Average Len of Reads Rmdup(bp)
    *[Total] Fraction of Mapped Reads
    *[Total] Fraction of Mapped Reads Rmdup
    *[Total] Fraction of Duplicate Reads
    *[Total] Fraction of Duplicate Reads Rmdup
    *[Total] Fraction of hotspot Coverage >=3000x
    *[Target] Len of target region(bp)
    *[Target] Len of Mapped Target region(bp)
    *[Target] Len of Mapped Target region Rmdup(bp)
    *[Target] Fraction of Mapped Target region
    *[Target] Fraction of Mapped Target region Rmdup
    *[Target] Fraction of Uniquely mapped Reads in Target mapped reads
    *[Target] Target Data(Mb)
    *[Target] Target Data Rmdup(Mb)
    *[Target] Fraction of Target Data in all data
    *[Target] Fraction of Target Data in all data Rmdup
    *[Target] Average depth
    *[Target] Average depth Rmdup
    *[Target] Fraction of target Coverage >=5000x
    *[Target] Fraction of target Coverage Rmdup >=5000x
    *[Target] Fraction of target Coverage >=1000x
    *[Target] Fraction of target Coverage Rmdup >=1000x
    *[Target] Fraction of target Coverage >=200x
    *[Target] Fraction of target Coverage Rmdup >=200x
    *[Flank] Len of Flank region(bp)
    *[Flank] Len of Mapped Flank region(bp)
    *[Flank] Fraction of Mapped Flank region
    *[Flank] Flank Data(Mb)
    *[Flank] Average depth
    *[Flank] Fraction of flank Coverage >=5000x
    *[Flank] Fraction of flank Coverage >=1000x
    *[Flank] Fraction of flank Coverage >=200x
    *[Target And Flank] Target And Flank Data(Mb)
    *[Target And Flank] Fraction of Target Data And Flank Data in all data

Examples:
    
    
Version: {version} (pysam: {pysamversion})
""".format(version = version,pysamversion = pysam.__version__)

    OptionParser.format_epilog = lambda self, formatter:self.epilog
    parser = OptionParser(usage = usage, description = description, epilog = epilog)
    
    parser.add_option("-s", "--sort", dest="sort", default=None, help="The raw sorted bam (0-based), required")
    parser.add_option("-r", "--rmdup", dest="rmdup", default=None, help="The rmdup bam (0-based), required")
    parser.add_option("-m", "--markdup", dest="markdup", default=None, help="The markdup bam (0-based), required")
    parser.add_option("-o", "--outdir", dest="outdir", default="./", help="The out directory set, default=./")
    parser.add_option("-t", "--target", dest="target", default=None, help="The target region bed file, required")
    parser.add_option("-p", "--hotspot", dest="hotspot", default=None, help="The hotspot snp and indel file")
    parser.add_option("-D", "--hotspotdepth", dest="hotspotdepth", default=3000, help="The hotspot depth value cutoff, default=3000")
    parser.add_option("-d", "--depth", dest="depth", default=[200,1000,5000], help="The depth value cutoff for target region, default=[200,1000,5000]")
    
    options, args = parser.parse_args()
    
    if len(args) > 0:
        parser.error("Using formal parameters please") 

    if not os.path.exists(options.outdir):
        os.mkdir(options.outdir)
    
      
