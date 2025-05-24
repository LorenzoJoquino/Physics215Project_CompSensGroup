def rmse(PSD1, PSD2):
    error = np.sqrt(np.mean((PSD1 - PSD2) ** 2))
    return error

