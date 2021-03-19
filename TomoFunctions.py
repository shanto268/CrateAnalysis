import scipy.interpolate, scipy.optimize
import plotly.express as px
import copy
import numpy as np
import matplotlib.pyplot as plt

def getSameShapeDataSets(mdfo1, mdfo2):
    mdfo1 =  copy.copy(mdfo1)
    mdfo2 = copy.copy(mdfo2)
    s1 = len(mdfo1.events_df.index)
    s2 = len(mdfo2.events_df.index)
    s = min(s1,s2)
    mdfo1.events_df =  mdfo1.events_df.iloc[:s]
    mdfo2.events_df =  mdfo2.events_df.iloc[:s]
    return mdfo1, mdfo2

def getSameSizeData(mdfo1, mdfo2, data_term):
    mdfo1, mdfo2 = getSameShapeDataSets(mdfo1, mdfo2)
    return mdfo1.get(data_term), mdfo2.get(data_term)

def getRatioPlot( xviews, yviews, axes=[-30,30], bins=(15,15)):
    xx_lead, xx_calib = xviews
    yy_lead, yy_calib = yviews
    ranges = (axes,axes)
    h1, xedges, yedges = np.histogram2d(xx_lead, yy_lead, bins=bins, range=ranges)
    h2, xedges, yedges = np.histogram2d(xx_calib, yy_calib, bins=bins, range=ranges)
    h = h1 / h2
    h[h >= 1.15] = 1.15
    h[h <= 0.7] = 0.7
    fig, ax = plt.subplots(1)
    pc = ax.pcolorfast(xedges, yedges, h.T)
    plt.title("Reco Z plane XY View Ratio (Data)",fontsize=15)
    plt.xlabel("X (cm)")
    plt.ylabel("Y (cm)")
    plt.colorbar(pc)
    plt.show()



def getLeadDistanceinXArr(xx_lead, xx_calib, bins):
    b1 = plt.hist(xx_lead, bins=bins, density=True, range=(-50, 50))
    b2 = plt.hist(xx_calib, bins=bins, density=True, range=(-50, 50))
    x = np.array([i * 5 for i in range(1, 12)])
    y1 = [1 for i in range(len(x))]
    y2 = b1[0] / b2[0]
    interp1 = scipy.interpolate.InterpolatedUnivariateSpline(x, y1)
    interp2 = scipy.interpolate.InterpolatedUnivariateSpline(x, y2)
    new_x = np.linspace(x.min(), x.max(), 100)
    new_y1 = interp1(new_x)
    new_y2 = interp2(new_x)
    idx = np.argwhere(np.diff(np.sign(new_y1 - new_y2)) != 0)
    plt.plot(x, y1, marker='o', mec='none', ms=4, lw=1, label='y1')
    plt.plot(x, y2, marker='o', mec='noe', ms=4, lw=1, label='y2')
    plt.plot(new_x[idx], new_y1[idx], 'ro', ms=7, label='intersection')
    plt.legend(frameon=False, fontsize=10, numpoints=1, loc='lower left')
    plt.ylim(0.7, 1.05)
    plt.xlim(0, 60)
    plt.show()
    return list(new_x[idx])


def testTomogram(mdfo_lead, mdfo_calib, bins):
    xx_lead = mdfo_lead.get("xx")
    yy_lead = mdfo_lead.get("yy")
    xx_calib = mdfo_calib.get("xx")
    yy_calib = mdfo_calib.get("yy")
    b1 = plt.hist(xx_lead,
                  bins=bins,
                  alpha=1,
                  label="Brick",
                  density=True,
                  range=(-50, 50),
                  histtype='step')
    b2 = plt.hist(xx_calib,
                  bins=bins,
                  alpha=1,
                  label="Calib",
                  density=True,
                  range=(-50, 50),
                  histtype='step')
    plt.title("XView at ZPlane of Lead Brick (cm)")
    plt.legend()
    plt.show()
    b3 = plt.hist(yy_lead,
                  bins=bins,
                  alpha=1,
                  label="Brick",
                  density=True,
                  range=(-50, 50),
                  histtype='step')
    b4 = plt.hist(yy_calib,
                  bins=bins,
                  alpha=1,
                  label="Calib",
                  density=True,
                  range=(-50, 50),
                  histtype='step')
    plt.title("YView at ZPlane of Lead Brick (cm)")
    plt.legend()
    plt.show()
    plt.plot([i * 5 for i in range(1, 12)], (b1[0] / b2[0]), '--x', label="X")
    plt.plot([i * 5 for i in range(1, 12)], (b3[0] / b4[0]), '--x', label="Y")
    plt.axhline(y=1, color='r')
    plt.title("Ratio Plot")
    plt.xlabel("length (cm)")
    plt.grid()
    plt.legend()
    plt.ylim(0.85, 1.1)
    plt.xlim(5, 60)
    plt.show()
    #x_dist = getLeadDistanceinXArr(xx_lead,xx_calib,bins=11)
    #y_dist = getLeadDistanceinXArr(yy_lead,yy_calib,bins=11)
    #return x_dist,y_dist


