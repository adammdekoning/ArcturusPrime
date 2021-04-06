import datetime

def avgTime(a):

    tot_time = 0


    for item in a:
        m = item.minute * 60
        s = item.second
        mi = item.microsecond / 1000000
        tot_time += (m + s + mi)

    avg_sec = round(tot_time/len(a),0)

    average_time = datetime.time(0, int(avg_sec // 60), int(round(avg_sec % 60, 0)), int(avg_sec - (avg_sec // 60) - (avg_sec % 60)))
    return average_time


def avgSplit(t, d):

    m = t.minute*60
    s = t.second
    mi = t.microsecond/1000000

    seconds = round(m + s + mi, 0)/(d/500)

    split = datetime.time(0, int(seconds // 60), int(round(seconds % 60, 0)), int(seconds - (seconds // 60) - (seconds % 60)))

    return split
