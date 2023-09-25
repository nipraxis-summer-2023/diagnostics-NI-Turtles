import numpy as np

def dvars(img):
    """ Calculate dvars metric on Nibabel image `img`

    The dvars calculation between two volumes is defined as the square root of
    (the mean of the (voxel differences squared)).

    Parameters
    ----------
    img : nibabel image

    Returns
    -------
    dvals : 1D array
        One-dimensional array with n-1 elements, where n is the number of
        volumes in `img`.
    """
    # Check if the image object has the necessary data attribute.
    if not hasattr(img, 'get_fdata'):
        raise ValueError("Invalid image: The provided image does not have the necessary data.")

    # Get the data from the image.
    data = img.get_fdata()

    # Calculate differences between consecutive volumes along the time axis.
    vol_diff = np.diff(data, axis=-1)

    # Calculate spatial RMS (DVARS) for each volume.
    dvars = np.sqrt(np.mean(vol_diff ** 2, axis=(0, 1, 2)))

    return dvars