def testTomogramRaw(mdfo_lead, mdfo_calib, bins):
    xx_lead = mdfo_lead.get("xx")
    yy_lead = mdfo_lead.get("yy")
    xx_calib = mdfo_calib.get("xx")
    yy_calib = mdfo_calib.get("yy")
    b1 = plt.hist(xx_lead,
                  bins=bins,
                  alpha=1,
                  label="Brick",
                  range=(-50, 50),
                  histtype='step')
    b2 = plt.hist(xx_calib,
                  bins=bins,
                  alpha=1,
                  label="Calib",
                  range=(-50, 50),
                  histtype='step')
    plt.title("XView at ZPlane of Lead Brick (cm)")
    plt.legend()
    plt.show()
    b3 = plt.hist(yy_lead,
                  bins=bins,
                  alpha=1,
                  label="Brick",
                  range=(-50, 50),
                  histtype='step')
    b4 = plt.hist(yy_calib,
                  bins=bins,
                  alpha=1,
                  label="Calib",
                  range=(-50, 50),
                  histtype='step')
    plt.title("YView at ZPlane of Lead Brick (cm)")
    plt.legend()
    plt.show()
    plt.plot([i * 5 for i in range(1, 12)], (b1[0] / b2[0]), '--x', label="X")
    plt.plot([i * 5 for i in range(1, 12)], (b3[0] / b4[0]), '--x', label="Y")
    plt.axhline(y=1, color='r')
    plt.title("Ratio Plot")
    plt.xlabel("length (cm)")
    plt.grid()
    plt.legend()
    plt.ylim(0.85, 1.1)
    plt.xlim(5, 60)
    plt.show()
    #x_dist = getLeadDistanceinXArr(xx_lead,xx_calib,bins=11)
    #y_dist = getLeadDistanceinXArr(yy_lead,yy_calib,bins=11)
    #return x_dist,y_dist


def getSameShapeDataSets(mdfo1, mdfo2):
    mdfo1 = copy.copy(mdfo1)
    mdfo2 = copy.copy(mdfo2)
    s1 = len(mdfo1.events_df.index)
    s2 = len(mdfo2.events_df.index)
    s = min(s1, s2)
    mdfo1.events_df = mdfo1.events_df.iloc[:s]
    mdfo2.events_df = mdfo2.events_df.iloc[:s]
    return mdfo1, mdfo2


def getSameSizeData(mdfo1, mdfo2, data_term):
    mdfo1, mdfo2 = getSameShapeDataSets(mdfo1, mdfo2)
    return mdfo1.get(data_term), mdfo2.get(data_term)


def getRatioPlot(xviews, yviews, axes=[-40, 40], bins=(15, 15)):
    xx_lead, xx_calib = xviews
    yy_lead, yy_calib = yviews
    ranges = (axes, axes)
    h1, xedges, yedges = np.histogram2d(xx_lead,
                                        yy_lead,
                                        bins=bins,
                                        range=ranges)
    h2, xedges, yedges = np.histogram2d(xx_calib,
                                        yy_calib,
                                        bins=bins,
                                        range=ranges)
    h = h1 / h2
    fig, ax = plt.subplots(1)
    pc = ax.pcolorfast(xedges, yedges, h.T)
    plt.title("Reco Z plane XY View Ratio (Data)", fontsize=15)
    plt.xlabel("X (cm)")
    plt.ylabel("Y (cm)")
    plt.colorbar(pc)
    plt.show()


def doTomography(bins, mdf, title):
    fig = px.density_heatmap(mdf,
                             x="xx",
                             y="yy",
                             title=title,
                             nbinsx=bins,
                             nbinsy=bins,
                             marginal_x="histogram",
                             marginal_y="histogram")
    fig.update_layout(
        xaxis_title="XView (cm)",
        yaxis_title="YView (cm)",
    )
    fig.show()
