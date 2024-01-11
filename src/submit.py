import os
import json
import random
from datasets import load_dataset, Dataset, concatenate_datasets
from sympy import simplify, N, evalf
from sympy.parsing.sympy_parser import parse_expr
from sympy.parsing.latex import parse_latex
import re
from pathlib import Path
from typing import Iterable, Union, Any


def load_jsonl(file: Union[str, Path]) -> Iterable[Any]:
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            try:
                yield json.loads(line)
            except:
                print("Error in loading:", line)
                exit()

def parse(s):
    for f in [parse_latex]:
        try:
            return f(s).evalf()
        except:
            pass
    return s



if __name__ == '__main__':
    """
    You need to change the input path and output path here, the general input path is ". /outputs/codellama_7b/TAL-SCQ-CN_mix_ep1/TAL-CN/" folder under the path of the jsonl file.
    """
    data_file = './outputs/codellama_7b/TAL-SCQ-CN_mix_ep1/TAL-CN/0_test_tora_-1_seed0_t0.0_s0_e7436_01-11_17-42.jsonl'
    save_path = './outputs/codellama_7b/TAL-SCQ-CN_mix_ep1/TAL-CN/submit.jsonl'

    examples = list(load_jsonl(data_file))

    # print('number:',len(examples))
    submits = {}
    for example in examples:
        queId = example['queId']
        pred = example['pred'][0]
        # print(pred)
        if pred == None:
            submits[queId] = "0"
        else:
            if "Error" in pred:
                submits[queId] = "0"
            else:

                answer = str(parse(pred))
                answer = re.sub('[^a-zA-Z0-9.+-]', '', answer)

                submits[queId] = answer



    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(submits, f, indent=4)
