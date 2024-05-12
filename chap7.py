import matplotlib.pyplot as plt
import numpy as np


np_array = np.array(float)


def Cal_beta(np_ratio:np.array, WbLp_ratio:np.array) -> np_array:
    beta:np_array
    if np_ratio.size == 1 and WbLp_ratio.size > 1:
        beta = 1 / (np.cosh(WbLp_ratio) + np.sinh(WbLp_ratio) - 1)
    elif np_ratio.size > 1 and WbLp_ratio.size == 1:
        beta = 0.648 / (1 + np_ratio*0.7616 - 0.648)
    return beta


def plot_betavsWbLp(ax1:plt.Axes) -> None:

    WbLp_ratio = np.linspace(0.01, 1, 100)
    np_ratio = np.array([1])
    res_beta = Cal_beta(np_ratio, WbLp_ratio)

    ax1.set_title(r'$\beta$ vs $W_b/L_p^n$')
    ax1.plot(WbLp_ratio, res_beta, linestyle='-', color='b')
    ax1.set_xlabel(r'$W_b/L_p^n$')
    ax1.set_ylabel(r'$\beta$')
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 100)


def plot_betavsnp(ax2:plt.Axes) -> None:
    np_ratio = np.linspace(0.01, 1, 100)
    WbLp_ratio = np.array([1])
    res_beta = Cal_beta(np_ratio, WbLp_ratio)

    ax2.set_title(r'$\beta$ vs $n_n/p_p$')
    ax2.plot(np_ratio, res_beta, linestyle='-', color='b')
    ax2.set_xlabel(r'$n_n/p_p$')
    ax2.set_ylabel(r'$\beta$')
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0.5, 2)


if __name__ == '__main__':
    np_array = np.array(float)
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2)
    plot_betavsWbLp(ax1)
    plot_betavsnp(ax2)
    plt.savefig('./chap7.png')
    plt.show()