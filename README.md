# Automated Diode I–V Characterization

University project developed for a computational methods course, focused on automated laboratory data acquisition and numerical analysis of the current–voltage characteristic of a semiconductor diode.

## Overview

The experiment measures the current flowing through a diode while scanning the applied voltage over several values.

The measured I–V characteristic is compared with the Shockley diode model:

$$
I(V)=I_S\left[\exp\left(\frac{qV}{n k_B T}\right)-1\right].
$$

The experimental data are fitted using

$$
I(V)=a\left[\exp\left(\frac{bV}{T}\right)-1\right],
$$

with the temperature fixed at

$$
T=298.46\ \mathrm{K}.
$$

The fit parameters are used to characterize the diode and, assuming an ideality factor \(n=1\), to estimate the Boltzmann constant through

$$
k_B=\frac{q}{b}.
$$

## Project structure

.
├── acquisition/
│   ├── dmm.py
│   ├── ps.py
│   └── test.py
│
├── analysis/
│   ├── fit_scipy.py
│   └── fit_root.py
│   └── out2.dat
│   └── diode_iv_fit.png
│
├── requirements.txt
├── .gitignore
└── README.md

### Data acquisition

The acquisition scripts communicate with laboratory instrumentation to:

* control a programmable power supply through PyVISA;
* read measurements from a digital multimeter through a serial connection;
* estimate the instrumental uncertainty from the multimeter specifications;
* save voltage, current and current uncertainty for each measurement point.

The resulting dataset has the form

$$
(V_i,\ I_i,\ \sigma_{I_i}).
$$

### Data analysis

The original university implementation used ROOT/TMinuit and $\chi^2$ minimization.

The analysis was later reimplemented using SciPy, making it easier to run without ROOT while preserving the original ROOT version as part of the project history.

The fit minimizes

$$
\chi^2=
\sum_i
\left[
\frac{I_i-I_{\mathrm{model}}(V_i)}
{\sigma_{I_i}}
\right]^2.
$$

The SciPy analysis also produces a plot of the experimental data, uncertainty bars and fitted diode characteristic.

## Requirements

The SciPy analysis uses:

* Python
* NumPy
* SciPy
* Matplotlib

The acquisition scripts additionally require:

* PySerial
* PyVISA

ROOT/PyROOT is only required to reproduce the original analysis implementation.

Install the Python dependencies with:

pip install -r requirements.txt

## Skills demonstrated

* Python scientific programming
* laboratory instrument control
* serial and VISA communication
* automated data acquisition
* experimental uncertainty estimation
* nonlinear curve fitting
* χ² minimization
* scientific visualization
* extraction of physical parameters from experimental data

## Academic context

Originally developed as a university Computational Methods laboratory exercise and later refactored, reorganized and documented as a reproducible scientific computing project.
