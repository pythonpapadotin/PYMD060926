# with open("satya.txt", 'w') as fp:
#     fp.write('My Name is Satya')


# fp = open('satya.txt', 'w')
#
# fp.write('My name is Satya')
#
# fp.close()


class satya_open:
    def __init__(self, file_path, mode):
        self.fp = open(file_path, mode)

    def __enter__(self):
        return self.fp

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fp.close()


with satya_open('sadhna.txt', 'w') as fp:
    fp.write('Sadhna is on a vacation!')

