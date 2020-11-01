import math


class u1:
	name = 'x$^{2}$'

	@staticmethod
	def f(x):
		return x*x

	@staticmethod
	def d1(x):
		return 2*x

	@staticmethod
	def d2(x):
		return 2


class u2:
	name = 'sin(x)'

	@staticmethod
	def f(x):
		return math.sin(x)

	@staticmethod
	def d1(x):
		return math.cos(x)

	@staticmethod
	def d2(x):
		return -math.sin(x)


def fd1_plus(f, x, h):
	return (f(x+h) - f(x))/h


def fd1_minus(f, x, h):
	return (f(x) - f(x-h))/h


def fd1_double(f, x, h):
	return (f(x+h) - f(x-h))/2/h


def fd2(f, x, h):
	return (f(x+h)-2*f(x)+f(x-h))/h/h

