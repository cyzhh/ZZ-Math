# MMOS

## 🔥 News

- [2024/1/11] Dataset released at [😊 HuggingFace](https://huggingface.co/datasets/cyzhh/TAL-SCQ-CN_mix)

## 💾 Install

    git clone https://github.com/cyzhh/MATH-PROBLEM-SOLVING---TRACK1.git
    cd MATH-PROBLEM-SOLVING---TRACK1
    conda create -n MMOS python=3.10
    pip install packaging==22.0
    conda install pytorch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 pytorch-cuda=11.7 -c pytorch -c nvidia
    pip install -r requirements.txt

## 📚 Dataset

Our dataset is inference GSM8K, MATH, TAL-SCQ by the open source big model ToRA series and processed by the algorithm to finally get the dataset TAL-SCQ-CN_mix.

The DATA, which we publish at [😊 HuggingFace](https://huggingface.co/datasets/cyzhh/TAL-SCQ-CN_mix), need to be placed under the relative path, `./train_data/TAL-SCQ-CN_mix/`.

If you are interested in our work, we will publish details about the data processing aspects after the paper is published.

## 🚀 Training
Due to resource constraints, we performed supervised fine-tuning on [CodeLLaMA 7B](https://huggingface.co/codellama/CodeLlama-7b-Python-hf) using our dataset on 8 A100 40G GPUs. To reproduce our work from CodeLLaMA 7B, you can train according to the following instruction.

    bash scripts/train_single.sh codellama 7b
    
## 💻 Inference
If you want to use our trained model directly to verify the authenticity of the results, then you can do so by downloading [the trained model](https://www.wolai.com/tC892NbsDTG1NEwnmkz53B) and placing the model in the relative path, `./train_outputs/codellama_7b/`.

You need to change the input path and output path here after first instruction, the general input relative path is `./outputs/codellama_7b/TAL-SCQ-CN_mix_ep1/TAL-CN/` folder under the path of the jsonl file.

    bash scripts/infer.sh
    python src/submit.py

The path to the Track1-WithoutAPI experiment results is at `. /outputs/codellama_7b/TAL-SCQ-CN_mix_ep1/TAL-CN/submit.jsonl`

## 😍 Future

If more GPU resources become available, we will release our 13B model as well as the 34B model!

## 😇 Acknowledgements

- [ToRA](https://github.com/microsoft/ToRA?tab=readme-ov-file)

