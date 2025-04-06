# General imports# General imports# General imports
import numpy as np
import warnings
warnings.filterwarnings("ignore")

# Pre-defined ansatz circuit, operator class and visualization tools
from qiskit.circuit.library import QAOAAnsatz
from qiskit.quantum_info import SparsePauliOp, Pauli
from qiskit.visualization import plot_distribution

# Estimator & Sampler for optimization in a full simulated environement
from qiskit.primitives import StatevectorEstimator
from qiskit.primitives import StatevectorSampler

# SciPy minimizer routine
from scipy.optimize import minimize

# rustworkx graph library
import rustworkx as rx
from rustworkx.visualization import mpl_draw
import numpy as np
import warnings
warnings.filterwarnings("ignore")

# Pre-defined ansatz circuit, operator class and visualization tools
from qiskit.circuit.library import QAOAAnsatz
from qiskit.quantum_info import SparsePauliOp, Pauli
from qiskit.visualization import plot_distribution

# Estimator & Sampler for optimization in a full simulated environement
from qiskit.primitives import StatevectorEstimator
from qiskit.primitives import StatevectorSampler

# SciPy minimizer routine
from scipy.optimize import minimize

# rustworkx graph library
import rustworkx as rx
from rustworkx.visualization import mpl_draw
import numpy as np
import warnings
warnings.filterwarnings("ignore")

# Pre-defined ansatz circuit, operator class and visualization tools
from qiskit.circuit.library import QAOAAnsatz
from qiskit.quantum_info import SparsePauliOp, Pauli
from qiskit.visualization import plot_distribution

# Estimator & Sampler for optimization in a full simulated environement
from qiskit.primitives import StatevectorEstimator
from qiskit.primitives import StatevectorSampler

# SciPy minimizer routine
from scipy.optimize import minimize

# rustworkx graph library
import rustworkx as rx
from rustworkx.visualization import mpl_draw