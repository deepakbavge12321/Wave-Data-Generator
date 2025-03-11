# GPU Setup Guide for Deep Learning (Windows)

This guide provides step-by-step instructions to set up a **GPU-powered Deep Learning environment** on Windows. Follow the steps carefully to ensure proper installation.

---

## 1. Install Visual Studio Code
Download and install **Visual Studio Code** from:
- [VS Code Official Site](https://code.visualstudio.com/)

---

## 2. Install Anaconda
Download and install **Anaconda** from:
- [Anaconda Official Site](https://www.anaconda.com/)

During installation, select **Add Anaconda to PATH** (optional but recommended).

---

## 3. Install Visual Studio with C++ Build Tools
TensorFlow requires **Visual Studio** for GPU support. Download and install:
- [Visual Studio 2019/2022](https://visualstudio.microsoft.com/)
- During installation, select:
  - **Desktop development with C++**
  - **Windows 10 SDK**
  - **C++ CMake tools** (optional but recommended)

---

## 4. Install NVIDIA CUDA Toolkit
Download and install **CUDA Toolkit 11.2**:
- [CUDA Toolkit 11.2](https://developer.nvidia.com/cuda-11.2.2-download-archive)

During installation, select **Express Install**.

After installation, verify CUDA:
```sh
nvcc --version
```

---

## 5. Install cuDNN
Download **cuDNN 8.1.0**:
- [cuDNN Archive](https://developer.nvidia.com/rdp/cudnn-archive)

After downloading, **extract the files** and copy them into the corresponding CUDA folders:
- Copy `bin\*` to `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.2\bin`
- Copy `include\*` to `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.2\include`
- Copy `lib\x64\*` to `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.2\lib\x64`

---

## 6. Create a Deep Learning Environment in Anaconda
Open **Anaconda Prompt** and run:
```sh
conda create --name tf2.10-gpu python=3.10 -y
conda activate tf2.10-gpu
```

---

## 7. Install CUDA and cuDNN via Conda
```sh
conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0 -y
```

---

## 8. Install TensorFlow with GPU Support
Ensure NumPy is compatible:
```sh
pip install "numpy<2"
```
Then, install TensorFlow 2.10:
```sh
pip install tensorflow==2.10
```

---

## 9. Verify GPU Setup in VS Code
Open VS Code and run the following in a Python script:
```python
import tensorflow as tf
print(tf.config.list_physical_devices('GPU'))
```
If your GPU is detected, you should see an output similar to:
```
[PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU')]
```

---

## 🎯 Troubleshooting
### Check if CUDA is Installed Properly
```sh
nvcc --version
```

### Check if cuDNN is Installed Properly
Navigate to the CUDA `bin` folder and run:
```sh
where cudnn64_8.dll
```

### Check TensorFlow GPU Support
```python
import tensorflow as tf
print(tf.test.is_built_with_cuda())  # Should return True
print(tf.config.list_physical_devices('GPU'))  # Should list GPUs
```

If GPU is not detected:
1. Ensure **NVIDIA drivers** are updated: [NVIDIA Drivers](https://www.nvidia.com/download/index.aspx)
2. Ensure **CUDA & cuDNN versions match TensorFlow requirements**
3. Restart your system and retry the verification

---

## ✅ Done!
You now have a fully functional **GPU-accelerated deep learning setup** on Windows! 🚀

