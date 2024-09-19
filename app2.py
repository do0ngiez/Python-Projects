import app

def print_app2():
    name = (__name__)
    return name

if __name__ == "__main__":
    print("working in {}".format(print_app2()))
    print("working in {}".format(app.print_app()))
