class PlotRegistry:
    registry  = dict()
    @classmethod
    def register(c, cls):
        c.registry[cls.__name__] = cls
        return cls
