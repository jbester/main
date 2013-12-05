#####################################################################################
#
#  Copyright (c) Jeffrey Bester. All rights reserved.
#
# This source code is subject to terms and conditions of the Apache License, Version 2.0. A
# copy of the license can be found in the License.html file at the root of this distribution. If
# you cannot locate the  Apache License, Version 2.0, please send an email to
# ironpy@microsoft.com. By using this source code in any fashion, you are agreeing to be bound
# by the terms of the Apache License, Version 2.0.
#
# You must not remove this notice, or any other, from this software.
#
#
#####################################################################################

from iptest.assert_util import *
import io

def test_read():
	# test stringio is readable
	with io.StringIO("hello world\r\n") as infile:
		SequencesAreEqual(infile.readline(), "hello world\r\n")

def test_seekable():
	# test stringio is seekable
	with io.StringIO("hello") as infile:
		infile.seek(0, 2)
		infile.write(" world\r\n")
		SequencesAreEqual(infile.getvalue(), "hello world\r\n")

def test_write():
	# test stringio is writable
	with io.StringIO() as output_file:
		output_file.write("hello")
		output_file.write(" world\n")
		SequencesAreEqual(output_file.getvalue(), "hello world\n")

run_test(__name__)
