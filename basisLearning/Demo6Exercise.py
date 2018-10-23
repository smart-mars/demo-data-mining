# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook


# 箱线图
np.random.seed(19680801)

spread = np.random.rand(50) * 100
print 'spread: %s' % spread
center = np.ones(25) * 40
print 'center: %s' % center
flier_high = np.random.rand(10) * 100 + 100
flier_low = np.random.rand(10) * -100
# 合并
data = np.concatenate((spread, center, flier_high, flier_low))
print 'data: %s' % data
print data[0]

plt.subplot(2, 1, 1)
d2 = np.concatenate((spread, center, flier_high, flier_low))
data.shape = (-1, 1)
d2.shape = (-1, 1)
plt.boxplot(d2, medianprops={'color': 'pink'})

plt.subplot(2, 1, 2)
data = [data, d2, d2[::2, 0]]
# fig7, ax7 = plt.subplots()
# ax7.set_title('Multiple Samples with Different sizes')
# ax7.boxplot(data, medianprops={'color': 'red'}, boxprops=dict(color="blue"), whiskerprops={'color': "black"},
#             capprops={'color': "cyan"}, flierprops={'color': 'purple', 'markeredgecolor': "purple"})
plt.boxplot(data, medianprops={'color': 'red'}, boxprops=dict(color="blue"), whiskerprops={'color': "black"},
            capprops={'color': "cyan"}, flierprops={'color': 'purple', 'markeredgecolor': "purple"})
plt.show()

# 散点图
# Load a numpy record array from yahoo csv data with fields date, open, close,
# volume, adj_close from the mpl-data/example directory. The record array
# stores the date as an np.datetime64 with a day unit ('D') in the date column.
with cbook.get_sample_data('goog.npz') as datafile:
    price_data = np.load(datafile)['price_data'].view(np.recarray)
price_data = price_data[-250:]  # get the most recent 250 trading days

delta1 = np.diff(price_data.adj_close) / price_data.adj_close[:-1]

# Marker size in units of points^2
volume = (15 * price_data.volume[:-2] / price_data.volume[0])**2
close = 0.003 * price_data.close[:-2] / 0.003 * price_data.open[:-2]

fig, ax = plt.subplots()
ax.scatter(delta1[:-1], delta1[1:], c=close, s=volume, alpha=0.5)

ax.set_xlabel(r'$\Delta_i$', fontsize=15)
ax.set_ylabel(r'$\Delta_{i+1}$', fontsize=15)
ax.set_title('Volume and percent change')

ax.grid(True)
fig.tight_layout()

plt.show()
