
import numpy as np
import pywt
import mne

def wavelet_denoise(data, srate=None, wavelet_type='sym4', threshold_factor=0.04, soft_thresh=False, method='original'):
    if method == 'original':
        return wavelet_denoise_original(data, wavelet_type=wavelet_type, threshold_factor=threshold_factor)
    elif method == 'adjusted':
        return wavelet_denoise_adjusted(data, srate=srate, soft_thresh=soft_thresh, wavelet_type=wavelet_type, threshold_factor=threshold_factor)

def wavelet_denoise_original(data, wavelet_type='sym4', threshold_factor=0.04):
    # Determine if data is multi-channel
    is_multi_channel = len(data.shape) > 1
    channels = data.shape[0] if is_multi_channel else 1
    denoised_data = []
    
    for ch in range(channels):
        channel_data = data[ch] if is_multi_channel else data
        
        # Decompose into wavelet components
        coeffs = pywt.wavedec(channel_data, wavelet_type)
        
        # Apply thresholding
        for i in range(1, len(coeffs)):
            coeffs[i] = pywt.threshold(coeffs[i], threshold_factor*max(coeffs[i]))
        
        # Reconstruct data
        datarec = pywt.waverec(coeffs, wavelet_type)
        
        denoised_data.append(datarec)
    
    return np.array(denoised_data) if is_multi_channel else denoised_data[0]

def wavelet_denoise_adjusted(data, srate, paradigm_erp=True, soft_thresh=False, wavelet_type=None, threshold_factor=0.04):
    # Determine if data is multi-channel
    is_multi_channel = len(data.shape) > 1
    channels = data.shape[0] if is_multi_channel else 1
    denoised_data = []
    
    for ch in range(channels):
        channel_data = data[ch] if is_multi_channel else data
        
        # Logic for wavelet and decomposition level
        if not wavelet_type:
            if paradigm_erp:
                wavelet_type = 'coif4'
                if srate > 500: 
                    wavLvl = 11
                elif srate > 250 and srate <= 500: 
                    wavLvl = 10
                else: 
                    wavLvl = 9
            else:
                wavelet_type = 'bior4.4'
                if srate > 500: 
                    wavLvl = 10
                elif srate > 250 and srate <= 500: 
                    wavLvl = 9
                else: 
                    wavLvl = 8
        else:
            w = pywt.Wavelet(wavelet_type)
            wavLvl = pywt.dwt_max_level(len(channel_data), w.dec_len)
        
        # Decompose data
        coeffs = pywt.wavedec(channel_data, wavelet_type, level=wavLvl)
        
        # Thresholding rule (Soft or Hard)
        mode = 'soft' if soft_thresh else 'hard'
        
        # Apply thresholding
        for i in range(1, len(coeffs)):
            coeffs[i] = pywt.threshold(coeffs[i], threshold_factor*max(coeffs[i]), mode=mode)
        
        # Reconstruct data
        datarec = pywt.waverec(coeffs, wavelet_type)
        
        denoised_data.append(datarec)
    
    return np.array(denoised_data) if is_multi_channel else denoised_data[0]
