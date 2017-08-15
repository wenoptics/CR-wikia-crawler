import multiprocessing
import os
import traceback

import sys


class AutoMTTask:
    def __init__(self):
        self.task_list = []

    def set_task_list(self, tasks: list):
        self.task_list = tasks

    def _do_with_each(self, single_piece_of_task):
        print('[i] do jobs from %s, with the task %s' % (os.getpid(), single_piece_of_task))
        try:
            return self.jobs(single_piece_of_task)
        except Exception:
            traceback.print_exc(file=sys.stdout)

    def jobs(self, single_piece_of_task):
        raise NotImplementedError("write you code here")

    def go(self, threads_num=2):
        pool = multiprocessing.Pool(processes=threads_num)
        ret = pool.map(self._do_with_each, self.task_list)
        pool.close()
        pool.join()

        return ret


############################################################################
class __AT(AutoMTTask):
    """
    This is an sample class
    """

    def jobs(self, single_piece_of_task):
        return "the content of the web from `%s`" % single_piece_of_task


if __name__ == '__main__':
    # This is an example
    at = __AT()
    at.set_task_list([
        'http://baidu.com',
        'http://taobao.com',
    ])
    at.go()
