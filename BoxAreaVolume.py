

def boxAreaVolume (w,h,d):

    area = 2* (h * w) + 2*(h * d) + 2*(w * d);
    volume = w * h * d;

    result = [ area, volume]

    return result


def main():
    boxAreaVolume()

if __name__ == '__main__':
    main()
