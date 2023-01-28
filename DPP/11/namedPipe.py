import multiprocessing


class ChildProcess(multiprocessing.Process):
    def __init__(self, conn):
        super(ChildProcess, self).__init__()
        self.conn = conn

    def run(self):
        print('Attempting to pipein to pipe')
        self.conn.send('My Name is Elliot')
        self.conn.close()


def main():
    conn1, conn2 = multiprocessing.Pipe()

    child = ChildProcess(conn2)
    child.start()
    child.join()
    
    pipeContent = conn1.recv()
    print('Pipe : {}'.format(pipeContent))

    conn1.close()


if __name__ == '__main__':
    main()
