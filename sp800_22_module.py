
#!/usr/bin/env python
# sp800_22_tests.py
# 
# Copyright (C) 2017 David Johnston
# This program is distributed under the terms of the GNU General Public License.
# 
# This file is part of sp800_22_tests.
# 
# sp800_22_tests is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# sp800_22_tests is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with sp800_22_tests.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import print_function
import argparse
import sys
def run_tests(bits):

    testlist = [
            'monobit_test',
            'frequency_within_block_test',
            'runs_test',
            'longest_run_ones_in_a_block_test',
            'binary_matrix_rank_test',
            'dft_test',
            'non_overlapping_template_matching_test',
            'overlapping_template_matching_test',
            'maurers_universal_test',
            'linear_complexity_test',
            'serial_test',
            'approximate_entropy_test',
            'cumulative_sums_test',
            'random_excursion_test',
            'random_excursion_variant_test']
    gotresult=False

    results = list()        
    for testname in testlist:
        print("TEST: %s" % testname)
        m = __import__ ("sp800_22_"+testname)
        func = getattr(m,testname)
        
        (success,p,plist) = func(bits)

        summary_name = testname
        if success:
            print("  PASS")
            summary_result = "PASS"
        else:
            print("  FAIL")
            summary_result = "FAIL"
        
        if p != None:
            print("  P="+str(p))
            summary_p = str(p)
            
        if plist != None:
            for pval in plist:
                print("P="+str(pval))
            summary_p = str(min(plist))
        
        results.append((summary_name,summary_p, summary_result))

    print()
    print("SUMMARY")
    print("-------")
    
    for result in results:
        (summary_name,summary_p, summary_result) = result
        print(summary_name.ljust(40),summary_p.ljust(18),summary_result) 
    return results 
