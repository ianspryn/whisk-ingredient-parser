#!/usr/bin/env python2

import json
from subprocess import check_output
import tempfile

import utils


def _exec_crf_test(input_text):
    with tempfile.NamedTemporaryFile() as input_file:
        input_file.write(utils.export_data(input_text))
        input_file.flush()
        return check_output(
            ['crf_test', '--verbose=1', '--model', 'ingredient-parser.crfmodel',
             input_file.name])


def _convert_crf_output_to_json(crf_output):
    return json.dumps(utils.import_data(crf_output), indent=2, sort_keys=True)


def parse(ingredients):
    crf_output = _exec_crf_test(ingredients)
    return _convert_crf_output_to_json(crf_output.split('\n'))
