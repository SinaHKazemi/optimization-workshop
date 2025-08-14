import matplotlib.pyplot as plt
import numpy as np


def plot_lag_function(f, g, ps, linespace): 
   L = lambda x,p: f(x) - p *g(x)

   fig = plt.figure()
   ax = fig.gca()
   ax.plot(linespace, f(linespace), label='f(x)')

   for p in ps:
      ax.plot(linespace, L(linespace, p), label=f'L(x, {p:.2f})', color ='black', linestyle='--', linewidth=0.5, alpha=0.5)

   ymin, ymax = ax.get_ylim()
   ax.fill_between(linespace, ymin, ymax, where=g(linespace) >= 0, alpha=0.2, interpolate=False, color='red')

   fig.legend()

   return 