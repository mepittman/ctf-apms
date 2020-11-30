# ctf-apms

### Clone the repository
git clone https://github.com/mepittman/ctf-apms/

### If using conda as a package manager (recommended):
cd ctf-apms/; 
conda create --name ctf_env --file requirements.txt; 
source activate ctf_env

### Download data and create necesssary folders
python setup.py

### Interact with code
cd jupyter_notebooks/; 
jupyter notebook

### Notebooks that should be run before any others:
1) define_interactome.ipynb
2) variant_comparison.ipynb
