# Copyright 2016 Google LLC
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

"""Google OAuth 2.0 Library for Python."""

import sys
import warnings

class Python37DeprecationWarning(DeprecationWarning):
    """
    Deprecation warning raised when Python 3.7 runtime is detected.
    Python 3.7 support will be dropped after October 1, 2023. See
    https://cloud.google.com/python/docs/python37-sunset/ for more information.
    """
    pass

class Python36DeprecationWarning(DeprecationWarning):
    """
    Deprecation warning raised when Python 3.6 runtime is detected.
    Python 3.6 support will be dropped after October 1, 2023.
    """
    pass

# Checks if the current runtime is Python 3.7.
if sys.version_info.major == 3 and sys.version_info.minor == 7:
    message = (
        "After October 1, 2023, new releases of this library will drop support "
        "for Python 3.7. More details about Python 3.7 support for Client Libraries "
        "can be found at https://cloud.google.com/python/docs/python37-sunset/"
    )
    # Configure the Python37DeprecationWarning warning so that it is only emitted once.
    warnings.simplefilter('once', Python37DeprecationWarning)
    warnings.warn(message, Python37DeprecationWarning)

# Checks if the current runtime is Python 3.6.
if sys.version_info.major == 3 and sys.version_info.minor == 6:
    message = (
        "After October 1, 2023, new releases of this library will drop support "
        "for Python 3.6."
    )
    # Configure the Python36DeprecationWarning warning so that it is only emitted once.
    warnings.simplefilter('once', Python36DeprecationWarning)
    warnings.warn(message, Python36DeprecationWarning)
