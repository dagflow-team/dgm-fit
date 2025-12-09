from importlib.metadata import version

__version__ = version(__name__)

from .fit_result import FitResult
from .iminuit_minimizer import IMinuitMinimizer
from .minimizable import Minimizable

__all__ = [
    "FitResult",
    "IMinuitMinimizer",
    "Minimizable",
    "__version__",
]
