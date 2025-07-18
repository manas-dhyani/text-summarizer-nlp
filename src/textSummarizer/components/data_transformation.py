import os
from textSummarizer.logging import logger
from transformers import AutoTokenizer
from datasets import load_dataset, load_from_disk
from textSummarizer.entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)

    def convert_examples_to_features(self,example_batch):
        input_encodings = self.tokenizer(example_batch['dialogue'] , max_length = 1024, truncation = True )
        
        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(example_batch['summary'], max_length = 128, truncation = True )
            
        return {
            'input_ids' : input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }
    def convert(self):
    # 1) Load from a true local path
        dataset_dir = self.config.data_path.resolve().as_posix()
        dataset_samsum = load_from_disk(dataset_dir)

    # 2) Tokenize
        dataset_samsum_pt = dataset_samsum.map(
        self.convert_examples_to_features,
        batched=True
    )

    # 3) Save to a true local path
        output_dir = (self.config.root_dir / "samsum_dataset").resolve().as_posix()
        dataset_samsum_pt.save_to_disk(output_dir)


    
