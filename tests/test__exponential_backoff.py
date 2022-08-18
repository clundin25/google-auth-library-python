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
    curr_wait = eb._current_wait_in_seconds
    iteration_count = 1

    try:
        for attempt in eb:
            backoff_interval = mock_time.call_args[0][0]
            jitter = curr_wait * eb._randomization_factor

            assert curr_wait <= backoff_interval <= (curr_wait + jitter)
            assert attempt == iteration_count
            assert eb._backoff_count == iteration_count
            assert eb._current_wait_in_seconds == eb._multiplier ** iteration_count

            curr_wait = eb._current_wait_in_seconds
            iteration_count += 1
        assert (
            False
        )  # We should hit the retry error exception since this loop is unbounded.
    except exceptions.RetryError:
        assert iteration_count == _exponential_backoff._DEFAULT_RETRY_TOTAL_ATTEMPTS
    assert mock_time.call_count == _exponential_backoff._DEFAULT_RETRY_TOTAL_ATTEMPTS
