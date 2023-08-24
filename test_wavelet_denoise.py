
import unittest
import numpy as np
from wavelet_denoise_py import wavelet_denoise

class TestWaveletDenoise(unittest.TestCase):
    def setUp(self):
        t = np.linspace(0, 1, 1000, endpoint=False)
        self.original_signal = np.cos(2 * np.pi * 7 * t) + 0.25 * np.sin(2 * np.pi * 13 * t)
        self.noisy_signal = self.original_signal + 0.5 * np.random.randn(t.size)
        self.sample_rate = 1000
        self.t = t

    def test_thresholding(self):
        denoised_signal_low_thresh = wavelet_denoise(self.noisy_signal, threshold_factor=0.01, method='original')
        denoised_signal_high_thresh = wavelet_denoise(self.noisy_signal, threshold_factor=0.5, method='original')
        
        mse_low = np.mean((self.original_signal - denoised_signal_low_thresh)**2)
        mse_high = np.mean((self.original_signal - denoised_signal_high_thresh)**2)

        self.assertTrue(isinstance(mse_low, float) and isinstance(mse_high, float))

    def test_soft_vs_hard_thresholding(self):
        denoised_signal_hard = wavelet_denoise(self.noisy_signal, srate=self.sample_rate, soft_thresh=False, method='adjusted')
        denoised_signal_soft = wavelet_denoise(self.noisy_signal, srate=self.sample_rate, soft_thresh=True, method='adjusted')
        
        diff = np.sum(np.abs(denoised_signal_hard - denoised_signal_soft))
        
        self.assertTrue(diff > 0)

    def test_multi_channel(self):
        multi_channel_data = np.vstack([self.noisy_signal, self.noisy_signal, self.noisy_signal])
        denoised_data = wavelet_denoise(multi_channel_data, method='original')
        self.assertEqual(denoised_data.shape, multi_channel_data.shape)

if __name__ == '__main__':
    unittest.main()
