from Lab1.index import u
import matplotlib.pyplot as plt
import numpy as np
import math


def tma(a, b, c, f):
	alpha = [-b[0] / c[0]]
	beta = [f[0] / c[0]]
	n = len(f)
	x = np.zeros(n)

	for i in range(1, n-1):
		alpha.append(-b[i-1] / (a[i-1] * alpha[i - 1] + c[i-1]))
		beta.append((f[i-1] - a[i-1] * beta[i-1]) / (a[i-1] * alpha[i - 1] + c[i-1]))

	x[n - 1] = (f[n - 1] - a[n-2] * beta[n-2]) / (c[n - 1] + a[n-2] * alpha[n-2])

	for i in range(n - 1, 0, -1):
		x[i - 1] = alpha[i-1] * x[i] + beta[i-1]

	return x


def main():
	A, B = 0, 1
	h_v = []
	err = []
	for deg in range(1, 7):
		h = 10**-deg
		x_v = np.arange(start=A, stop=B + h, step=h)
		n = len(x_v)
		c = -np.ones(n-2) * 2
		b = np.ones(n-3)
		a = np.ones(n-3)
		f = [u.d2(x) * h * h for x in x_v][1:n-1]
		f[0] -= u.f(A)
		f[n-3] -= u.f(B)
		Y = [u.f(A), *tma(c=c, a=a, b=b, f=f), u.f(B)]
		h_v.append(h)
		err.append(math.sqrt(sum(map(lambda el: (el[0] - el[1])*(el[0] - el[1]), zip(Y, [u.f(x) for x in x_v])))))

	print(*h_v)
	print(*err)
	plt.loglog(h_v, err)
	plt.title('Зависимость ошибки от шага h')
	plt.show()


if __name__ == '__main__':
	main()
