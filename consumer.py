import logging
import multiprocessing

from OpenFisca_simulator import Simulator

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class Consumer(multiprocessing.Process):

    def __init__(self, task_queue, result_queue):
        multiprocessing.Process.__init__(self)
        self.task_queue = task_queue
        self.result_queue = result_queue
        self.simulator = Simulator()

    def run(self):
        jobs_processed = 0
        proc_name = self.name
        while True:
            next_task = self.task_queue.get()
            if next_task is None:
                # Poison pill means shutdown
                logger.info('%s: Exiting' % proc_name)
                self.result_queue.put('DONE')
                self.task_queue.task_done()
                break
            answer = zip([v.ID for v in next_task.persons], self.simulator.simulate('GG_270_mensual', '2017-1', next_task))
            self.task_queue.task_done()
            self.result_queue.put(answer)
            jobs_processed += 1
        return
