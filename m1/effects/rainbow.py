import time
from m1.effects.effect import Effect
from m1.effects.utils import wheel


class Rainbow(Effect):
    """
    Draw rainbow that fades across all pixels at once.
    Extracted from https://github.com/rpi-ws281x/rpi-ws281x-python/blob/master/examples/strandtest.py
    """

    def __init__(self, wait_ms=20, iterations=1):
        super(Rainbow, self).__init__()
        self.wait_ms = wait_ms
        self.iterations = iterations

    def run(self):
        for j in self.range(256 * self.iterations):
            for i in self.range(self.strip.numPixels()):
                self.strip.setPixelColor(i, wheel((i + j) & 255))
            self.strip.show()
            time.sleep(self.wait_ms / 1000.0)

