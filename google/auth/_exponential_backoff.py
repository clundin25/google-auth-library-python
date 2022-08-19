# Copyright 2021 Google LLC
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

import time
import random

from google.auth import exceptions

# The default amount of retry total_attempts
_DEFAULT_RETRY_TOTAL_ATTEMPTS = 3

# The default initial backoff period (1.0 second).
_DEFAULT_INITIAL_INTERVAL_MILLIS = 1000

# The default randomization factor (1.1 which results in a random period ranging
# between 10% below and 10% above the retry interval).
_DEFAULT_RANDOMIZATION_FACTOR = 0.1

# The default multiplier value (2 which is 100% increase per back off).
_DEFAULT_MULTIPLIER = 2.0

# Todo: Add a note about reusing
class ExponentialBackoff(object):
    def __init__(
        self,
        *,
        total_attempts=_DEFAULT_RETRY_TOTAL_ATTEMPTS,
        initial_wait=_DEFAULT_INITIAL_INTERVAL_MILLIS,
        randomization_factor=_DEFAULT_RANDOMIZATION_FACTOR,
        multiplier=_DEFAULT_MULTIPLIER,
    ):
        self._total_attempts = total_attempts
        # convert milliseconds to seconds for the time.sleep API
        self._current_wait_in_seconds = initial_wait * 0.001
        self._randomization_factor = randomization_factor
        self._multiplier = multiplier
        self._backoff_count = 0

    def __iter__(self):
        return self

    def __next__(self):
        jitter_range = self._current_wait_in_seconds * self._randomization_factor
        jitter = random.uniform(0, jitter_range)

        time.sleep(self._current_wait_in_seconds + jitter)

        self._backoff_count += 1
        if self._backoff_count >= self._total_attempts:
            # TODO: Should we reset the backoff count here?
            raise exceptions.RetryError(
                f"Ran out of retry attempts. Tried a total of {self._backoff_count} "
                f"times but the configured total retry count is {self._total_attempts}."
            )

        self._current_wait_in_seconds *= self._multiplier
        return self._backoff_count

    @property
    def total_attempts(self):
        return self._total_attempts

    @property
    def backoff_count(self):
        return self._backoff_count
