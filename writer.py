import csv
import multiprocessing


class Writer(multiprocessing.Process):

    def __init__(self, result_queue, results_stream=None):
        multiprocessing.Process.__init__(self)
        self.result_queue = result_queue
        self.results_stream = results_stream

    def run(self):
        proc_name = self.name
        jobs_processed = 0
        workers_done = 0
        num_consumers = multiprocessing.cpu_count()
        aggregated_results = {}
        while True:
            simulation_result = self.result_queue.get()
            if simulation_result == 'DONE':
                workers_done += 1
                if num_consumers == workers_done:
                    break
                else:
                    continue
            jobs_processed += 1

            for person_id, amount in simulation_result:
                aggregated_results[int(person_id)] = amount + 0

        if self.results_stream is not None:
            out_file = open(self.results_stream, 'wb')
            writer = csv.writer(out_file, delimiter=',')
            writer.writerow(['ID_PERS', 'IMPORT_RGC'])
            for key in sorted(aggregated_results.iterkeys()):
                writer.writerow((key, aggregated_results[key]))
            out_file.close()
        else:
            for key in sorted(aggregated_results.iterkeys())[0:100]:
                print "%s: %s" % (key, aggregated_results[key])

        return
