from MuDataFrame import *

mdfo_lead = MuDataFrame("processed_data/lead_bricks_with_gap.csv")
mdf_lead = mdfo_lead.events_df
mdfo_lead.og_df = mdf_lead.copy()

mdfo_calib = MuDataFrame("processed_data/calibration_data.csv")
mdf_calib = mdfo_calib.events_df
mdfo_calib.og_df = mdf_calib.copy()


def getTDCPlot(xval):
    mdfo_calib.reload()
    mdfo_calib.keepEvents("diffL1", xlower, "<=")
    mdfo_calib.keepEvents("diffL2", -59, "<=")

    x1_1 = mdfo_calib.get("L1")

    mdfo_calib.reload()
    mdfo_calib.keepEvents("diffL1", xlower, "<=")

    mdfo_calib.keepEvents("diffL2", -43, "<=")
    mdfo_calib.keepEvents("diffL2", -50, ">=")

    x1_2 = mdfo_calib.get("L1")

    mdfo_calib.reload()
    mdfo_calib.keepEvents("diffL1", xlower, "<=")

    mdfo_calib.keepEvents("diffL2", -34, "<=")
    mdfo_calib.keepEvents("diffL2", -42, ">=")

    x1_3 = mdfo_calib.get("L1")

    mdfo_calib.reload()
    mdfo_calib.keepEvents("diffL1", xlower, "<=")

    mdfo_calib.keepEvents("diffL2", -22, "<=")
    mdfo_calib.keepEvents("diffL2", -28, ">=")

    x1_4 = mdfo_calib.get("L1")

    mdfo_calib.reload()
    mdfo_calib.keepEvents("diffL1", xlower, "<=")

    mdfo_calib.keepEvents("diffL2", -11, "<=")
    mdfo_calib.keepEvents("diffL2", -19, ">=")

    x1_5 = mdfo_calib.get("L1")

    mdfo_calib.reload()
    mdfo_calib.keepEvents("diffL1", xlower, "<=")

    mdfo_calib.keepEvents("diffL2", 5, "<=")
    mdfo_calib.keepEvents("diffL2", -5, ">=")

    x1_6 = mdfo_calib.get("L1")

    mdfo_calib.reload()
    mdfo_calib.keepEvents("diffL1", xlower, "<=")

    mdfo_calib.keepEvents("diffL2", 17, "<=")
    mdfo_calib.keepEvents("diffL2", 10, ">=")

    x1_7 = mdfo_calib.get("L1")

    mdfo_calib.reload()
    mdfo_calib.keepEvents("diffL1", xlower, "<=")

    mdfo_calib.keepEvents("diffL2", 30, "<=")
    mdfo_calib.keepEvents("diffL2", 20, ">=")

    x1_8 = mdfo_calib.get("L1")

    mdfo_calib.reload()
    mdfo_calib.keepEvents("diffL1", xlower, "<=")

    mdfo_calib.keepEvents("diffL2", 38, "<=")
    mdfo_calib.keepEvents("diffL2", 32, ">=")

    x1_9 = mdfo_calib.get("L1")

    mdfo_calib.reload()
    mdfo_calib.keepEvents("diffL1", xlower, "<=")

    mdfo_calib.keepEvents("diffL2", 51, "<=")
    mdfo_calib.keepEvents("diffL2", 45, ">=")

    x1_10 = mdfo_calib.get("L1")

    mdfo_calib.reload()
    mdfo_calib.keepEvents("diffL1", xlower, "<=")

    mdfo_calib.keepEvents("diffL2", 51, ">")

    x1_11 = mdfo_calib.get("L1")

    bins = 50
    range = (60, 110)

    plt.hist(x1_1,
             label="1",
             bins=bins,
             range=range,
             histtype="step",
             color="red")
    plt.hist(x1_2,
             label="2",
             bins=bins,
             range=range,
             histtype="step",
             color="blue")
    plt.hist(x1_3,
             label="3",
             bins=bins,
             range=range,
             histtype="step",
             color="green")
    plt.hist(x1_4,
             label="4",
             bins=bins,
             range=range,
             histtype="step",
             color="lawngreen")
    plt.hist(x1_5,
             label="5",
             bins=bins,
             range=range,
             histtype="step",
             color="sienna")
    plt.hist(x1_6,
             label="6",
             bins=bins,
             range=range,
             histtype="step",
             color="gold")
    plt.hist(x1_7,
             label="7",
             bins=bins,
             range=range,
             histtype="step",
             color="black")
    plt.hist(x1_8,
             label="8",
             bins=bins,
             range=range,
             histtype="step",
             color="maroon")
    plt.hist(x1_9,
             label="9",
             bins=bins,
             range=range,
             histtype="step",
             color="olive")
    plt.hist(x1_10,
             label="10",
             bins=bins,
             range=range,
             histtype="step",
             color="cyan")
    plt.hist(x1_11,
             label="11",
             bins=bins,
             range=range,
             histtype="step",
             color="fuchsia")
    plt.legend()
    plt.xlabel("TDC (Left Channel)")
    plt.title("Tray 1 (x = {})".format(xval))
    plt.savefig("tdc_x={}.png".format(xval))
    plt.show()
