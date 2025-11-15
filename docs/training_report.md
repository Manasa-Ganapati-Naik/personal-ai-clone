# Training Report

## Dataset Information
- Number of training examples: 270
- Number of tokens: 4820

## Training Hyperparameters
- Model: GPT-2 / DistilGPT2
- LoRA: r=8, alpha=32, dropout=0.05
- Batch size: 2
- Gradient accumulation: 4
- Epochs: 3
- Learning rate: 2e-4
- FP16: True
- Max token length: 256

## Loss Graphs
Loss graph not available.

## Sample Inference
**Prompt 1:** Hey, are we still meeting tomorrow?
**Generated:** Hey, are we still meeting tomorrow? What do we need to do to get here?"

"I-I'm not here for you. I just need some time off from work."

She looked up at me and nodded toward the

**Prompt 2:** Dear team, please review the document attached.
**Generated:** Dear team, please review the document attached.

As you can see, there's something very wrong with this document. In short, it's almost impossible to define and implement your own language. And there are lots of reasons why it's an

**Prompt 3:** Happy birthday! Hope your day is amazing!
**Generated:** Happy birthday! Hope your day is amazing! I'm going to try to do my best to bring you some time with me, so please let me know if you have any questions or want to come out and discuss your journey, or just want to

## Metrics
**Prompt 1:** Hey, are we still meeting tomorrow?
- Generated: Hey, are we still meeting tomorrow? What do we need to do to get here?"

"I-I'm not here for you. I just need some time off from work."

She looked up at me and nodded toward the
- Perplexity: 44.29
- SBERT similarity: 0.74

**Prompt 2:** Dear team, please review the document attached.
- Generated: Dear team, please review the document attached.

As you can see, there's something very wrong with this document. In short, it's almost impossible to define and implement your own language. And there are lots of reasons why it's an
- Perplexity: 64.83
- SBERT similarity: 0.37

**Prompt 3:** Happy birthday! Hope your day is amazing!
- Generated: Happy birthday! Hope your day is amazing! I'm going to try to do my best to bring you some time with me, so please let me know if you have any questions or want to come out and discuss your journey, or just want to
- Perplexity: 74.43
- SBERT similarity: 0.76

