# Copyright 2020 Google LLC
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

"""An interface indicating if an exception is retryable.

A flag indicating whether the error is retryable

@return true if related error is retryable, false otherwise

  boolean isRetryable();
"""

import abc

import six


@six.add_metaclass(abc.ABCMeta)
class Retryable(object):
    @abc.abstractmethod
    def is_retryable(self):
        raise NotImplementedError("is_retryable must be implemented.")
