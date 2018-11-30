import logging
import sys
import time

from data_import import simulate_stream

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


if __name__ == "__main__":
    assert len(sys.argv) == 3, "Missing parameters: " + sys.argv[0] + " <input_data> <file_with_results>"
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    start_time = time.time()
    simulate_stream(input_file, output_file)
    elapsed_time = time.time() - start_time
    logger.info("elapsed time: " + time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
