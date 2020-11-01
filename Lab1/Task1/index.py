import matplotlib.pyplot as plt

from Lab1.index import fd1_double, fd1_plus, fd1_minus, fd2, u1, u2


def main1():
	fix_x = 0.8
	for f in [u1, u2]:
		for method in [
			fd1_plus,
			fd1_minus,
			fd1_double,
		]:
			x_h, y_h = [], []
			for h_deg in range(0, 16, 1):
				h = 10 ** (-h_deg)
				x_h.append(h)
				y_h.append(abs(f.d1(fix_x) - method(f.f, fix_x, h)))
			plt.loglog(x_h, y_h)
		plt.legend(['|u\' -  u$_{x}$|', '|u\' -  ${u_\overline{x}}$|', '|u\' -  ${u_\dot{x}}$|'])
		plt.title(f.name)
		plt.show()


def main2():
	fix_x = 0.8
	for f in [u1, u2]:
		x_h, y_h = [], []
		for h_deg in range(0, 16, 1):
			h = 1 * 10 ** (-h_deg)
			x_h.append(h)
			y_h.append(abs(f.d2(fix_x) - fd2(f.f, fix_x, h)))
		plt.loglog(x_h, y_h)
		plt.legend(['|u\'\' -  u$_{x\overline{x}}$|'])
		plt.title(f.name)
		plt.show()


if __name__ == "__main__":
	main1()
	main2()
