import matplotlib.pyplot as plt
import numpy as np

def multiple_formatter(denominator=2, number=np.pi, latex='\pi'):
    def gcd(a, b):
        while b:
            a, b = b, a%b
        return a
    def _multiple_formatter(x, pos):
        den = denominator
        num = int(np.rint(den*x/number))
        com = gcd(num,den)
        (num,den) = (int(num/com),int(den/com))
        if den==1:
            if num==0:
                return r'$0$'
            if num==1:
                return r'$%s$'%latex
            elif num==-1:
                return r'$-%s$'%latex
            else:
                return r'$%s%s$'%(num,latex)
        else:
            if num==1:
                return r'$\frac{%s}{%s}$'%(latex,den)
            elif num==-1:
                return r'$\frac{-%s}{%s}$'%(latex,den)
            else:
                return r'$\frac{%s%s}{%s}$'%(num,latex,den)
    return _multiple_formatter

class Multiple:
    def __init__(self, denominator=2, number=np.pi, latex='\pi'):
        self.denominator = denominator
        self.number = number
        self.latex = latex

    def locator(self):
        return plt.MultipleLocator(self.number / self.denominator)

    def formatter(self):
        return plt.FuncFormatter(multiple_formatter(self.denominator, self.number, self.latex))

def P_2(x):
    return 1.5 * x**2 - 0.5

delta_H = 1/3
delta_v = 1/8
H = 8000.
z1 = 0
z2 = 5e3

theta_0 = -10.

phi = np.linspace(-0.5*np.pi,0.5*np.pi)
sinphi = np.sin(phi)

P2x = P_2(sinphi)

theta_E_1 = theta_0 * (1 - 2/3 * delta_H * P2x + delta_v * (z1/H - 0.5))
theta_E_2 = theta_0 * (1 - 2/3 * delta_H * P2x + delta_v * (z2/H - 0.5))

title = r"$\Theta_E$ at different z"
subtitle = rf"$\Theta_0$ = {theta_0}"
xlabel = r"$\varphi$"
ylabel = r"$\Theta_E$"

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

fig.suptitle(title, y=1.01, fontsize=14) # make title larger than default
ax.set_title(subtitle)

ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)

ax.xaxis.set_major_locator(plt.MultipleLocator(np.pi / 2))
ax.xaxis.set_minor_locator(plt.MultipleLocator(np.pi / 12))
ax.xaxis.set_major_formatter(plt.FuncFormatter(multiple_formatter()))

ax.plot(phi, theta_E_1, label=f"z = {z1}")
ax.plot(phi, theta_E_2, label=f"z = {z2}")
ax.legend()

plt.savefig(f'theta_e.png', dpi=300, bbox_inches='tight')