# Virtual Environment Setup 

## Create New Environment
```bash
conda create -n <new_env_name> python=<python_version> -y
```
```bash
conda activate <new_env_name>
```
---

## Check Existing Environment
```bash
conda env list
```
---

## Remove Environment
```bash
conda remove --name <env_name> --all
```
---

## Create New Environment into Project Folder
```bash
conda create --prefix .\<new_env_name> python=3.9 -y
```
```bash
conda activate .\<new_env_name>
```
---

## Install packages with requirements.txt
```python
pip install-r requirements.txt
```
---
