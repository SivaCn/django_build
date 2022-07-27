# -*- coding: utf-8 -*-

"""

    Module :mod:``


    LICENSE: The End User license agreement is located at the entry level.

"""

# ----------- START: Namespace Imports ---------- #
__import__('pkg_resources').declare_namespace(__name__)
# ----------- END: Namespace Imports ---------- #

# ----------- START: Native Imports ---------- #
import os
# ----------- END: Native Imports ---------- #

# ----------- START: Third Party Imports ---------- #
from configparser import ConfigParser
# ----------- END: Third Party Imports ---------- #

# ----------- START: In-App Imports ---------- #
# ----------- END: In-App Imports ---------- #

__all__ = [
    # All public symbols go here.
]


def get_build_path():
    return os.environ['BUILD_HOME']


class CustomConfigParser(object):
    """A custom class to read the config inputs"""

    def __init__(self, filename=None):
        """Initialization Block.

        Args:
            filename (``str``): config file to be parsed

        """
        self.config_file_path = os.path.join(
            get_build_path(), 'parts', 'config', filename or 'config.ini'
        )

        self.config = ConfigParser(interpolation=None)
        self.config.read(self.config_file_path)

    def normalize_value(self, value):

        if isinstance(value, str):
            value = value.strip()

        #
        # Try Auto Casting into integer if the value part is digit
        if isinstance(value, str) and value.isdigit():
            value = int(value)

        if isinstance(value, str):

            #
            # Mark the values into booleans if deserved
            if value.lower() == 'true':
                value = True
            elif value.lower() == 'false':
                value = False

        return value

    def parse(self):

        _config = dict()

        for section in self.config.sections():
            _config[section] = {
                _option: self.normalize_value(self.config.get(section, _option))
                for _option in self.config.options(section)
            }

        return _config


def get_build_settings():

    """Get build level settings."""

    return CustomConfigParser().parse()
