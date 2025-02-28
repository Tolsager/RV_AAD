import numpy as np

from rvaad.FIR_filter import FIR


def test_fir_fit_transform():
    # Test data
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=float)
    y = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20], dtype=float)  # Linear relationship

    filter_length = 3
    fir = FIR(filter_length)

    # Fit the model
    fir.fit(x, y)
    assert fir.w is not None, "Weights should not be None after fitting."

    # Transform input
    y_pred = fir.transform(x)

    # Check output shape
    expected_length = len(x) - filter_length + 1
    assert y_pred.shape[0] == expected_length, "Output shape mismatch."

    # Check if the model correctly estimates a linear transformation
    assert np.allclose(y_pred, y[-expected_length:], atol=1e-5), "Model output does not match expected values."
