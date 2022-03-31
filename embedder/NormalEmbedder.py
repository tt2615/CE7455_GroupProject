import torch.nn as nn

class NormalEmbedder(nn.Module):
    def __init__(self, vocab_size, emsize, padding_idx=0): 
        super(NormalEmbedder, self).__init__()

        self.vocab_size = vocab_size
        self.emsize = emsize
        self.padding_idx = padding_idx
        self.embed = nn.Embedding(self.vocab_size, self.emsize, self.padding_idx)

    def forward(self, tokens):
        return self.embed(tokens)