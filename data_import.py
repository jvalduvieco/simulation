#!/usr/bin/python
import logging
import multiprocessing
import csv
from Family import Family
from consumer import Consumer
from data_adapters import person_from_row
from writer import Writer

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def simulate_stream(input_file, output_stream):
    task_queue = multiprocessing.JoinableQueue()
    results_queue = multiprocessing.Queue()
    num_consumers = multiprocessing.cpu_count()
    reader = csv.DictReader(open(input_file), delimiter=',')

    start_consumers(num_consumers, results_queue, task_queue)

    writer = Writer(results_queue, output_stream)
    writer.start()

    publish_rows(reader, task_queue)

    end_consumers(num_consumers, task_queue)

    logger.info("Waiting for processes to die...")
    # Wait for all of the tasks to finish
    task_queue.join()
    writer.join()
    logger.info("Done ...")


def start_consumers(num_consumers, results, tasks):
    logger.info('Creating %d consumers' % num_consumers)
    consumers = [Consumer(tasks, results)
                 for i in xrange(num_consumers)]
    for w in consumers:
        w.start()


def end_consumers(num_consumers, tasks):
    logger.info("Killing everyone...")
    for i in xrange(num_consumers):
        tasks.put(None)


def publish_rows(reader, tasks):
    current_family = None
    row_number = 0
    for row in reader:
        person = person_from_row(row)

        if current_family is None:
            current_family = Family(person.familiy_id)

        if current_family.ID == person.familiy_id:
            current_family.add_person(person)
        else:
            tasks.put(current_family)
            current_family = Family(person.familiy_id)
            current_family.add_person(person)
        row_number += 1
        if row_number % 10000 == 0:
            logger.info(row_number)
    tasks.put(current_family)
