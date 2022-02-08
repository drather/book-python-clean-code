class Point:
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long


def locate(latitude: float, longitude: float) -> Point:
    """
    맵에서 좌표에 해당하는 객체를 출력
    :param latitude: 위도
    :param longitude: 경도
    :return: Point
    """

    return Point(lat=latitude, long=longitude)


print(locate.__doc__)
