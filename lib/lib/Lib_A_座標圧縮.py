#name#
# 座標圧縮
#description#
# 座標圧縮
#body#
def compress(points, reverse=False, spacing=False):
    """一次元座標圧縮

    Parameters
    ----------
    points : list
         値のリスト [100,300,50,900,200]

    Returns
    -------
    pos : {50: 0, 100: 1, 200: 2, 300: 3, 900: 4}
    vals : {0: 50, 1: 100, 2: 200, 3: 300, 4: 900}
    """
    pos = {}
    vals = {}
    sx = set(points)
    if spacing:
        for p in points:
            sx.add(p+1)

    for i, xi in enumerate(sorted(set(sx), reverse=reverse)):
        pos[xi] = i
        vals[i] = xi
    sx_cmp = [pos[xi] for xi in sx]
    return pos, vals, sx_cmp


def compress2d(points, spacing=False):
    """二次元座標圧縮
    """
    sx = [point[0] for point in points]
    sy = [point[1] for point in points]
    xpos, xvals, sx_cmp = compress(sx, False, spacing)
    ypos, yvals, sy_cmp = compress(sy, False, spacing)
    points_cmp = list(zip(sx_cmp, sy_cmp))

    return xpos, ypos, xvals, yvals, points_cmp

#prefix#
# compress_zaatsu
# lib_座標圧縮
#end#
