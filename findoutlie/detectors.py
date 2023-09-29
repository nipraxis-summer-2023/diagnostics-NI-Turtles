""" Utilities for detecting outliers

These functions take a vector of values, and return a boolean vector of the
same length as the input, where True indicates the corresponding value is an
outlier.

The outlier detection routines will likely be adapted to the specific measure
that is being worked on.  So, some detector functions will work on values > 0,
other on normally distributed values etc.  The routines should check that their
requirements are met and raise an error otherwise.
"""

# Any imports you need
import numpy as np

def iqr_detector(measures, iqr_proportion=1.5):
    """ Detect outliers in `measures` using interquartile range.

    Returns a boolean vector of same length as `measures`, where True means the
    corresponding value in `measures` is an outlier.

    Call Q1, Q2 and Q3 the 25th, 50th and 75th percentiles of `measures`.

    The interquartile range (IQR) is Q3 - Q1.

    An outlier is any value in `measures` that is either:

    * > Q3 + IQR * `iqr_proportion` or
    * < Q1 - IQR * `iqr_proportion`.

    See: https://en.wikipedia.org/wiki/Interquartile_range

    Parameters
    ----------
    measures : 1D array
        Values for which we will detect outliers
    iqr_proportion : float, optional
        Scalar to multiply the IQR to form upper and lower threshold (see
        above).  Default is 1.5.

    Returns
    -------
    outlier_tf : 1D boolean array
        A boolean vector of same length as `measures`, where True means the
        corresponding value in `measures` is an outlier.
    """

    percentiles = [25, 75]
    result = np.percentile(measures, q=percentiles)
    Q1, Q3 = result
    IQR = Q3 - Q1
    upper_bound = Q3 + IQR * iqr_proportion # upper outlier
    lower_bound = Q1 - IQR * iqr_proportion # lower outlier

    return np.logical_or(measures > upper_bound, measures < lower_bound)


def vol_mean(data):
    """
    Calculates the mean of each volume in the 4D data

    Parameters: a nibabel image
    data: a nibable image (nibabel.nifti1.Nifti1Image), a 4D fMRI data with volumes over time
    --------
    Returns: list
    a list of means, each item being mean per volume across time
    """
    return [
        np.mean(data[..., vol])
        for vol in range(data.shape[-1])
    ]


def z_score_detector(data, n_std=2):
    """
    Detects outliers in the 4D data and returns a list of indices of outlier volumes

    Parameters: nibable image, int
    data: a nibable image (nibabel.nifti1.Nifti1Image), a 4D fMRI data with volumes over time
    n_std: number of standard deviations away from mean for a volue to be classified as an outlier; default 2
    -------
    Returns: numpy array
    A list of indices of outlier volumes in the data (classifed as > n_std from the mean)
    """
    if data.size == 0:
        return np.array([])

    means = vol_mean(data)
    mean_means = np.mean(means)
    std_means = np.std(means)
    if std_means == 0: # avoid division by zero
        return np.array([])

    # Calculate Z-scores
    z_scores = (means - mean_means) / std_means

    # Find outliers using Z-scores
    outliers = np.asarray(np.abs(z_scores) > n_std).nonzero()[0]

    return outliers