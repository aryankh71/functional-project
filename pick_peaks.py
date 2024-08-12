def pick_peaks(arr):
    pos = []
    peaks = []
    length = len(arr)

    if length < 3:
        return {"pos": pos, "peaks": peaks}

    for i in range(1, length - 1):
        if arr[i] > arr[i - 1]:
            if arr[i] > arr[i + 1]:
                pos.append(i)
                peaks.append(arr[i])
            elif arr[i] == arr[i + 1]:
                plateau_start = i
                while i + 1 < length and arr[i] == arr[i + 1]:
                    i += 1
                if i + 1 < length and arr[i] > arr[i + 1]:
                    pos.append(plateau_start)
                    peaks.append(arr[plateau_start])

    return {"pos": pos, "peaks": peaks}

price = [0,50,100,150,120,150,123]
print(pick_peaks(price))