print("=" * 50)

def funcionExterna(n1):
    def funcionInterna(n2):
        print("", n2 * n1)

    return funcionInterna

funcionExterna(5)(3)