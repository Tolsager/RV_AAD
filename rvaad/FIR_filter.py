import numpy.typing as npt
import scipy
from scipy.linalg import hankel


class FIR:
    """Finds the optimal weights for the FIR model as described in
    'A Tutorial on Auditory Attention Identification Methods'
    They don't use padding so the output shape is different from
    """

    def __init__(self, filter_length: int):
        if type(filter_length) is not int:
            raise ValueError("filter_length is not of type int")  # noqa: TRY003
        self.fl = filter_length
        self.w = None

    def fit(self, x: npt.NDArray, y: npt.NDArray):
        if len(x) != len(y):
            raise ValueError("x and y are of different length")  # noqa: TRY003
        N = len(x)
        # generate the Hankel matrix
        H = hankel(x[: N - self.fl + 1], x[-self.fl :])
        self.w = scipy.linalg.pinv(H) @ y[self.fl - 1 :]

    def transform(self, x: npt.NDArray) -> npt.NDArray:
        N = len(x)
        H = hankel(x[: N - self.fl + 1], x[-self.fl :])
        return H @ self.w
