# ANN-Implementation

## Important Commands
### Creating Environment
```bash
conda create --prefix ./envs python=3.7 -y
```
### Activating Environment
```bash
conda activate ./envs
```

### Creating Requirements File
```bash
pip freeze>requirements.txt
```

### If you want to install all required libraries
```bash
pip install -r requirements.txt
```

### List Conda environments
```bash
conda list env
```

### Build Wheel
```bash
python setup.py bdist_wheel
```

### Local Package Installation
```bash
pip install -e . ### <<< To install local packages defined in setup.py
```

### Running TensorBoard
```bash
tensorboard --logdir=logs/tensorboard/
```