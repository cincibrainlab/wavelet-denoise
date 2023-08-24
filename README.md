# Wavelet Denoising Module for EEG Data (Python Implementation)

## Description
This Python module provides functions to perform wavelet-based denoising on EEG data, with specialized support for MNE objects. The denoising techniques are particularly suited for biomedical signals like EEG, ECG, and others. This module offers both a standard wavelet denoising function and an adjusted function that aligns more closely with a MATLAB-based function from the [HAPPE repository](https://github.com/PINE-Lab/HAPPE/).

## Features
- Supports both single-channel and multi-channel EEG data.
- Designed to work seamlessly with MNE raw or epoched data objects.
- Offers two denoising methods: `original` and `adjusted`.
- Thresholding options available for denoising.
- Incorporates both `Soft` and `Hard` thresholding based on requirements.

## Installation
1. Clone the repository:  
   ```
   git clone <repository_url>
   ```
2. Navigate to the directory and you'll find the `wavelet_denoise_py.py` module ready to be imported into your Python scripts.

## Usage
```python
from wavelet_denoise_py import wavelet_denoise

# Sample data (replace with your EEG data or MNE object)
data = ...

# Denoise using the original method
denoised_data_original = wavelet_denoise(data, method='original')

# Denoise using the adjusted method (closer to MATLAB function in HAPPE)
denoised_data_adjusted = wavelet_denoise(data, srate=1000, method='adjusted')
```

## Adaptation
This module is adapted and inspired from the MATLAB-based wavelet denoising approach used in the [HAPPE repository](https://github.com/PINE-Lab/HAPPE/). We've translated and optimized it for Python while maintaining the integrity of the original denoising process.

## Unit Tests
Unit tests are provided in the `test_wavelet_denoise.py` script. To run the tests, execute:

```
python test_wavelet_denoise.py
```

## Dependencies
- numpy
- pywt
- mne

## Contributing
If you'd like to contribute, please fork the repository, make your changes, and open a Pull Request.

## License
This project is licensed under the MIT License.

---

The README now more clearly reflects the module's capability to handle MNE objects. If you'd like any further adjustments, please let me know.
