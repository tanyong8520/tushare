import traceback


class Loader(object):
    def __init__(self):
        pass

    def load(self, path):
        try:
            tmp = {}
            exec open(path).read() in tmp
            return tmp
        except:
            print("Load module [path %s] error: %s"
                  % (path, traceback.format_exc()))
            return None