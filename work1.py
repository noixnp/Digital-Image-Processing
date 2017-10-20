
def to_dark(data):
    dark = [v * 0.5 for v in data]

    return dark


def to_gray(data,b ,g, r):

    count2 = 0
    bc = 0
    gc = 0
    rc = 0

    for w in range(len(b)):
        gray = (b[w]+g[w]+r[w])//3
        b[w] = g[w] = r[w] = gray

    for x in range(len(data)):
        if count2 == 0:
            data[x] = b[bc]
            count2+=1
            bc+=1
        elif count2 == 1:
            data[x] = g[gc]
            count2+=1
            gc+=1
        else:
            data[x] = r[rc]
            count2 = 0
            rc+=1

    return data


def to_threshold(data):
    threshold = 127

    for y in range(len(data)):
        if data[y] > threshold:
            data[y] = 255
        else:
            data[y] = 0

    return  data


def np_reversal(data):
     for z in range(len(data)):
         data[z] = 255 - data[z]

     return data


# BMPファイルの書き込み
def save_bmp(filename, data):
        ofile = open(filename, "wb")
        ofile.write(data)
        ofile.close()

def main():
    # bmpファイルを読み込み
    rfile = open("lena.bmp","rb")
    data = rfile.read()
    rfile.close()
    header = data[0:54]
    img = data[54:]
    b = []
    g = []
    r = []
    count = 0

    img = [int(t) for t in img]
    for u in img:
        if count == 0:
            b.append(u)
            count += 1
        elif count == 1:
            g.append(u)
            count +=1
        else:
            r.append(u)
            count = 0



    # 画像を暗くする
    # data2 = to_dark(img)
    # ネガポジ反転
    data3 = np_reversal(img)
    #グレースケール化
    data4 = to_gray(data3, b, g, r)
    # #二値化
    data5 = to_threshold(data4)


    save_data = header + bytes(data5)
    save_bmp("lena2.bmp", save_data)


if __name__ == "__main__":
    main()