# Medical Imaging Diglobalgeniesis Agent

Medical Imaging Diglobalgeniesis Agent is a medical imaging analysis agent that analyzes medical images and provides detailed findings by utilizing models and external tools.

### 1. Create a virtual environment

```shell
./scripts/readygenie_setup.py
source ./globalgenieenv/bin/activate

### 2. Install requirements

```shell
pip install -r readygenie/examples/streamlit_apps/medical_imaging/requirements.txt
```

### 3. Export `GOOGLE_API_KEY`

```shell
export GOOGLE_API_KEY=****
```

### 4. Run Streamlit App

```shell
streamlit run readygenie/examples/streamlit_apps/medical_imaging/app.py
```
