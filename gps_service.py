class GPSSignalLostError(Exception):
    """Ngoai le khi mat tin hieu GPS."""
    pass


def get_current_location():
    """Mo phong phan cung GPS."""
    return (10.0, 105.0)
