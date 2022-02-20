from borg.borg import Borg


class BorgExample(Borg):
    def __init__(self):
        Borg.__init__(self)

    def _set_config(self, val):
        self._value = val

    def _get_config(self):
        return getattr(self, "_value", None)

    config = property(_get_config, _set_config)


def setup_borg():
    c = BorgExample()
    obj = "You're object here"
    c.config = {"obj": obj}
    return c


if __name__ == "__main__":
    # set up Borg's shared state
    ref_1 = setup_borg()
    print("\nobject reference: {}".format(ref_1))
    print("shared state: {}\n".format(ref_1.config["obj"]))

    # get a new instance and retrieve the shared state
    ref_2 = BorgExample()
    print("object reference: {}".format(ref_2))
    print("shared state: {}".format(ref_2.config["obj"]))

