#    Copyright (c) 2016 Mirantis, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
import testtools

from muranodashboard.dynamic_ui import helpers


class TestHelper(testtools.TestCase):
    def test_to_str(self):
        names = ['string', b'ascii', u'ascii',
                 u'\u043d\u0435 \u0430\u0441\u043a\u0438']
        for name in names:
            self.assertIsInstance(helpers.to_str(name), str)

    def test_int2base(self):
        for x in range(30):
            self.assertEqual("{0:b}".format(x), helpers.int2base(x, 2))
            self.assertEqual("{0:o}".format(x), helpers.int2base(x, 8))
            self.assertEqual("{0:x}".format(x), helpers.int2base(x, 16))
