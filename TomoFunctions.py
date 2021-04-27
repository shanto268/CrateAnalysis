import copy

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

def getRatioPlot( xviews, yviews, axes=[-30,30], bins=(15,15),title="Data"):
    xx_lead, xx_calib = xviews
    yy_lead, yy_calib = yviews
    ranges = (axes,axes)
    h1, xedges, yedges = np.histogram2d(xx_lead, yy_lead, bins=bins, range=ranges)
    h2, xedges, yedges = np.histogram2d(xx_calib, yy_calib, bins=bins, range=ranges)
    h = h1 / h2
 #   h[h >= 1.15] = 1.15
 #   h[h <= 0.8] = 0.8
    fig, ax = plt.subplots(1)
    pc = ax.pcolorfast(xedges, yedges, h.T)
    plt.title("Reco Z plane XY View Ratio ({})".format(title),fontsize=15)
    plt.xlabel("X (cm)")
    plt.ylabel("Y (cm)")
    plt.colorbar(pc)
    plt.show()


def getNormalizedRatioPlot( xviews, yviews, axes=[-30,30], bins=(15,15),title="Data"):
    xx_lead, xx_calib = xviews
    yy_lead, yy_calib = yviews
    ranges = (axes,axes)
    h1, xedges, yedges = np.histogram2d(xx_lead, yy_lead, bins=bins, range=ranges)
    h2, xedges, yedges = np.histogram2d(xx_calib, yy_calib, bins=bins, range=ranges)
    normH1 = (1/(h1[int(np.floor(h1.shape[0]/2))][int(np.floor(h1.shape[1]/2))]))*h1
    normH2 = (1/(h2[int(np.floor(h2.shape[0]/2))][int(np.floor(h2.shape[1]/2))]))*h2
    h = normH1 / normH2
 #   h[h >= 1.15] = 1.15
 #   h[h <= 0.8] = 0.8
    fig, ax = plt.subplots(1)
    pc = ax.pcolorfast(xedges, yedges, h.T)
    plt.title("Reco Z plane XY View Ratio ({})".format(title),fontsize=15)
    plt.xlabel("X (cm)")
    plt.ylabel("Y (cm)")
    plt.colorbar(pc)
    plt.savefig("tomograms/tomogram_{}.png".format(title.strip()))
    plt.show()

    
def getNormalizedRatioPlotMatrix( xviews, yviews, axes=[-30,30], bins=(15,15),title="Data"):
    xx_lead, xx_calib = xviews
    yy_lead, yy_calib = yviews
    ranges = (axes,axes)
    h1, xedges, yedges = np.histogram2d(xx_lead, yy_lead, bins=bins, range=ranges)
    h2, xedges, yedges = np.histogram2d(xx_calib, yy_calib, bins=bins, range=ranges)
    normH1 = (1/(h1[int(np.floor(h1.shape[0]/2))][int(np.floor(h1.shape[1]/2))]))*h1
    normH2 = (1/(h2[int(np.floor(h2.shape[0]/2))][int(np.floor(h2.shape[1]/2))]))*h2
    h = normH1 / normH2
 #   h[h >= 1.15] = 1.15
 #   h[h <= 0.8] = 0.8
    return h.T
    
def getNormalizedRatioPlot_nonCenter( xviews, yviews, axes=[-30,30], bins=(15,15),title="Data"):
    xx_lead, xx_calib = xviews
    yy_lead, yy_calib = yviews
    ranges = (axes,axes)
    h1, xedges, yedges = np.histogram2d(xx_lead, yy_lead, bins=bins, range=ranges)
    h2, xedges, yedges = np.histogram2d(xx_calib, yy_calib, bins=bins, range=ranges)
    normH1 = (1/(h1[int(np.floor(h1.shape[0]/2))][int(np.floor(h1.shape[1]/2))]))*h1
    normH2 = (1/(h2[int(np.floor(h2.shape[0]/2))][int(np.floor(h2.shape[1]/2))]))*h2
    h = normH1 / normH2
 #   h[h >= 1.15] = 1.15
 #   h[h <= 0.8] = 0.8
    fig, ax = plt.subplots(1)
    pc = ax.pcolorfast(xedges, yedges, h.T)
    plt.title("Reco Z plane XY View Ratio ({})".format(title),fontsize=15)
    plt.xlabel("X (cm)")
    plt.ylabel("Y (cm)")
    plt.colorbar(pc)
    plt.savefig("tomograms/tomogram_{}.png".format(title.strip()))
    plt.show()
    
    
def getNormalizedRatioPlot( xviews, yviews, axes=[-30,30], bins=(15,15),title="Data"):
    xx_lead, xx_calib = xviews
    yy_lead, yy_calib = yviews
    ranges = (axes,axes)
    h1, xedges, yedges = np.histogram2d(xx_lead, yy_lead, bins=bins, range=ranges)
    h2, xedges, yedges = np.histogram2d(xx_calib, yy_calib, bins=bins, range=ranges)
    normH1 = (1/(h1[int(np.floor(h1.shape[0]/2))][int(np.floor(h1.shape[1]/2))]))*h1
    normH2 = (1/(h2[int(np.floor(h2.shape[0]/2))][int(np.floor(h2.shape[1]/2))]))*h2
    h = normH1 / normH2
 #   h[h >= 1.15] = 1.15
 #   h[h <= 0.8] = 0.8
    fig, ax = plt.subplots(1)
    pc = ax.pcolorfast(xedges, yedges, h.T)
    plt.title("Reco Z plane XY View Ratio ({})".format(title),fontsize=15)
    plt.xlabel("X (cm)")
    plt.ylabel("Y (cm)")
    plt.colorbar(pc)
    plt.savefig("tomograms/tomogram_{}.png".format(title.strip()))
    plt.show()
    
    
def getTomogramMatrix(xview, yview, axes=[-30,30], bins=(15,15),title="Data"):
    ranges = (axes,axes)
    h1, xedges, yedges = np.histogram2d(xview, yview, bins=bins, range=ranges)
    normH = (1/(h1[int(np.floor(h1.shape[0]/2))][int(np.floor(h1.shape[1]/2))]))*h1
   # return normH, , xedges, yedges
    fig, ax = plt.subplots(1)
    pc = ax.pcolorfast(xedges, yedges, normH.T)
    plt.title("Reco Z plane XY View ({})".format(title),fontsize=15)
    plt.xlabel("X (cm)")
    plt.ylabel("Y (cm)")
    plt.colorbar(pc)
    plt.show()
