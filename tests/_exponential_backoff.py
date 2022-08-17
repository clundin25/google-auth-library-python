# Copyright 2014 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import mock
import pytest  # type: ignore

from google.auth import _exponential_backoff
from google.auth import exceptions


@mock.patch("time.sleep", return_value=None)
def test_exponential_backoff(mock_time):
    eb = _exponential_backoff.ExponentialBackoff()
    count = 1
    try:
        for _ in eb:
            backoff_interval = mock_time.call_args[0][0]
            assert (
                (eb._current_wait_in_seconds - eb._jitter)
                < backoff_interval
                < (eb._current_wait_in_seconds + eb._jitter)
            )

            count += 1
        assert (
            False
        )  # We should hit the retry error exception since this loop is unbounded.
    except exceptions.RetryError:
        assert count == _exponential_backoff._DEFAULT_RETRY_TOTAL_ATTEMPTS
    assert mock_time.call_count == _exponential_backoff._DEFAULT_RETRY_TOTAL_ATTEMPTS
