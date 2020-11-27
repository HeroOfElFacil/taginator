from distutils.version import LooseVersion

from pkg_resources import get_distribution

__all__ = ["PACKAGE", "__version__"]


PACKAGE = get_distribution("taginator")

__version__ = LooseVersion(PACKAGE.version)